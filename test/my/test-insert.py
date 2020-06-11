# coding: utf-8

import requests
import sys

lc = sys.argv[1]


def insert():
    for i in range(int(lc)):
        insert = requests.post("http://172.20.51.11:40089/press/insert")
        print(insert)
    pass


if __name__ == '__main__':
    insert()
