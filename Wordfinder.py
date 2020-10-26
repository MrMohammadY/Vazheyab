import json
import requests
from config import API_KEY, URL


def create_data(data):
    """
    check a true data and return that
    :param data: json data
    :return: result from vazheyab
    """
    if (len(data['data']['results']) == 0) or (data is None):
        return 'result is not exit please change Database!'
    else:
        for i in range(0, len(data['data']['results'])):
            return data['data']['results'][i]['text']


def send_requests(text, db):
    """
    send a request to vazheyab and create json data
    :param text: text to find in database
    :param db: database name like dehkhoda
    :return: json data to create_data func
    """
    response = requests.get(
        url=URL,
        params={
            'token': API_KEY,
            'q': text,
            'type': 'exact',
            'filter': db,
        }
    )

    if response.status_code == 200:
        data = json.loads(response.text)
    else:
        data = None

    return create_data(data)


