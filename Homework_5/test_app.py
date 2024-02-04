from fastapi.testclient import TestClient
from app import router

client = TestClient(router)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200


def test_answer():
    response = client.post("/contextQuestionAns/", json={"context": "Я люблю машинное обучение!", "question": "Кто любит машинное обучение"})
    json_data = response.json()
    assert response.status_code == 200
    assert json_data['answer'] == 'Я'


def test_answer2():
    response = client.post("/contextQuestionAns/", json={"context": "Я люблю машинное обучение!", "question": "Что я люблю?"})
    json_data = response.json()
    assert response.status_code == 200
    assert json_data['answer'] == 'машинное обучение'