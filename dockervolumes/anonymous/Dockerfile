FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 9090

VOLUME ["/app"]

CMD ["python", "countrydetails.py"]
