# 1. INTEGRATION PROTOCOLS

## a.HTTP/HTTPS

They are based on a client-server model, and requests and responses are exchanged using the HTTP methods

## Sending a GET Request

To send a GET request in Python, you can use the `requests` library. Below is an example script:

```python
import requests

url = 'https://api.example.com/data'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}")

```

## b. Websockets

enables real-time communication between clients and servers.

An example of a WebSocket client in Python:

```python
import asyncio
import websockets

async def send_message():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        message = "Hello, WebSocket!"
        await websocket.send(message)
        print(f"Sent message: {message}")

        response = await websocket.recv()
        print(f"Received response: {response}")

asyncio.get_event_loop().run_until_complete(send_message())
```

## c. GraphQL

is a query language and runtime for APIs that enables clients to request only the data they need

An example of GraphQl usage in python

```python
import graphene

class Query(graphene.ObjectType):
    hello = graphene.String(description="A simple greeting")

    def resolve_hello(self, info):
        return "Hello, GraphQL!"

schema = graphene.Schema(query=Query)


```

# 2. DATA STREAMING APPLICATION

Managing a data streaming application that sends one million notifications every hour involves considerations for scalability, reliability, and efficient handling of asynchronous tasks. Here's a walkthrough with examples of technologies and configurations I would use:

### 1\. Data Streaming Platform: Apache Kafka

- Technology: Apache Kafka
- Configuration:
  - Set up a Kafka cluster to handle high-throughput, fault-tolerant data streaming.
  - Create Kafka topics for different notification types.

### 2\. Message Queue for Asynchronous Processing: RabbitMQ

- Technology: RabbitMQ
- Configuration:
  - Set up RabbitMQ for handling asynchronous tasks and decoupling notification sending from the main application.
  - Use different queues for different notification types.

### 3\. Asynchronous Task Processing: Celery with Redis Backend

- Technology: Celery, Redis
- Configuration:
  - Integrate Celery for handling asynchronous tasks.
  - Use Redis as a backend for Celery to store task results and manage distributed task queues.
  - Configure Celery workers to process tasks concurrently.

### 4\. Database: PostgreSQL for Persistence

- Technology: PostgreSQL
- Configuration:
  - Store notification data and relevant information in a PostgreSQL database for persistence.
  - Optimize database schema and indexes for efficient retrieval.

### 5\. Load Balancing and Auto-Scaling: NGINX, Docker, Kubernetes

- Technology: NGINX, Docker, Kubernetes
- Configuration:
  - Use NGINX as a reverse proxy to distribute incoming requests to multiple Flask instances.
  - Containerize the application using Docker for easy deployment and scaling.
  - Deploy on Kubernetes for automatic scaling and load balancing.

# 3. ENCRYPTION AND HASHING METHODS

One-way hashes are suitable for storing sensitive information, like passwords, where you don't need to retrieve the original data.

```python

import hashlib

def hash_password(password):
    salt = b'somesalt'
    password = password.encode('utf-8')
    hashed_password = hashlib.sha256(salt + password).hexdigest()
    return hashed_password

# Example usage
password = "securepassword"
hashed_password = hash_password(password)
print(f"Password: {password}")
print(f"Hashed Password: {hashed_password}")

```

Two-way encryption is suitable when you need to encrypt and later decrypt data, such as storing sensitive data like credit card numbers or encrypting communication channels.

```python
import bcrypt

def encrypt_data(data, secret_key):
    salt = bcrypt.gensalt()
    encrypted_data = bcrypt.hashpw(data.encode('utf-8'), salt)
    return encrypted_data

def decrypt_data(encrypted_data, secret_key):
    return bcrypt.checkpw(secret_key.encode('utf-8'), encrypted_data)

# Example usage
data = "sensitivedata"
secret_key = "secretkey"

# Encryption
encrypted_data = encrypt_data(data, secret_key)
print(f"Data: {data}")
print(f"Encrypted Data: {encrypted_data}")

# Decryption
is_valid = decrypt_data(encrypted_data, secret_key)
print(f"Is Valid: {is_valid}")

```

# Django Search and Results Page Deployment Guide

## Introduction

### Welcome to the comprehensive guide on deploying a Movie Django application with a PostgreSQL database, incorporating a search and results page. This walkthrough will cover setting up Django, configuring the PostgreSQL database, deploying the application on a nginx web server, and containerizing it with an Alpine Docker image.

# Django Project Setup: `django_project`

## PostgreSQL Configuration in `settings.py`

In the `django_project/settings.py` file, the PostgreSQL database configuration is as follows:

`# django_project/settings.py`

```sql
DATABASES = {
"default": {
"ENGINE": "django.db.backends.postgresql",
"NAME": "postgres",
"USER": "postgres",
"PASSWORD": "postgres",
"HOST": "db",
"PORT": 5432,
}
}
```

This configuration specifies the use of the PostgreSQL database with the following parameters:

- Database Name: `postgres`
- User: `postgres`
- Password: `postgres`
- Host: `db`
- Port: `5432`

These settings define the connection details for the default database used by the Django project.

# Dockerizing the Django Project

## Dockerfile

# Dockerfile

```Dockerfile
# Pull base image
FROM python:3.11-alpine

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PORT 8000

# Create and set work directory called `app`
WORKDIR /code

# Install dependencies
COPY requirements.txt .

RUN set -ex && \
    pip install --upgrade pip && \
    pip install -r /code/requirements.txt

# Copy local project
COPY . .

# Expose port 8000
EXPOSE $PORT

# Use gunicorn on port 8000
#CMD ["gunicorn", "--bind", ":8000", "--workers", "2", "django_project.wsgi"]
CMD python manage.py runserver 0.0.0.0:$PORT
```

In this Dockerfile:

- It uses the `python:3.11-alpine` base image.
- Sets environment variables and creates a working directory.
- Installs project dependencies from `requirements.txt`.
- Exposes port 8000.
- Copies the local project into the container.
- Specifies the command to run Django's development server.

## docker-compose.yml

# docker-compose.yml

```yaml
version: "3.9"

services:
  web:
    build:
      context: .
    volumes:
      - .:/code
    ports:
      - 8000:8000
    depends_on:
      - db

  db:
    image: postgres:14
    volumes:
      - ./postgres_data:/var/lib/postgresql/data/
    environment:
      - "POSTGRES_HOST_AUTH_METHOD=trust"

  nginx:
    build:
      context: ./nginx
      dockerfile: Dockerfile
    ports:
      - 80:80
    depends_on:
      - web

volumes:
  postgres_data:
```

This docker-compose.yml file:

- Defines three services: `web` (Django), `db` (PostgreSQL), and `nginx` (Nginx).
- Links services and defines dependencies.
- Maps ports for Django (8000), PostgreSQL, and Nginx (80).
- Uses a volume for persistent PostgreSQL data.

# 2\. Configuring Nginx

## nginx.conf

```nginx
worker_processes 1;

events {
    worker_connections 1024;
}

http {
    sendfile on;
    tcp_nopush on;
    tcp_nodelay on;
    keepalive_timeout 65;
    types_hash_max_size 2048;

    include /etc/nginx/mime.types;
    default_type application/octet-stream;

    server {
        listen 80;
        server_name web;

        location / {
            proxy_pass http://0.0.0.0:8000;
        }
    }
}
```

This Nginx configuration:

- Uses one worker process.
- Defines basic event settings.
- Configures an HTTP server.
- Listens on port 80 for the `web` server.
- Forwards requests to the Django application using the `proxy_pass` directive.

# 3\. Walk-through Explanations

1.  Dockerizing Django:

    - The Dockerfile uses the lightweight Python Alpine image.
    - Sets necessary environment variables and creates a working directory.
    - Installs project dependencies.
    - Exposes port 8000 and specifies the command to run the Django development server.

2.  docker-compose.yml:

    - Defines services for Django (`web`), PostgreSQL (`db`), and Nginx (`nginx`).
    - Establishes dependencies between services.
    - Maps ports and uses volumes for persistent data.

3.  Configuring Nginx:

    - Nginx acts as a reverse proxy, forwarding requests to the Django application.
    - The `proxy_pass` directive directs requests to the `web` service on port 8000.

# 4\. Running the Application

- Run `docker-compose up --build` in the project root.
- Visit `http://localhost:80` in your browser.
