import requests

# Swagger JSON ka URL
URL = "https://petstore.swagger.io/v2/swagger.json"

resp = requests.get(URL, timeout=30)
resp.raise_for_status()
data = resp.json()

# File open karo write mode me
with open("endpoints.txt", "w") as f:
    f.write("Endpoints with methods:\n")
    for path, methods in data.get("paths", {}).items():
        for method in methods.keys():
            line = f"{method.upper()} {path}\n"
            f.write(line)

print("✅ Endpoints documentation 'endpoints.txt' file me save ho gaya hai.")
