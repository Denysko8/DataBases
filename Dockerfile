# Multi-stage Dockerfile for the Flask app
# Usage:
#  docker build -t databases-app:latest .
#  docker run -e USER=... -e PASSWORD=... -e PUBLIC_IP=... -e DB_NAME=... -p 5000:5000 databases-app:latest

FROM python:3.11-slim as builder
WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    libmysqlclient-dev \
 && rm -rf /var/lib/apt/lists/*

# Copy deps and install them into a wheelhouse to speed up builds
COPY requirements.txt req2.txt /app/
RUN python -m pip install --upgrade pip
RUN pip wheel --no-cache-dir --wheel-dir /wheels -r requirements.txt || true
RUN pip wheel --no-cache-dir --wheel-dir /wheels -r req2.txt || true

FROM python:3.11-slim
WORKDIR /app

# System deps for runtime
RUN apt-get update && apt-get install -y --no-install-recommends \
    libmysqlclient21 \
 && rm -rf /var/lib/apt/lists/*

# Copy wheels and install
COPY --from=builder /wheels /wheels
COPY requirements.txt req2.txt /app/
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir --find-links=/wheels -r requirements.txt || pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir --find-links=/wheels -r req2.txt || pip install --no-cache-dir -r req2.txt

# Copy app code
COPY . /app

# Expose port
EXPOSE 5000

# Environment defaults (override with docker run -e ...)
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

# Use gunicorn in production
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app", "--workers=3", "--threads=2"]
