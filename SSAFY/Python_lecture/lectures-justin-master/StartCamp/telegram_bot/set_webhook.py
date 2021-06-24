import requests

token = '805457410:AAGhgJeP4X79yj8TKWsrr_shUYbvjMWEZUo'
app_url = f'https://api.telegram.org/bot{token}'
ngrok_url = 'https://6c3acaf0.ngrok.io'
python_anywhere_url = 'https://edujustin.pythonanywhere.com'
set_webhook_url = f'{app_url}/setWebhook?url={python_anywhere_url}/telegram'

response = requests.get(set_webhook_url)
print(response.text)
