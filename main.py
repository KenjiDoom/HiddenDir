#!/usr/bin/python3
# Author: KenjiDoom
import requests
import argparse



def usr_input(args=None):
    parser = argparse.ArgumentParser(description='HiddenDir is a tool used for scanning a websites hidden or active web directories, using brute-froce attack method. This is done by analyzing the HTTP status return codes')
    parser.add_argument('url', type=str, help='Target webiste to be attacked.')
    parser.add_argument('wordlist', type=str, help='Wordlist file, must be a .txt file.')
    parser.add_argument('example', help='python main.py <URL> <WORDLIST> ')
    return parser.parse_args(args)


def main():
    args = usr_input()
    website = args.url
    wordlist = open(args.wordlist,  'r')
    for words in wordlist:
        resp = requests.get(website + words.strip())
        if resp.status_code == requests.codes.ok:
            print("Succ " + website + words)
        elif resp.status_code == 404:
            pass
            #print("Not working " + website + words)



                #website = "http://192.168.1.137/"
                #wordlist = open('common.txt', 'r')
main()
