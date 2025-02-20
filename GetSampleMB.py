# Title : GetSampleMB
# Author: nltt0
# Date: February 19, 2025
# Version: v1.0

from requests import post
from argparse import ArgumentParser
from os import getenv
from json import dumps
from random import choices
from string import ascii_lowercase
from string import digits
from os import getcwd
from colorama import init, Fore, Back, Style

init()

class GetSample():
    def __init__(self, limit=2, option=False):
        self.limit = limit
        self.option = option
        

    def generate_file_name(self):
        length = 12
        random_string = ''.join(choices(ascii_lowercase + digits, k=length))
        return random_string
    
    def banner(self):
        var = """

 ▗▄▄▖▗▞▀▚▖   ■   ▗▄▄▖▗▞▀▜▌▄▄▄▄  ▄▄▄▄  █ ▗▞▀▚▖▗▖  ▗▖▗▄▄▖ 
▐▌   ▐▛▀▀▘▗▄▟▙▄▖▐▌   ▝▚▄▟▌█ █ █ █   █ █ ▐▛▀▀▘▐▛▚▞▜▌▐▌ ▐▌
▐▌▝▜▌▝▚▄▄▖  ▐▌   ▝▀▚▖     █   █ █▄▄▄▀ █ ▝▚▄▄▖▐▌  ▐▌▐▛▀▚▖
▝▚▄▞▘       ▐▌  ▗▄▄▞▘           █     █      ▐▌  ▐▌▐▙▄▞▘
            ▐▌                  ▀                       
                                                        
                           v1.0
                         by nltt0                                      


    """
        print(Fore.GREEN + f'{var}')

    def list_for_tag(self, tag):
        print('0 - Define local variables')
        capture_values, saves, data = {}, {}, {}

        headers = {
            'Auth-Key': getenv('AUTH'),
            'User-Agent': 'Chrome/51.0.2704.106 Safari/537.36 OPR/38.0.2220.41'
        }

        url = 'https://mb-api.abuse.ch/api/v1/'

        current_path = getcwd()

        if self.limit > 0:
            data = {'query': 'get_taginfo',
                    'tag': tag,
                    'limit': self.limit}

        try:
            print('1 - Request to MalwareBaazar')
            req = post(url, data=data, headers=headers)

            if req.status_code == 200:
                saves = req.json()
                print('2 - Loop to store the values ​​found')
                for save in saves['data']:
                    file_name = save['file_name']
                    obj = {'file_name': save['file_name'],
                        'file_size': save['file_size'],
                        'file_type': save['file_type'],
                        'signature': save['signature'],
                        'reporter': save['reporter'],
                        'sha256_hash': save['sha256_hash']}
                    
                    capture_values[file_name] = obj
                
                print('3 - Printing the found values')
                print(dumps(capture_values, indent=4))

                if self.option:
                    file_name=self.generate_file_name()
                    print('4 - Downloading the values ​​found in the output folder')
                    with open(f'{current_path}/output/{file_name}.json', 'a') as f:
                        f.write(dumps(capture_values, ensure_ascii=False, indent=4))

        except Exception as e:
            print('Error in {}'.format(e))    

    def list_for_filetype(self, file_type):
        print('0 - Define local variables')
        capture_values, saves, data = {}, {}, {}

        headers = {
            'Auth-Key': getenv('AUTH'),
            'User-Agent': 'Chrome/51.0.2704.106 Safari/537.36 OPR/38.0.2220.41'
        }

        url = 'https://mb-api.abuse.ch/api/v1/'

        current_path = getcwd()

        if self.limit > 0:
            data = {'query': 'get_file_type',
                    'file_type': file_type,
                    'limit': self.limit}

        try:
            print('1 - Request to MalwareBaazar')
            req = post(url, data=data, headers=headers)

            if req.status_code == 200:
                saves = req.json()
                print('2 - Loop to store the values ​​found')
                for save in saves['data']:
                    file_name = save['file_name']
                    obj = {'file_name': save['file_name'],
                        'file_size': save['file_size'],
                        'file_type': save['file_type'],
                        'signature': save['signature'],
                        'reporter': save['reporter'],
                        'sha256_hash': save['sha256_hash']}
                    
                    capture_values[file_name] = obj
                
                print('3 - Printing the found values')
                print(dumps(capture_values, indent=4))

                if self.option:
                    file_name=self.generate_file_name()
                    print('4 - Downloading the values ​​found in the output folder')
                    with open(f'{current_path}/output/{file_name}.json', 'a') as f:
                        f.write(dumps(capture_values, ensure_ascii=False, indent=4))

        except Exception as e:
            print('Error in {}'.format(e))   

    def list_for_hash(self, hash):
            print('0 - Define local variables')
            capture_values, saves, data = {}, {}, {}

            headers = {
                'Auth-Key': getenv('AUTH'),
                'User-Agent': 'Chrome/51.0.2704.106 Safari/537.36 OPR/38.0.2220.41'
            }

            url = 'https://mb-api.abuse.ch/api/v1/'

            current_path = getcwd()

            if self.limit > 0:
                data = {'query': 'get_info',
                        'hash': hash,
                        'limit': self.limit}

            try:
                print('1 - Request to MalwareBaazar')
                req = post(url, data=data, headers=headers)

                if req.status_code == 200:
                    saves = req.json()
                    print('2 - Loop to store the values ​​found')
                    for save in saves['data']:
                        file_name = save['file_name']
                        obj = {'file_name': save['file_name'],
                            'file_size': save['file_size'],
                            'file_type': save['file_type'],
                            'signature': save['signature'],
                            'reporter': save['reporter'],
                            'sha256_hash': save['sha256_hash']}
                        
                        capture_values[file_name] = obj
                    
                    print('3 - Printing the found values')
                    print(dumps(capture_values, indent=4))

                    if self.option:
                        file_name=self.generate_file_name()
                        print('4 - Downloading the values ​​found in the output folder')
                        with open(f'{current_path}/output/{file_name}.json', 'a') as f:
                            f.write(dumps(capture_values, ensure_ascii=False, indent=4))

            except Exception as e:
                print('Error in {}'.format(e))   

def main():
    parser = ArgumentParser(description="Search for samples and download malware")
    
    parser.add_argument("-t", "--tag", type=str, nargs="?", help="If you enable the option, you can search by tag (example: TrickBot)")
    parser.add_argument("-l", "--limit", type=int, default=2, help="Number of search results, default two")
    parser.add_argument("-f", "--file_type", type=str, help="If you enable the option, you can search by file extension")
    parser.add_argument("-ha", "--hash", type=str, help="If you enable the option, you can search by file hash")
    parser.add_argument("-o", "--option", action="store_true", help="Enables downloading of the result in json format")

    args = parser.parse_args()

    GetSampleObj = GetSample(args.limit, args.option)
    GetSampleObj.banner()

    if args.file_type:
        GetSampleObj.list_for_filetype(args.file_type)

    if args.tag:
        GetSampleObj.list_for_tag(args.tag)

    if args.hash:
        GetSampleObj.list_for_hash(args.hash)

if __name__ == "__main__":
    main()
