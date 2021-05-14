#!/usr/bin/python3
# Author: KenjiDoom
import requests

def main():
    website = input("Enter website: ")
    wordlist = ['list', 'test', 'yikes', 'and', 'okay?']
    for words in wordlist:
        resp = requests.get(website + words)
        if resp.status_code == 200:
            print("+" + resp + ":200")
        elif resp.status_code == 404:
            print("Not working")
        else:
            print("I have no clue")


main()

