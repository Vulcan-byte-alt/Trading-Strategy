FROM python:3.10-slim

WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy strategy files
COPY your_strategy.py .
COPY startup.py .

# Copy base template (if needed in container)
COPY ../base-bot-template /app/base/

# Set environment
ENV PYTHONUNBUFFERED=1

# Run startup script
CMD ["python", "startup.py"]
