from flask import Flask, render_template, request, jsonify
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch
import requests
from bs4 import BeautifulSoup

# Tạo ứng dụng Flask
app = Flask(__name__)

# Tải mô hình và tokenizer
model = AutoModelForSequenceClassification.from_pretrained("phobert_fake_news_model/")
tokenizer = AutoTokenizer.from_pretrained("phobert_fake_news_model/")

# Hàm trích xuất nội dung văn bản từ một URL
def extract_text_from_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    paragraphs = soup.find_all('p')
    text = '\n'.join([para.get_text() for para in paragraphs])
    return text

# Hàm dự đoán tin giả cho một đoạn văn
def predict_fake_news_hf(text):
    max_length = 500
    inputs = tokenizer(text, return_tensors='pt', truncation=True, padding=True, max_length=max_length)
    with torch.no_grad():
        outputs = model(**inputs)
    prediction = torch.argmax(outputs.logits, dim=1).item()
    return "Thật" if prediction == 1 else "Giả"

# Hàm quét toàn bộ bài báo
def scan_article_for_fake_news(url):
    article_text = extract_text_from_url(url)
    paragraphs = article_text.split('\n')
    
    fake_paragraphs_set = set()  # Sử dụng tập hợp để loại bỏ trùng lặp
    total_paragraphs = len(paragraphs)
    
    for paragraph in paragraphs:
        if paragraph.strip():
            result = predict_fake_news_hf(paragraph)
            if result == "Giả":
                fake_paragraphs_set.add(paragraph)
    
    fake_percentage = (len(fake_paragraphs_set) / total_paragraphs) * 100
    
    return {
        "fake_percentage": fake_percentage,
        "fake_paragraphs": list(fake_paragraphs_set)  # Chuyển đổi tập hợp thành danh sách
    }


# Route để hiển thị trang chủ
@app.route('/')
def index():
    return render_template('index.html')

# Route để xử lý form nhập URL
@app.route('/scan', methods=['POST'])
def scan():
    url = request.form['url']
    result = scan_article_for_fake_news(url)
    
    return jsonify(result)

# Chạy ứng dụng Flask
if __name__ == '__main__':
    app.run(debug=True)
