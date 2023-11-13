import requests
import json

from common._secrets import OPENAI_KEY  # pylint: disable=import-error


BASE_URL = "https://api.openai.com/v1/{endpoint}"

HEADER = {
    "Authorization": f"Bearer {OPENAI_KEY}",
}


def make_request(
    endpoint: str, data: dict = None, files: dict = None, header: dict = HEADER
):
    if not files:
        header["Content-Type"] = "application/json"
        resp = requests.post(
            BASE_URL.format(endpoint=endpoint), headers=header, data=json.dumps(data)
        )
    else:
        resp = requests.post(
            BASE_URL.format(endpoint=endpoint), headers=header, data=data, files=files
        )
    return json.loads(resp.text)


def send_chat_completion(
    model_version: str,
    system_content: str,
    user_content: str,
    temperature: float = 0,
):
    return make_request(
        endpoint="chat/completions",
        data={
            "model": model_version,
            "messages": [
                {"role": "system", "content": system_content},
                {"role": "user", "content": user_content},
            ],
            "temperature": temperature,
        },
    )
