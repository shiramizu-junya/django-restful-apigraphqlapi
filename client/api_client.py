import requests


class APIClient:
    def __init__(self, base_url: str = "http://localhost:8000"):
        self.base_url = base_url.rstrip("/")

    def get(self, endpoint: str, params: dict = None) -> dict:
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def post(self, endpoint: str, data: dict = None) -> dict:
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        response = requests.post(url, json=data)
        response.raise_for_status()
        return response.json()

    def put(self, endpoint: str, data: dict = None) -> dict:
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        response = requests.put(url, json=data)
        response.raise_for_status()
        return response.json()

    def delete(self, endpoint: str) -> dict:
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        response = requests.delete(url)
        response.raise_for_status()
        return response.json()


if __name__ == "__main__":
    client = APIClient()

    # GET /api/
    result = client.get("/api/")
    print(result)
