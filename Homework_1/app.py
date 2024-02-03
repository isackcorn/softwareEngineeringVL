# model: https://huggingface.co/AndyChiang/Pre-CoFactv3-Question-Answering
from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline

model = AutoModelForQuestionAnswering.from_pretrained("AndyChiang/Pre-CoFactv3-Question-Answering")
tokenizer = AutoTokenizer.from_pretrained("AndyChiang/Pre-CoFactv3-Question-Answering")

QA = pipeline("question-answering", model=model, tokenizer=tokenizer)

context = input("Введите контекст: \n")
question = input("Введите вопрос: \n")

QA_input = { 'context' : context, 'question': question, }
answer = QA(QA_input)
print(answer)