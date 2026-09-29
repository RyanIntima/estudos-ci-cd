FROM python:3.12

COPY requirements.txt /app

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

CMD ["python", "main.py", "uvicorn app.main:app --reload"]