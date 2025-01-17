import requests
import module4.calculator

response = requests.get('https://google.com')
print(response.text)