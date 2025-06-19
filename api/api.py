import requests

def get_functions_list():
    response = requests.get("http://134.214.202.235:8000/fonctions")
    response.raise_for_status()
    data = response.json()
    return data

def get_function_detail(name):
    response = requests.get(f"http://134.214.202.235:8000/fonctions/{name}")
    response.raise_for_status()
    data = response.json()
    return data

def get_function_status(name):
    response = requests.get(f"http://134.214.202.235:8000/fonctions/{name}/etat")
    response.raise_for_status()
    data = response.json()
    return data
