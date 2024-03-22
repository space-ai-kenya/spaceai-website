# Use the official Python image
FROM python:3.10-alpine

WORKDIR /app

# Add a non-root user and group
RUN addgroup -S spaceai && adduser -S spaceai -G spaceai

ENV CELERY_BROKER redis://redis:6379/0
ENV CELERY_BACKEND redis://redis:6379/1

RUN pip install -U setuptools pip

COPY ./requirements.txt .


RUN pip install -r requirements.txt

# Change the ownership to the created user and group
RUN chown -R spaceai:spaceai .


# Switch to the non-root user
USER spaceai

# Copy the entire application code
COPY . .


# Expose the port that Uvicorn will run on (adjust as needed)
EXPOSE 8000
