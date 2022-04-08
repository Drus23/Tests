import requests

def get_users(url):
    response = requests.get(url)
    return response


def post_user(url, name, job):
    response = requests.post(url, data={'name': name, 'job': job})
    return response
