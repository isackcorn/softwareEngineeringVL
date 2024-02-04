import streamlit as st
from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline

@st.cache_resource

def get_model():
    return pipeline("question-answering", model=AutoModelForQuestionAnswering.from_pretrained("AndyChiang/Pre-CoFactv3-Question-Answering"), tokenizer=AutoTokenizer.from_pretrained("AndyChiang/Pre-CoFactv3-Question-Answering"))

st.title("Модель ответов на вопросы")

context = st.text_area("Введите контекст: ")
question = st.text_area("Введите вопрос:")
process = st.button("Запустить")

if process:
    QA_input = { 'context' : context, 'question': question, }
    QA = get_model()
    answer = QA(QA_input)
    st.write(answer)