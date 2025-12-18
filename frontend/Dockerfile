# FIX 1: Base Image Upgrade
FROM python:3.12-slim
# MITIGATION 3: User Creation
RUN groupadd -r appuser && useradd -r -g appuser -u 1000 appuser
WORKDIR /app
# FIX 2: Pip Upgrade
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt
COPY . .
# Transfer ownership for the new user
RUN chown -R appuser:appuser /app
# MITIGATION 3: Enforce non-root execution
USER 1000
# Expose standard HTTP port
EXPOSE 80
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

