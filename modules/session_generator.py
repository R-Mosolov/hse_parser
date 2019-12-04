import requests


def run(base_url):
    headers = {'accept': '*/*',
               'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/78.0.3904.97 Safari/537.36'}

    session = requests.session()
    request = session.get(base_url, headers=headers)

    return request
