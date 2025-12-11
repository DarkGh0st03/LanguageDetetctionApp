# FIX 1: Base Image Upgrade
# Switching to Python 3.12 resolves multiple system-level CVEs found in 3.10 (e.g., glibc, openssl)
FROM python:3.12-slim
# MITIGATION 3: Defense-in-Depth (User Creation)
# Creating a non-privileged system user (UID 1000) to prepare for privilege drop
RUN groupadd -r appuser && useradd -r -g appuser -u 1000 appuser
WORKDIR /app
# FIX 2: Supply Chain Hardening
# Explicitly upgrading pip to patch CVE-2023-5752 (Command Injection risk)
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt
COPY . .
# Transferring file ownership to the non-root user
RUN chown -R appuser:appuser /app
# MITIGATION 3: Runtime Security Enforcement
# Switching execution context to non-root.
# This neutralizes the impact of the unpatched 'tar' vulnerability (CVE-2025-45582)
# by preventing arbitrary file overwrites on system paths.
USER 1000
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

