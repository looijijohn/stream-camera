# Use official Python 3.10 slim image as base
FROM python:3.10-slim

# Set working directory in the container
WORKDIR /app

# Install system dependencies for OpenCV (includes FFmpeg for RTSP support)
RUN apt-get update && apt-get install -y \
    libopencv-dev \
    python3-opencv \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Copy project files (excluding config.yaml)
COPY rtsp_stream.py .
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Command to run the script
CMD ["python", "rtsp_stream.py"]