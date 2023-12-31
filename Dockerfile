FROM python:3.10.12
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /cars

COPY requirements.txt /cars/
RUN pip install -r requirements.txt

COPY . .