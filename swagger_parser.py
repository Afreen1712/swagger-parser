# swagger_parser.py
import requests

URL = "https://petstore.swagger.io/v2/swagger.json"  # Swagger JSON

resp = requests.get(URL, timeout=30)
resp.raise_for_status()
data = resp.json()

print("Endpoints:")
for path in data.get("paths", {}).keys():
    print(path)
