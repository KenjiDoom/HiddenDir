#!/usr/bin/python3
# Author: KenjiDoom
import requests

def main():
    website = input("Enter website: ")
    wordlist = input("Enter Wordlist: ")


    good_code = ['200', '201', '202']
    bad_code = ['400', '401', '403', '404']

    for words in wordlist:
        resp = requests.get(website + words)
        if resp.status_code == 200:
            print(website + words)
        elif resp.status_code == 404:
            print("Not working" + website + words)
        else:
            print("I have no clue")


main()

