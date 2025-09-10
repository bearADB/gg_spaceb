# Dockerfile hoàn chỉnh với fix PORT
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# entrypoint shell để sử dụng PORT từ Cloud Run
CMD exec gunicorn -w 1 -k uvicorn.workers.UvicornWorker main:app -b 0.0.0.0:${PORT:-8080}
