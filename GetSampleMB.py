from requests import post
from dotenv import load_dotenv
from os import getenv


class GetSample():
    def __init__(self, tag):
        self.tag = tag

    def find_for_tag(self):

        saves = {}

        headers = {
            'Auth-Key': getenv('AUTH'),
            'User-Agent': 'Chrome/51.0.2704.106 Safari/537.36 OPR/38.0.2220.41'
        }

        url = 'https://mb-api.abuse.ch/api/v1/'

        data = {'query': 'get_taginfo',
                'tag': self.tag,
                'limit': 2}

        req = post(url, data=data, headers=headers)

        if req.status_code == 200:
            
            saves = req.json()

            for save in saves['data']:
                print('{},{},{},{},{},{}'.format(save['file_name'], save['file_size'], 
                                                 save['file_type'], save['signature'],
                                                 save['reporter'], save['sha256_hash']))
        

GetSampleObj = GetSample('TrickBot')
GetSampleObj.find_for_tag()