#!/usr/bin/python3
""" Simple module """
import requests


def main():
    """fetches https://intranet.hbtn.io/status"""
    r = requests.get('https://intranet.hbtn.io/status')
    html = r.text
    print("Body response:")
    print("\t- type:", type(html))
    print("\t- content:", html)

if __name__ == "__main__":
    main()
