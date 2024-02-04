## Модель ответов на вопросы с возможностью развертывания в облаке

### Требования

Для работы с приложением установите библиотеки при помощи следующих команд:
```python
pip install transformers
pip install tensorflow
pip install torch
pip install streamlit
```
В случае развертывания приложения в облаке необходимые зависимости автоматически выгрузятся из файла `requirements.txt`.

## Использование
- Клонируйте или загрузите репозиторий на свой локальный компьютер или в удаленный репозиторий.
- Если используется облако Streamlit, укажите при развертывании приложения путь до исполняемого файла.
- Запустите программу `app.py` локально, или в виде Web-приложения на Streamlit.
- Введите контекст и вопрос по запросу от программы

## Пример использования
В качестве примера использования можно посмотреть развернутое на Streamlit [приложение](https://softwareengineeringvl-xexb2cqut3l9mrdydqbsxs.streamlit.app/)

Если у Вас не работают гиперссылки: https://softwareengineeringvl-xexb2cqut3l9mrdydqbsxs.streamlit.app/

### Используемая модель
Используется предобученная модель: [Pre-CoFactv3-Question-Answering](https://huggingface.co/AndyChiang/Pre-CoFactv3-Question-Answering)

### Автор
Лобачев В.И., РИМ-130962
