# Sử dụng Python nhẹ, slim
FROM python:3.11-slim

# Thư mục làm việc
WORKDIR /app

# Copy requirements và cài đặt
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy toàn bộ source code
COPY . .

# Sử dụng Gunicorn với 1 worker để tiết kiệm RAM
CMD ["gunicorn", "-w", "1", "-k", "uvicorn.workers.UvicornWorker", "main:app", "-b", "0.0.0.0:8080"]
