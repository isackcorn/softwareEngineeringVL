from fastapi import APIRouter, Depends
from pydantic import BaseModel
from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline


router = APIRouter(
    prefix="/contextQuestionAns",
    tags=["contextQuestionAns"]
)


@router.post("/")
async def contextQuestionAns(
    context,
    question):

    model = AutoModelForQuestionAnswering.from_pretrained("AndyChiang/Pre-CoFactv3-Question-Answering")
    tokenizer = AutoTokenizer.from_pretrained("AndyChiang/Pre-CoFactv3-Question-Answering")
    QA = pipeline("question-answering", model=model, tokenizer=tokenizer)
    
    result = QA(context, question)

    return result