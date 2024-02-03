import streamlit as st
from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline

model = AutoModelForQuestionAnswering.from_pretrained("AndyChiang/Pre-CoFactv3-Question-Answering")
tokenizer = AutoTokenizer.from_pretrained("AndyChiang/Pre-CoFactv3-Question-Answering")

QA = pipeline("question-answering", model=model, tokenizer=tokenizer)

st.title("Модель ответов на вопросы")

context = st.text_area("Введите контекст: ")
question = st.text_area("Введите вопрос:")
process = st.button("Запустить")

if process:
    QA_input = { 'context' : context, 'question': question, }
    answer = QA(QA_input)
    st.write(answer)