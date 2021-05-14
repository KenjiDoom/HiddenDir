#!/usr/bin/python3
# Author: KenjiDoom
import requests

def main():
    website = input("Enter website: ")
    wordlist = ['admin', 'snot', 'backup', 'docs', 'include', 'styles']
    for words in wordlist:
        resp = requests.get(website + words)
        if resp.status_code == 200:
            print(website + words)
        elif resp.status_code == 404:
            print("Not working" + website + words)
        else:
            print("I have no clue")


main()

