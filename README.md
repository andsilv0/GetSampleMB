# GetSampleMB

![](GetSampleMB.png)

## Usage

```
---

[0] - Create auth_key -> https://auth.abuse.ch/

[00] - Create file .env with variable in current directory 

[1] - Example:
  AUTH='69d00b49efaffec4821af2e72039803b575d4c26c7e11b1e1f1dc59c6ee926cf'

--------

usage: GetSampleMB.py [-h] [-t [TAG]] [-l LIMIT] [-f FILE_TYPE] [-ha HASH] [-o]

Busca amostras e faz download de malware

options:
  -h, --help            show this help message and exit
  -t [TAG], --tag [TAG]
                        Se ativa a opção, é possível pesquisar por tag (exemplo: TrickBot)
  -l LIMIT, --limit LIMIT
                        Quantidade de linhas para a consulta, padrão 2
  -f FILE_TYPE, --file_type FILE_TYPE
                        Se ativa a opção, é possível pesquisar por extensão do arquivo
  -ha HASH, --hash HASH
                        Se ativa a opção, é possível pesquisar por hash do arquivo
  -o, --option          Habilita o download do resultado em formato json

```

## Example

### Pesquisar por tag 
`python GetSampleMB.py -t TrickBot`

### Pesquisar por extensão de arquivo 
`python GetSampleMB.py -f exe`

### Pesquisar por hash 
`python GetSampleMB.py -ha 7de2c1bf58bce09eecc70476747d88a26163c3d6bb1d85235c24a558d1f16754`


## Limitations 

```
Download limit on the file download API

MalwareBazaar runs on Google Cloud infrastructure. Sadly, network egress traffic from Google Cloud is extremely expensive. We therefore had to restrict the number of file downloads on our file download API to 2,000 per IP address/day. For bulk downloads we recommend you to use the hourly and daily file exports of MalwareBazaar served by our datalake:

    MalwareBazaar hourly malware batches (ZIP password: infected)
    MalwareBazaar daily malware batches (ZIP password: infected)

Should you have valid reasons to download more than 2,000 malware samples through the file download API per day, feel free to reach out to us using the Spamhaus Technology contact form:
https://www.spamhaus.com/#contact-form

https://bazaar.abuse.ch/faq/#api-limit

```