FROM python:3.10.16

ENV PYTHONUNBUFFERED=1

WORKDIR /code

# Install system packages
RUN apt-get update && apt-get install -y \
    libpq-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

CMD ["sh", "-c", "python manage.py makemigrations && python manage.py migrate && gunicorn weather_data.wsgi:application --bind 0.0.0.0:8000"]

