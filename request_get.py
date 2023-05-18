"""This gets the response for given url.
This requires below lib from pypi
requests
How to use:
python request_get.py --url http://api.github.com/repos/kumvijaya/semantic-release-tester/actions/workflows
"""
import requests
import os
import argparse

parser = argparse.ArgumentParser(
    description='Gets the response for the given url'
)
parser.add_argument(
    '-u',
    '--url',
    required=True,
    help='url to fetchg e.g. http://api.github.com/repos/kumvijaya/semantic-release-tester/actions/workflows')

args = parser.parse_args()
url = args.url

username = os.environ["GITHUB_USER"]
token = os.environ["GITHUB_TOKEN"]

def get(url):
    """Invokes get request for given url.
    It requires user and password to connect and fetch the given url.

    Args:
        url (str): url to fetch (Ex: http://api.github.com/repos/kumvijaya/semantic-release-tester/actions/workflows/55073540)

    Returns:
        obj: response object
    """
    session = requests.Session()
    session.auth = (username, token)
    response = session.get(url)
    return response

def post(url, data):
    """Invokes post request for given url.
    It requires user and password to connect and fetch the given url.

    Args:
        url (str): url to fetch (Ex: http://api.github.com/repos/kumvijaya/semantic-release-tester/actions/workflows/55073540)

    Returns:
        obj: response object
    """
    session = requests.Session()
    session.auth = (username, token)
    data = {}
    data['first_name'] = 'vijay'
    data['last_name'] = 'ayy'
    response = session.post(url, data=data)
    return response

# url =  "http://api.github.com/repos/kumvijaya/semantic-release-tester/actions/workflows/55073540"
response = get(url)

if response.status_code == 200:
    out = response.json()
    print(out)
    # print(out['id'])
    # print(out['name'])
else:
    print(f'error in url reponse {response.status_code}')

    
