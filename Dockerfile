FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

# system deps (build tooling for some wheels)
RUN apt-get update && apt-get install -y build-essential && rm -rf /var/lib/apt/lists/*

# deps
COPY requirements.txt .
RUN pip install -r requirements.txt

# app
COPY . .

# static will be produced by entrypoint
EXPOSE 8000

# use our entrypoint so migrations/static run on each deploy
CMD ["bash", "-c", "./entrypoint.sh"]