import streamlit as st
import requests

st.set_page_config(page_title="Chatbot Tra cứu Văn bản", layout="wide")
st.title("📄 Chatbot Tra cứu Văn bản Hành chính")

st.markdown("Hỏi chatbot về nội dung văn bản bạn đã cung cấp (PDF/DOCX)")

query = st.text_input("✍️ Nhập câu hỏi của bạn:")

if query:
    with st.spinner("Đang truy vấn..."):
        try:
            response = requests.post(
                "http://localhost:5000/ask",  # URL Flask local
                json={"query": query}
            )
            data = response.json()
            st.success(data["answer"])
        except Exception as e:
            st.error(f"Lỗi truy vấn: {e}")
