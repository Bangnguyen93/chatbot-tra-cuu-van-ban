# Chatbot Tra cứu Văn bản (Python + LangChain + OpenAI)

Chatbot này giúp tra cứu nội dung từ văn bản PDF/DOCX đã được upload (ví dụ: văn bản pháp luật, công văn, tài liệu học tập...).

## Cài đặt

```bash
pip install -r requirements.txt
```

## Chạy local

```bash
python app.py
```

Gửi truy vấn POST đến `/ask` với JSON:
```json
{"query": "Nội dung công văn 123 là gì?"}
```
