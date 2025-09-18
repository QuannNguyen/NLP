# Các bước triển khai 
- Cài đặt SimpleTokenizer và RegexTokenizer để tách từ.
    + SimpleTokenizer: tách từ dựa vào ký tự khoảng trắng và dấu câu.
    + RegexTokenizer: sử dụng biểu thức chính quy để tách từ, xử lý tốt hơn dấu câu, chữ + số.
- Viết hàm load_raw_text_data để đọc dữ liệu từ UD_English-EWT.
- Code trong main.py:
    + task1_2(): chạy tokenizer trên 3 câu mẫu.
    + task3(): tự động giải nén UD_English-EWT.tar.gz, đọc dữ liệu, tokenize và so sánh.
    + Chạy python main.py để xem output.

# Cách chạy code và log kết quả
- Clone repo về:
    '''bash
    git clone https://github.com/QuannNguyen/NLP.git
    cd NLP/Lab1
    python main.py
    '''
- Chạy file main.py sẽ ra log kết quả.
- log kết quả sẽ gồm
    + Output của SimpleTokenizer và RegexTokenizer trên câu mẫu có sẵn.
    + Token đầu tiên, số lượng token, và so sánh side-by-side trên dữ liệu thực.
# Giải thích kết quả thu được
## Trên các câu mẫu
- Câu 1: "Hello, world! This is a test of the tokenizer modules."
    + Cả SimpleTokenizer và RegexTokenizer đều tách được dấu câu riêng biệt (",", "!", ".") nên kết quả giống nhau.
- Câu 2: "NLP is fascinating... isn't it?"
    + Cả hai tokenizer đều tách dấu ... thành ba dấu ".".
    + Contraction "isn't" được tách thành ["isn", "'", "t"] ở cả hai tokenizer nên không giữ nguyên dạng "isn't".

- Câu 3: "Let's see how it handles 123 numbers and punctuation!"
    + "Let's" được tách thành ["Let", "'", "s"].
    + Số "123" được giữ nguyên như một token.
    + Dấu "!" được tách riêng.
    + Kết quả SimpleTokenizer và RegexTokenizer vẫn giống nhau.

## Trên dữ liệu thực 
    Đoạn văn bản gốc: "Al - Zaman : American forces killed Shaikh Abdullah al - Ani , the preacher at the mosque ..."
    Kết quả tokenization:
    SimpleTokenizer và RegexTokenizer đều cho output giống hệt nhau.
    Ví dụ: "Al", "-", "Zaman", ":", "Ani", ",", "the", …
    Số lượng token:
        + SimpleTokenizer: 102
        + RegexTokenizer: 102
# Khó khăn và cách giải quyết
    Đường dẫn dataset: nếu hardcode theo máy cá nhân thì người khác không chạy được. Có thể giải quyết bằng cách nén thành .tar.gz và code tự động giải nén.
# Nguồn tham khảo
    Documents của python và các thư viện.