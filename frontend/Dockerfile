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
RUN chown -R appuser:appuser /app
# MITIGATION 3: Enforce non-root execution
USER 1000
EXPOSE 8501
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]

