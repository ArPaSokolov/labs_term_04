import requests

requests_string = "https://belarusbank.by/api/kurs_cards"

response = requests.get(requests_string)

if response:
    print("Все ок:", response.content)
    A = response.json()
    print(type(A))
else:
    print("Что-то пошло не так.")
    print("Код ответа:", response.status_code)
    print("Причина:", response.reason)
