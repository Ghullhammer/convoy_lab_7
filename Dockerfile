FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ ./app/

RUN adduser --disabled-password --gecos '' appuser
USER appuser

EXPOSE 5000

ENV FLASK_APP=app/main.py
ENV PORT=5000

CMD ["python", "app/main.py"]