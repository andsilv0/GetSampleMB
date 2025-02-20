# GetSampleMB

![](GetSampleMB.png)

## Usage

```
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
