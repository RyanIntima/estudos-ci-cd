FROM python:3.12

COPY requirements.txt /app_teste/

WORKDIR /app_teste/

RUN pip install -r requirements.txt

COPY . /app_teste/

CMD ["python", "main.py", "uvicorn app.main:app --reload"]