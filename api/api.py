import requests

def get_functions_list():
    response = requests.get("http://134.214.202.235:8000/functions")
    response.raise_for_status()
    data = response.json()
    """
    if isinstance(data, list):
        return data
    elif isinstance(data, dict) and "items" in data:
        return data["items"]
    else:
        return []"""
    print(data)
