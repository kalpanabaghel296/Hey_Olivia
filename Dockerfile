FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy dependency list first (for better caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY backend/ backend/
COPY ml/ ml/
COPY frontend/ frontend/

# Expose Flask port
EXPOSE 5000

# Start Flask app
CMD ["python", "backend/app.py"]