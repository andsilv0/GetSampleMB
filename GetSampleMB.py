# Title : GetSampleMB
# Author: nltt0
# Date: February 19, 2025
# Version: v1.0

from requests import post, exceptions
from argparse import ArgumentParser
from os import getenv
from json import dumps
from random import choices
from string import ascii_lowercase
from string import digits
from os import getcwd
from colorama import init, Fore, Back, Style
from os import makedirs,path
from zipfile import ZipFile
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


init()

class GetSample():
    def __init__(self, limit=2, option=False, proxy=False):
        self.proxy = proxy
        self.limit = limit
        self.option = option
        self.url = 'https://mb-api.abuse.ch/api/v1/'
        self.headers = {
            'Auth-Key': getenv('AUTH'),
            'User-Agent': 'Chrome/51.0.2704.106 Safari/537.36 OPR/38.0.2220.41'
        }
        self.current_path = getcwd()

        self.current_path = getcwd()
        self.samples_path = f"{self.current_path}/samples"

        # Criar a pasta samples caso não exista
        if not path.exists(self.samples_path):
            makedirs(self.samples_path)

    def generate_file_name(self):
        return ''.join(choices(ascii_lowercase + digits, k=12))

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

    def send_to_proxy(self, data, proxy_url, target_url):   

        proxies = {
            "http": proxy_url, 
            "https": proxy_url
        }

        req = []

        try:
            req = post(target_url, data=data, headers=self.headers, proxies=proxies, verify=False)
        except exceptions.RequestException as e:
            print(f"Erro ao enviar dados para o proxy: {e}")

        return req

    def search(self, query_type, query_value):
        print('0 - Define local variables')
        capture_values = {}

        query_map = {
            "tag": {"query": "get_taginfo", "param": "tag"},
            "file_type": {"query": "get_file_type", "param": "file_type"},
            "hash": {"query": "get_info", "param": "hash"}
        }

        if query_type not in query_map:
            print(f"Invalid query type: {query_type}")
            return

        data = {"query": query_map[query_type]["query"], query_map[query_type]["param"]: query_value, "limit": self.limit}

        try:
            print(f'1 - Request to MalwareBaazar for {query_type}')

            if (self.proxy):
                req = self.send_to_proxy(data, self.proxy, self.url)
            else:
                req = post(self.url, data=data, headers=self.headers)

            if req.status_code == 200 and "ok" in req.content.decode():
                saves = req.json()
                print('2 - Loop to store the values ​​found')
                for save in saves.get('data', []):
                    file_name = save['file_name']
                    capture_values[file_name] = {
                        'file_name': file_name,
                        'file_size': save['file_size'],
                        'file_type': save['file_type'],
                        'signature': save['signature'],
                        'reporter': save['reporter'],
                        'sha256_hash': save['sha256_hash']
                    }
                
                print('3 - Printing the found values')
                print(dumps(capture_values, indent=4))

                if self.option:
                    file_name = self.generate_file_name()
                    print('4 - Downloading the values ​​found in the output folder')
                    with open(f'{self.current_path}/output/{file_name}.json', 'a') as f:
                        f.write(dumps(capture_values, ensure_ascii=False, indent=4))

        except Exception as e:
            print(f'Error: {e}') 
        
    def download_sample(self, query_type, query_value):
        """
            Download a sample using different query types (hash, tag, file_type)

            ####
            MalwareBazaar runs on Google Cloud infrastructure. Sadly, network egress traffic from Google Cloud is extremely expensive. We therefore had to restrict the number of file downloads on our file download API to 2,000 per IP address/day. For bulk downloads we recommend you to use the hourly and daily file exports of MalwareBazaar served by our datalake:

                MalwareBazaar hourly malware batches (ZIP password: infected)
                MalwareBazaar daily malware batches (ZIP password: infected)

            Should you have valid reasons to download more than 2,000 malware samples through the file download API per day, feel free to reach out to us using the Spamhaus Technology contact form:
            https://www.spamhaus.com/#contact-form
        
        
        """

        query_map = {
            "hash": {"query": "get_file", "param": "sha256_hash"},
            "tag": {"query": "get_taginfo", "param": "tag"},
            "file_type": {"query": "get_file_type", "param": "file_type"}
        }

        if query_type not in query_map:
            print(f"Invalid query type: {query_type}")
            return

        data = {"query": "get_file", query_map[query_type]["query"]:query_value}

        try:
            print(f'1 - Requesting MalwareBaazar for {query_type} sample download')
            req = post(self.url, data=data, headers=self.headers)

            if req.status_code == 200 and "limited" not in req.content.decode('utf-8'):
                file_name = f"{query_value}.zip" if query_type == "hash" else self.generate_file_name() + ".zip"
                file_path = f"{self.current_path}/samples/{file_name}"

                with open(file_path, "wb") as f:
                    f.write(req.content)
                
                print(f"Sample downloaded successfully: {file_path}")

            else:
                print(f"Failed to download sample. {req.content.decode('utf-8')}")

        except Exception as e:
            print(f'Error: {e}')   

  

def main():
    parser = ArgumentParser(description="Search for samples and download malware")

    parser.add_argument("-t", "--tag", type=str, help="Search by tag (example: TrickBot)")
    parser.add_argument("-l", "--limit", type=int, default=2, help="Number of search results, default two")
    parser.add_argument("-p", "--proxy", type=str, help="Proxy URL (example: http://127.0.0.1:8080)")
    parser.add_argument("-f", "--file_type", type=str, help="Search by file extension")
    parser.add_argument("-ha", "--hash", type=str, help="Search by file hash")
    parser.add_argument("-o", "--option", action="store_true", help="Enables downloading of the result in json format")
    parser.add_argument("-d", "--download", action="store_true", help="Download sample for given hash, tag, or file type")

    args = parser.parse_args()

    GetSampleObj = GetSample(args.limit, args.option, args.proxy)
    GetSampleObj.banner()

    if args.download:
        if args.hash:
            GetSampleObj.download_sample("hash", args.hash)
        elif args.tag:
            GetSampleObj.download_sample("tag", args.tag)
        elif args.file_type:
            GetSampleObj.download_sample("file_type", args.file_type)
        else:
            print("No valid parameter provided for sample download.")

    else:
        if args.file_type:
            GetSampleObj.search("file_type", args.file_type)

        if args.tag:
            GetSampleObj.search("tag", args.tag)

        if args.hash:
            GetSampleObj.search("hash", args.hash)

if __name__ == "__main__":
    main()


