import requests
from logs import logging

addr = 'http://127.0.0.1'
port = 8000


def search_books(author: str, book: str):
    payload = {'search': f'{author} {book}'}
    try:
        r = requests.get(f'{addr}:{port}', params=payload)
        return r.json()
    except Exception as e:
        logging.critical(f'Searching books failed: {e}')


def get_page(page: int):
    payload = {'page': str(page)}
    r = requests.get(f'{addr}:{port}', params=payload)
    return r.json()
