#!/usr/bin/python3
# Author: KenjiDoom
import requests

def main():
    #wordlist = input("Enter wordlist: ")
    wordlist = ['list', 'test', 'yikes', 'and', 'okay?']
    for words in wordlist:
        print('www.google.com/' + words)

#if r.status_code == 200:
 #   print("working")
#elif r.status_code == 404:
  #  print('Not found')
#else:
 #   print("I have no clue")
main()

