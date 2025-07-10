from flask import Flask, request, jsonify
from chatbot_logic import load_documents, create_vectorstore
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA

app = Flask(__name__)
docs = load_documents()
db = create_vectorstore(docs)
qa = RetrievalQA.from_chain_type(llm=ChatOpenAI(), retriever=db.as_retriever())

@app.route("/ask", methods=["POST"])
def ask():
    query = request.json.get("query")
    result = qa.run(query)
    return jsonify({"answer": result})

if __name__ == "__main__":
    app.run(debug=True)
