# 1.INTEGRATION PROTOCOLS

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

# DATA STREAMING APPLICATION

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
