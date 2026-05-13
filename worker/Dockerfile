FROM python:3.11

WORKDIR /app

COPY requirements.txt .
RUN pip install redis

COPY . .

CMD ["python", "worker.py"]
