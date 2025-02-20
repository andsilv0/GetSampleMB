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

usage: GetSampleMB.py [-h] [-l LIMIT] [-o] tag

Busca amostras de malware por tag

positional arguments:
  tag                   Nome da tag para busca (exemplo: TrickBot)

options:
  -h, --help            show this help message and exit
  -l LIMIT, --limit LIMIT
                        Linhas de busca
  -o, --option          Habilita o download do resultado em formato json

```

## Example

`python GetSampleMB.py TrickBot -l 1`


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