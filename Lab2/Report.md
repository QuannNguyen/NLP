# Các bước triển khai
- Xây dựng interface Vectorizer với 3 method:
    + fit(corpus): học vocabulary từ corpus.
    + transform(documents): biến documents thành ma trận số đếm (count vectors).
    + fit_transform(corpus): tiện ích gọi fit rồi transform.
- Cài đặt class CountVectorizer kế thừa Vectorizer:
    + Trong constructor nhận vào một Tokenizer.
    + fit: token hóa toàn bộ corpus, thu thập token duy nhất, xây dựng vocabulary_.
    + transform: duyệt từng document, tạo vector đếm theo vocabulary.
    + fit_transform: kết hợp cả hai bước.
- Code trong lab2_test.py
    + main() chạy trên câu mẫu
    + main2() chạy trên datasets
# Cách chạy code và log kết quả
- Clone repo về:

```bash
git clone https://github.com/QuannNguyen/NLP.git
cd NLP/Lab2
python lab2_test.py
```
- Chạy file lab2_test.py
- log kết quả gồm
    + Vocabulary đã học được.
    + Document-term matrix (list vector đếm cho từng document).
# Giải thích kết quả thu được
- Vocabulary là tập hợp tất cả các token duy nhất trong corpus, mỗi token được ánh xạ sang một index.
- Document-term matrix cho biết số lần xuất hiện của mỗi token trong từng văn bản:
    + Ví dụ: [0, 1, 1, 0, ...] nghĩa là document này có 1 lần xuất hiện từ "I", 1 lần từ "NLP", nhưng không có "AI".
- Trên dataset UD English EWT:
    + Vocabulary rất lớn do chứa nhiều từ, ký hiệu, dấu câu.
    + Vector của mỗi document thưa (đa số là 0), đúng với đặc trưng của mô hình bag-of-words.
# Khó khăn và cách giải quyết
- Kích thước vocabulary lớn: gây ra ma trận sparse và tốn bộ nhớ. Có thể giải quyết bằng cách giới hạn vocabulary, bỏ stopwords, hoặc chỉ lấy top-k từ phổ biến.
# Nguồn tham khảo
    - Documents của python và các thư viện.