# HiddenDir
HiddenDir is a tool used for scanning a websites hidden or active web directories, using brute-froce attack method.
This is done by analyzing the HTTP status return codes. Inspiration comes from dirb scanner.


## Installation
1. First clone the repo
```
git clone https://github.com/KenjiDoom/HiddenDir.git
```
2. Install tor, Arch & Ubuntu
```
sudo apt-get install tor
sudo pacman -S tor
```
3. Install python packages
```
pip install -r requirements.txt
```
4. [Setup Tor](https://github.com/KenjiDoom/StealthProbes#4th-step-is-to-copy-the-hash-into-the-torrc-file)


### Usage Examples
```
$ python HideDir.py --help
usage: HideDir.py [-h] [-u URL] [-w WORDLIST] [-p PROXY] [-a AGENT]

HiddenDir is a tool used for scanning a websites hidden or active web directories, using brute-froce attack method. This is done by analyzing the
HTTP status return codes

optional arguments:
  -h, --help            show this help message and exit
  -u URL, --url URL     Target Webiste To Be Attacked.
  -w WORDLIST, --wordlist WORDLIST
                        Wordlist File, Must Be A .Txt File.
  -p PROXY, --proxy PROXY
                        Enable Tor Proxies
  -a AGENT, --agent AGENT
                        Enable Random User Agent Strings

```
1. Scan TARGET with custom wordlist
```
python -u http://scanexample.com/ -w common.txt
```
2. Scan TARGET with Random User-Agents Enabled
```
python -u http://scanexample.com/ -w common.txt -a on
```
3. Scan TARGET with Tor Proxies Enabled
```
python -u http://scanexample.com/ -w common.txt -p on
```
4. Scan TARGET with Random UserAgent & Tor Peoxies Enabled
```
python -u http://scanexample.com/ -w common.txt -p on -a on
```

### TO-DO
- [x] - Args user input
- [x] - Tor Proxies
- [x] - Random User-Agents
- [] - Save output to file
