import json 
import requests

from common._secrets import AIDEVS_KEY

BASE_URL = "https://zadania.aidevs.pl/"

def get_token_and_task(task: str) -> str:
    data = {"apikey": AIDEVS_KEY}

    resp = requests.post(f"{BASE_URL}/token/{task}", data=json.dumps(data))
    resp.raise_for_status()

    token = json.loads(resp.text)["token"]

    resp = requests.get(f"{BASE_URL}/task/{token}")

    return token, json.loads(resp.text)

def send_answer(token: str, answer: str) -> str:
    resp = requests.post(
        f"{BASE_URL}/answer/{token}", data=json.dumps({"answer": answer})
    )

    return resp.text