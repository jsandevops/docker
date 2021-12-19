FROM python:3.9

WORKDIR /app

ENV POSTGRES_IP='172.17.0.2'

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 9091

CMD ["python", "hostdb.py"]
