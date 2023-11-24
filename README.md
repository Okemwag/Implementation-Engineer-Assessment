# HTTP Integration

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
