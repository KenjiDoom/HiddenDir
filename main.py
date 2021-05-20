#!/usr/bin/python3
# Author: KenjiDoom
import requests
import argparse



def usr_input(args=None):
    parser = argparse.ArgumentParser(description='HiddenDir is a tool used for scanning a websites hidden or active web directories, using brute-froce attack method. This is done by analyzing the HTTP status return codes')
    parser.add_argument('--url', type=str, help='Target webiste to be attacked.')
    parser.add_argument('--wordlist', type=str, help='Wordlist file, must be a .txt file.')
    return parser.parse_args(args)


def main(args=usr_input()):
    try:
        website = args.url
        wordlist = open(str(args.wordlist), 'r')
    except FileNotFoundError:
        print("No wordlist was specified using defualt wordlist.")
        wordlist = open('common.txt', 'r')

    for words in wordlist:
        resp = requests.get(str(website) + str(words.strip()))
        if resp.status_code == requests.codes.ok:
            print("Successful: " + website + words)
        elif resp.status_code == 404:
            pass


main()
