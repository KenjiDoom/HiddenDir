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
    parser.add_argument('-u', '--url', type=str, help='Target webiste to be attacked.'.title())
    parser.add_argument('-w', '--wordlist', type=str, help='Wordlist file, must be a .txt file.'.title())
    parser.add_argument('-p', '--proxy', type=str, help='Enable Tor Proxies')
    parser.add_argument('-a', '--agent', type=str, help='Enable random user agent strings'.title())
    return parser.parse_args(args)

def main(args=usr_input()):
    proxies = {
    'http': 'socks5h://localhost:9050',
    'https': 'socks5h://localhost:9050'
    }
    headers = { 'User-Agent': UserAgent().random }

    try:
        website = args.url
        proxy = str(args.proxy).strip().lower()
        agent = str(args.agent).strip().lower()
        wordlist = open(str(args.wordlist), 'r')
    except FileNotFoundError:
        wordlist = open('common.txt', 'r')

    for words in wordlist:
        if proxy.startswith('on'):
            resp = requests.get(str(website) + str(words.strip()), proxies=proxies)
            if resp.status_code == requests.codes.ok:
                print("Successful: " + website + words)
            elif resp.status_code == 404:
                pass

        elif agent.startswith('on'):
            resp = requests.get(str(website) + str(words.strip()), headers=headers)
            if resp.status_code == requests.codes.ok:
                print("Successful: " + website + words)
            elif resp.status_code == 404:
                pass


        elif proxy.startswith('on') and agent.startswith('on'):
            print("working")
            resp = requests.get(str(website) + str(words.strip()), proxies=proxies, headers=headers)
            if resp.status_code == requests.codes.ok:
                print("Successful: " + website + words)
            elif resp.status_code == 404:
                pass

        else:
            resp = requests.get(str(website) + str(words.strip()))
            if resp.status_code == requests.codes.ok:
                print("Successful: " + website + words)
            elif resp.status_code == 404:
                pass


def renew_tor_ip():
    with Controller.from_port(port = 9051) as controller:
        controller.authenticate(password="TEST_PASSWORD") # CHANGE THIS
        controller.signal(Signal.NEWNYM)

if __name__ == '__main__':
    try:
        main()
        renew_tor_ip()
    except requests.exceptions.MissingSchema:
        print('Invalid url or no url provided....'.upper())
    except KeyboardInterrupt:
        print("exiting program.....".upper())
