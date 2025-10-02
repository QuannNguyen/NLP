package com.harito.spark

import org.apache.spark.sql.SparkSession
import org.apache.spark.ml.Pipeline
import org.apache.spark.ml.feature.{HashingTF, IDF, RegexTokenizer, StopWordsRemover, Normalizer}
import org.apache.spark.sql.functions._
import org.apache.hadoop.fs.{FileSystem, Path}
import java.io.{File, PrintWriter}
import java.time.LocalDateTime

object Lab17_NLPPipeline {
  def main(args: Array[String]): Unit = {
    // Initialize Spark Session
    val spark = SparkSession.builder
      .appName("NLP Pipeline Example")
      .master("local[*]")
      .getOrCreate()

    import spark.implicits._
    println("Spark Session created successfully.")
    println(s"Spark UI available at http://localhost:4040")
    Thread.sleep(3000)

    // Initialize log file
    val logPath = "../log/lab17_metrics.log"
    new File(logPath).getParentFile.mkdirs()
    val logWriter = new PrintWriter(new File(logPath))

    val jobStartTime = LocalDateTime.now()
    logWriter.println(s"Job Start Time: $jobStartTime")

    try {
      // ------------------------------
      // 1. Read Dataset with Limit
      // ------------------------------
      val limitDocuments = 5000 // <-- customize this value easily
      val dataPath = "../data/c4-train.00000-of-01024-30K.json.gz"

      val readStartTime = System.nanoTime()
      val initialDF = spark.read.json(dataPath).limit(limitDocuments)
      val recordCount = initialDF.count()
      val readDuration = (System.nanoTime() - readStartTime) / 1e9d
      logWriter.println(f"Read duration: $readDuration%.2f seconds, Records: $recordCount")
      println(f"--> Read $recordCount records in $readDuration%.2f seconds")

      initialDF.printSchema()
      initialDF.show(5, truncate = false)

      // ------------------------------
      // 2. Define Pipeline Stages
      // ------------------------------
      val tokenizer = new RegexTokenizer()
        .setInputCol("text")
        .setOutputCol("tokens")
        .setPattern("\\s+|[.,;!?()\"']")

      val stopWordsRemover = new StopWordsRemover()
        .setInputCol(tokenizer.getOutputCol)
        .setOutputCol("filtered_tokens")

      val hashingTF = new HashingTF()
        .setInputCol(stopWordsRemover.getOutputCol)
        .setOutputCol("raw_features")
        .setNumFeatures(20000)

      val idf = new IDF()
        .setInputCol(hashingTF.getOutputCol)
        .setOutputCol("tfidf_features")

      // 3. Normalization Layer
      val normalizer = new Normalizer()
        .setInputCol(idf.getOutputCol)
        .setOutputCol("features")
        .setP(2.0)

      // Pipeline
      val pipeline = new Pipeline()
        .setStages(Array(tokenizer, stopWordsRemover, hashingTF, idf, normalizer))

      // ------------------------------
      // 3. Fit Pipeline
      // ------------------------------
      println("\nFitting the NLP pipeline...")
      val fitStartTime = System.nanoTime()
      val pipelineModel = pipeline.fit(initialDF)
      val fitDuration = (System.nanoTime() - fitStartTime) / 1e9d
      logWriter.println(f"Pipeline fitting duration: $fitDuration%.2f seconds")
      println(f"--> Pipeline fitting took $fitDuration%.2f seconds.")

      // ------------------------------
      // 4. Transform Data
      // ------------------------------
      println("\nTransforming data with the fitted pipeline...")
      val transformStartTime = System.nanoTime()
      val transformedDF = pipelineModel.transform(initialDF).cache()
      val transformCount = transformedDF.count()
      val transformDuration = (System.nanoTime() - transformStartTime) / 1e9d
      logWriter.println(f"Data transformation duration: $transformDuration%.2f seconds")
      println(f"--> Transformed $transformCount records in $transformDuration%.2f seconds")

           // ------------------------------
      // 5. Similarity Computation
      // ------------------------------
      println("\nFinding similar documents...")
      val sampleDoc = transformedDF.select("features", "text").limit(1).collect()(0)
      val sampleVector = sampleDoc.getAs[org.apache.spark.ml.linalg.Vector]("features")
      val sampleText = sampleDoc.getAs[String]("text")

      val dotUdf = udf { (vec: org.apache.spark.ml.linalg.Vector) =>
        val dot = vec.toArray.zip(sampleVector.toArray).map { case (a, b) => a * b }.sum
        val norm1 = math.sqrt(sampleVector.toArray.map(x => x * x).sum)
        val norm2 = math.sqrt(vec.toArray.map(x => x * x).sum)
        if (norm1 == 0.0 || norm2 == 0.0) 0.0 else dot / (norm1 * norm2)
      }

      val similarityDF = transformedDF
        .withColumn("similarity", dotUdf($"features"))
        .select("text", "similarity")
        .orderBy(desc("similarity"))

      println(s"Sample document:\n${sampleText.take(200)}...\n")
      println("Top 5 similar documents:")
      val topDocs = similarityDF.limit(5).collect()
      topDocs.foreach { row =>
        println(f"Similarity: ${row.getAs[Double]("similarity")}%.4f | Text: ${row.getAs[String]("text").take(80)}...")
        logWriter.println(f"Similarity: ${row.getAs[Double]("similarity")}%.4f | Text: ${row.getAs[String]("text").take(80)}...")
      }


      // ------------------------------
      // 6. Save Results
      // ------------------------------
      val writeStartTime = System.nanoTime()
      val resultPath = "../results"

      val outputDF = transformedDF
        .select(concat_ws(" | ",
          substring($"text", 0, 100),
          $"features".cast("string")
        ).as("output"))

      outputDF.coalesce(1).write.mode("overwrite").text(resultPath)

      // Rename part-* to lab17_pipeline_output.txt
      val fs = FileSystem.get(spark.sparkContext.hadoopConfiguration)
      val srcFile = fs.globStatus(new Path(s"$resultPath/part-*"))(0).getPath
      val destFile = new Path(s"$resultPath/lab17_pipeline_output.txt")
      if (fs.exists(destFile)) fs.delete(destFile, true)
      fs.rename(srcFile, destFile)

      val writeDuration = (System.nanoTime() - writeStartTime) / 1e9d
      logWriter.println(f"Write duration: $writeDuration%.2f seconds")
      println(f"--> Results written in $writeDuration%.2f seconds")

    } catch {
      case e: Exception =>
        logWriter.println(s"Error occurred: ${e.getMessage}")
        e.printStackTrace()
        throw e
    } finally {
      val jobEndTime = LocalDateTime.now()
      logWriter.println(s"Job End Time: $jobEndTime")
      logWriter.close()
      spark.stop()
      println("Spark Session stopped.")
    }
  }
}
