import random
import requests

def get_dog_facts(number):
    url = f"https://dog-facts-api.herokuapp.com/api/v1/resources/dogs/?number={number}"
    response = requests.get(url)
    return response.json()