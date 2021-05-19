#!/usr/bin/python3
# Author: KenjiDoom
import requests

def main():
    website = "http://192.168.1.137/"
    wordlist = open('common.txt', 'r')

    for words in wordlist:
        resp = requests.get(website + words.strip())
        if resp.status_code == requests.codes.ok:
            print("Succ " + website + words)
        elif resp.status_code == 404:
            pass
            #print("Not working " + website + words)

main()
