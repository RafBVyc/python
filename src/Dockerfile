FROM python:3.11-alpine

WORKDIR /app

RUN mkdir -p data logs

COPY src/ .

CMD ["python", "-u", "main.py"]