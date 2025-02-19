# Title : GetSampleMB
# Author: nltt0
# Date: February 19, 2025
# Version: v1.0

from requests import post
from dotenv import load_dotenv
from os import getenv
import argparse
from json import dumps
from random import choices
from string import ascii_lowercase
from string import digits
from os import getcwd
from colorama import init, Fore, Back, Style

init()

class GetSample():
    def __init__(self, tag, limit):
        self.tag = tag
        self.limit = limit

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

    def find_for_tag(self):
        print('0 - Definir variáveis locais')
        capture_values, saves = {}, {}

        headers = {
            'Auth-Key': getenv('AUTH'),
            'User-Agent': 'Chrome/51.0.2704.106 Safari/537.36 OPR/38.0.2220.41'
        }

        url = 'https://mb-api.abuse.ch/api/v1/'

        current_path = getcwd()

        data = {'query': 'get_taginfo',
                'tag': self.tag,
                'limit': self.limit}

        try:
            print('1 - Requisição para o MalwareBaazar')
            req = post(url, data=data, headers=headers)

            if req.status_code == 200:
                saves = req.json()
                print('2 - Laço de repetição para armazenar os valores encontrados')
                for save in saves['data']:
                    file_name = save['file_name']
                    obj = {'file_name': save['file_name'],
                        'file_size': save['file_size'],
                        'file_type': save['file_type'],
                        'signature': save['signature'],
                        'reporter': save['reporter'],
                        'sha256_hash': save['sha256_hash']}
                    
                    capture_values[file_name] = obj
                    
                print(dumps(capture_values, indent=4))
                print('3 - Salvando os valores encontrados e mostrando na tela')
                file_name=self.generate_file_name()
                with open(f'{current_path}/output/{file_name}.json', 'a') as f:
                    f.write(dumps(capture_values, ensure_ascii=False, indent=4))

        except Exception as e:
            print('Error in {}'.format(e))    

def main():
    parser = argparse.ArgumentParser(description="Busca amostras de malware por tag")
    
    parser.add_argument("tag", type=str, help="Nome da tag para busca (exemplo: TrickBot)")
    parser.add_argument("limit", type=int, help="Linhas de busca")

    args = parser.parse_args()

    GetSampleObj = GetSample(args.tag, args.limit)
    GetSampleObj.banner()
    GetSampleObj.find_for_tag()

if __name__ == "__main__":
    main()