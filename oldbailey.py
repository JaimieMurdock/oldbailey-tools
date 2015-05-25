#!/usr/bin/env python
from bs4 import BeautifulSoup
import os, os.path

def parse(filename):
    with open(filename,'rb') as xml_file:
        data = xml_file.read()
    soup = BeautifulSoup(data)
    print filename

def parse_folder(folder):
    for filename in os.listdir(folder):
        parse(os.path.join(folder,filename))

parse_folder('data')
