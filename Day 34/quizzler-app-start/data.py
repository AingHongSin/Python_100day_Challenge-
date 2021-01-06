import requests

parameter = {
    "amount": 10,
    "type": 'boolean'
}

respones = requests.get(url='https://opentdb.com/api.php', params=parameter)
respones.raise_for_status()
data = respones.json()

question_data = data['results']


