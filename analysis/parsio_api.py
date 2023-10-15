import json
from pprint import pprint
from time import sleep

import requests
from requests import Response

BASE_URL = 'https://api.parsio.io'

API_KEY = '7u0dyg18o72i0nrzymvcjqkti6vuodd9yenrff7f2ph894oa'
headers = {"X-API-Key": API_KEY}


def _upload(filename: str) -> str:
    MAILBOX_ID = '652929aae1999a000e3486c3'

    url = BASE_URL + f"/mailboxes/{MAILBOX_ID}/upload"

    with open(filename, 'rb') as f:
        files = {'file': f}
        with requests.request("POST", url, files=files, headers=headers) as response:
            print('response: ', response)
            doc_id = response.text
            print('doc_id', type(doc_id), f"*{doc_id}*")
            doc_id = doc_id.replace('"', '')

    return doc_id


def _get_parsed(doc_id: str):
    url = BASE_URL + f'/docs/{doc_id}'
    response: Response = requests.get(url, headers=headers)
    data = json.loads(response.text)

    if data['parsed']:
        return data['parsed']

    sleep(1)
    return _get_parsed(doc_id)


GENERAL_TABLE_NAME = 'Table 1'
TESTS_TABLE_NAME = 'Table 2'


def _extract_data(data: dict) -> list[dict]:
    general_table, tests_table = None, None

    for item in data:
        if item['name'] == GENERAL_TABLE_NAME:
            general_table = item['value']
        elif item['name'] == TESTS_TABLE_NAME:
            tests_table = item['value']

    pprint(general_table)
    print('\n\n')
    pprint(tests_table)

    rows = []
    for row in tests_table:
        obj = {}
        for item in row:
            obj[item['name']] = item['value']

        rows.append(obj)

    pprint(rows)
    return rows


def parse_pdf(filename: str):
    doc_id = _upload(filename)
    sleep(2)
    data = _get_parsed(doc_id)

    pprint(data)
    print('\n\n\n')

    return _extract_data(data)


