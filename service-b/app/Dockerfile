FROM python:3.11-slim

WORKDIR /app

COPY service-b/app/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY service-b/app .

COPY shared shared

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
