import requests
import json
import numpy as np
import sys

url = "http://127.0.0.1:5000/sum"
headers = {"Content-Type":"application/json"}

def get_info(array):
    data = {"array":array}   
    data = json.dumps(data)
    r = requests.post(url, headers=headers,data = data)
    r_dict = r.json()
    return r_dict["result"]


if __name__ == "__main__":
    array = [1.0001,2.0001,3.0001]
    r = get_info(array)
    print(r)
