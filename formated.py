import requests

def formater(message, CHAD_API_KEY):
    request_json = {
        "message": f'{message}, ТЕБЕ НУЖНО ВЫНЕСТИ ТОЛЬКО ВАЖНОЕ очень коротко в 1 абзац без комментариев',
        "api_key": CHAD_API_KEY
    }

    response = requests.post(url='https://ask.chadgpt.ru/api/public/gpt-4o-mini',
                            json=request_json)
    resp_json = response.json()

    resp_msg = resp_json['response']
    return resp_msg