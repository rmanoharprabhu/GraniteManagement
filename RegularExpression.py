#!/usr/bin/env

import re

def main():
    file = open("google.txt")
    print("Hellow")

    for i in file:
        pathMatch = re.search("(g|G)oogle", i)
        if pathMatch:
            print(pathMatch.group())
        


if __name__ == '__main__':
    main()


