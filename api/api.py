from config.settings import api_path
import requests

def get_functions_list():
    response = requests.get(f"{api_path}/fonctions")
    response.raise_for_status()
    data = response.json()
    return data

def get_function_detail(name):
    response = requests.get(f"{api_path}/fonctions/{name}")
    response.raise_for_status()
    data = response.json()
    return data

def get_function_status(name):
    response = requests.get(f"{api_path}/fonctions/{name}/etat")
    response.raise_for_status()
    data = response.json()
    return data
