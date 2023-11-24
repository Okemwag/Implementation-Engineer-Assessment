# INTEGRATION PROTOCOLS

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
