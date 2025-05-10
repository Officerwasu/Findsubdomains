#!/usr/bin/env python3
import requests
import sys

def request(url):
    try:
        response = requests.get("http://" + url)
        if response.status_code == 200:
            return response
        else:
            return None
    except requests.exceptions.ConnectionError:
        return None
    except requests.exceptions.RequestException:
        return None

if len(sys.argv) != 3:
    print("Usage: python subdomain_scanner.py <target_url> <wordlist_file>")
    sys.exit(1)

target_url = sys.argv[1]
wordlist_file_path = sys.argv[2]

try:
    with open(wordlist_file_path, "r") as wordlist_file:
        for line in wordlist_file:
            word = line.strip()
            test_url = word + "." + target_url
            response = request(test_url)
            if response:
                print("[+] Discovered subdomain --> " + test_url)
except FileNotFoundError:
    print(f"Error: Wordlist file not found at {wordlist_file_path}")
    sys.exit(1)
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    sys.exit(1)
