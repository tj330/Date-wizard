FROM python:3.11

WORKDIR /app

COPY requirements.txt /app

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 8000

ENTRYPOINT ["python3"]

CMD ["manage.py", "runserver","0.0.0.0:8000"]
