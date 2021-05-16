#!/usr/bin/python3
# Author: KenjiDoom
import requests

def main():
    website = input("Enter website: ")
    wordlist = open(input("Enter Wordlist: "), 'r')


    good_code = ['200', '201', '202']
    bad_code = ['400', '401', '403', '404']

    for words in wordlist:
        resp = requests.get(website + words)
        if resp.status_code in good_code:
            print(website + words)
        elif resp.status_code in bad_code:
            print("Not working" + website + words)
        else:
            print("I have no clue")


main()

