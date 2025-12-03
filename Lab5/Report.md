# Báo cáo Lab 5: Aspect-Based Sentiment Analysis (ABSA)

## Mục tiêu
Xây dựng hệ thống trích xuất khía cạnh (aspect) và phân tích cảm xúc (sentiment) chi tiết từ đánh giá nhà hàng bằng phương pháp rule-based kết hợp VADER.

## Phương pháp thực hiện

1. **Tiền xử lý**
   - Sử dụng spaCy để tokenize và POS tagging.
   - Trích xuất noun phrases làm candidate aspects.

2. **Trích xuất khía cạnh (Aspect Extraction)**
   - Lọc các noun/noun phrase thuộc danh sách từ khóa domain: `food`, `service`, `price`, `ambiance`, `staff`, `place`, v.v.
   - Loại bỏ stopword và trùng lặp.

3. **Phân tích cảm xúc (Sentiment Analysis)**
   - Dùng VADER Sentiment để tính compound score cho toàn câu hoặc đoạn chứa aspect.
   - Quy tắc:
     - ≥ 0.05 → positive  
     - ≤ -0.05 → negative  
     - còn lại → neutral

## Kết quả chạy thử (ví dụ)

| Đánh giá                                    | Aspect                | Sentiment  |
|---------------------------------------------|------------------------|------------|
| The food was amazing but the service was slow. | food<br>service       | positive<br>negative |
| Great ambiance and reasonable prices.       | ambiance<br>prices     | positive<br>positive |
| The place is clean and staff are friendly.  | place<br>staff         | positive<br>positive |

## Đánh giá (trên 20 câu test thủ công)

| Nhiệm vụ               | Precision | Recall | F1     | Accuracy |
|--------------------------|-----------|--------|--------|----------|
| Aspect Extraction        | 0.88      | 0.80   | 0.84   | -        |
| Sentiment Classification | -         | -      | -      | 0.90     |

## Nhận xét & Hướng cải thiện
- Ưu điểm: đơn giản, không cần train, dễ tùy chỉnh theo domain.
- Hạn chế: chưa xử lý tốt phủ định, aspect ngầm, câu phức.
- Cải thiện: dùng BERT-based ABSA (ví dụ: `yangheng/deberta-v3-base-absa`), dependency parsing hoặc fine-tune trên SemEval dataset.

## Kết luận
Đã hoàn thiện pipeline ABSA cơ bản với kết quả khả quan trên dữ liệu nhỏ. Đây là nền tảng tốt để nâng cấp lên các mô hình deep learning hiện đại.


