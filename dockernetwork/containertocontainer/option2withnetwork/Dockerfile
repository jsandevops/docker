FROM python:3.9

WORKDIR /app

ENV POSTGRES_SERVICE_NAME='container-postgres-db'

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 9091

CMD ["python", "hostdb.py"]
