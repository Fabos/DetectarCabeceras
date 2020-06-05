#!/usr/bin/env python
#_*_ coding: utf8 _*_

import requests
import argparse

parser =argparse.ArgumentParser(description="Script para detectar cabeceras")
parser.add_argument('-o', '--objetivo', help='URL o IP objetivo')
parser =parser.parse_args()

def main():
    if parser.objetivo:
        try:
            url = requests.get(url=parser.objetivo)
            cabeceras = dict(url.headers)
            for x in cabeceras:
                print(x + " : " + cabeceras[x])
        except:
            print("No se pudo conectar")

    else:
        print("No hay objetivo")

if __name__ == '__main__':
    main()