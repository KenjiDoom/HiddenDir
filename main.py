#!/usr/bin/python3
# Author: KenjiDoom
from stem import Signal
from stem.control import Controller
from fake_useragent import UserAgent
import requests
import argparse
import sys

def usr_input(args=None):
    parser = argparse.ArgumentParser(description='HiddenDir is a tool used for scanning a websites hidden or active web directories, using brute-froce attack method. This is done by analyzing the HTTP status return codes')
    parser.add_argument('-u', '--url', type=str, help='Target webiste to be attacked.')
    parser.add_argument('-w', '--wordlist', type=str, help='Wordlist file, must be a .txt file.')
    parser.add_argument('-p', '--proxy', type=str, help='Enable Tor Proxies')
    return parser.parse_args(args)

def main(args=usr_input()): # Main function with no Proxies or headers

    try:
        website = args.url
        wordlist = open(str(args.wordlist), 'r')
    except FileNotFoundError:
        wordlist = open('common.txt', 'r')

    for words in wordlist:
        resp = requests.get(str(website) + str(words.strip()))
        if resp.status_code == requests.codes.ok:
            print("Successful: " + website + words)
        elif resp.status_code == 404:
            pass

def handle_proxy(args=usr_input()):
    # All Proxy Functions
    proxies = {
    'http': 'socks5h://localhost:9050',
    'https': 'socks5h://localhost:9050'
    }
    #r = requests.get(website, proxies=proxies) # Test if proxy works
    #print(r.content)
    try:
        website = args.url
        wordlist = open(str(args.wordlist), 'r')
    except FileNotFoundError:
        wordlist = open('common.txt', 'r')

    for words in wordlist:
        content = requests.get(str(website) + str(words.strip()), proxies=proxies)
        if content.status_code == requests.codes.ok:
            print("Successful: " + website + words)
            #print(content.content)
        elif content.status_code == 404:
            pass


def renew_tor_ip():
    with Controller.from_port(port = 9051) as controller:
        controller.authenticate(password="TEST_PASSWORD")
        controller.signal(Signal.NEWNYM)


def options(args=usr_input()):
    if args.proxy == 'on':
        handle_proxy()
    else:
        main()


options()
renew_tor_ip()
