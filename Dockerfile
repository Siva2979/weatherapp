FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Default API key (will be overridden by --env-file)
ENV WEATHER_API_KEY=""

# Expose the port
EXPOSE 5000

# Run the application
CMD ["flask", "run"]