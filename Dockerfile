# Use official Python 3.10 slim image as base
FROM python:3.12-slim

# Set working directory in the container
WORKDIR /app

# Copy project files
COPY rtsp_stream.py .
COPY requirements.txt .

# Install FFmpeg minimally (assuming it's available in the base image or via pip dependencies)
# We'll rely on opencv-python's prebuilt FFmpeg support
RUN apt-get update -qq && apt-get install -y ffmpeg || echo "FFmpeg install failed, relying on pip opencv-python" \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Command to run the script
CMD ["python", "rtsp_stream.py"]