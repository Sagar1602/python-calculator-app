FROM python:3.11-slim

# Install Tkinter dependencies
RUN apt-get update && \
    apt-get install -y python3-tk x11-apps && \
    apt-get clean

WORKDIR /app
COPY app.py .

# Run the calculator UI
CMD ["python", "app.py"]
