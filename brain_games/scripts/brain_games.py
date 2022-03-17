#!/usr/bin/env python3
import sys
sys.path.append('/home/egortrod/python-project-lvl1/brain_games')
from cli import welcome_user

# from brain_games.cli import welcome_user

def main():
    print ('Welcome to the Brain Games!')
    welcome_user()

if __name__ == '__main__':
    main()