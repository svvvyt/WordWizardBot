import requests
import json
import random

from assets.words_100 import words

# https://dictionary.yandex.net/api/v1/dicservice.json/lookup?key=dict.1.1.20240110T134658Z.42bf471f4889a06f.663f79b97e4b477f78483d9a1f0c6ba0b2156ac2&lang=en-ru&text=OUR_QUERY

randomInt = random.randint(0, len(words))

response = requests.get(
    f'https://dictionary.yandex.net/api/v1/dicservice.json/lookup?key=dict.1.1.20240110T134658Z.42bf471f4889a06f.663f79b97e4b477f78483d9a1f0c6ba0b2156ac2&lang=en-ru&text={words[randomInt]}')
json_content = json.loads(response.text)

try:
    word = json_content['def'][0]['text']
except:
    response = requests.get(
        f'https://dictionary.yandex.net/api/v1/dicservice.json/lookup?key=dict.1.1.20240110T134658Z.42bf471f4889a06f.663f79b97e4b477f78483d9a1f0c6ba0b2156ac2&lang=en-ru&text={words[randomInt]}')
    word = json_content['def'][0]['text']

# транскрипция
try:
    transcription = json_content['def'][0]['ts']
except:
    transcription = ''

# синонимы
try:
    synonyms = [synonym['text'] for synonym in json_content['def'][0]['tr'][0]['syn']]
except:
    synonyms = []

# примеры употребления
try:
    examples_eng = [example['text'] for example in json_content['def'][0]['tr'][0]['ex']]
    examples_rus = [item['tr'][0]['text'] for item in json_content.get('def', [])[0].get('tr', [])[0].get('ex', [])]
    dict_eng_rus = {eng: rus for rus, eng in zip(examples_rus, examples_eng)}
except:
    examples_eng, examples_rus, dict_eng_rus = [], [], []


def get_word():
    randomInt = random.randint(0, len(words))

    response = requests.get(
        f'https://dictionary.yandex.net/api/v1/dicservice.json/lookup?key=dict.1.1.20240110T134658Z.42bf471f4889a06f.663f79b97e4b477f78483d9a1f0c6ba0b2156ac2&lang=en-ru&text={words[randomInt]}')
    json_content = json.loads(response.text)

    try:
        word = json_content['def'][0]['text']
    except:
        response = requests.get(
            f'https://dictionary.yandex.net/api/v1/dicservice.json/lookup?key=dict.1.1.20240110T134658Z.42bf471f4889a06f.663f79b97e4b477f78483d9a1f0c6ba0b2156ac2&lang=en-ru&text={words[randomInt]}')
        word = json.loads(response.text)['def'][0]['text']

    return word

print(get_word())

# with open('./assets/100_words.txt', 'r') as file:
#   lines = [line.strip() for line in file]
