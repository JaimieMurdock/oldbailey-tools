#!/usr/bin/env python
from bs4 import BeautifulSoup
from collections import Counter
import os, os.path



def parse(filename):
    with open(filename,'rb') as xml_file:
        data = xml_file.read()
    soup = BeautifulSoup(data)
    formatted = ""
    # { defendants }, { charges }, { verdict }
    
    # ---------- Defendants
    defendants = []
    for defendant in soup.find_all(type='defendantName'):
        defandantText = defendant.find(type='surname')['value'] + ", " + defendant.find(type='given')['value']
        # Insert politically corrent other answers
        defendants.append(defandantText);
    formatted += '; '.join(defendants)
    
    formatted += " - "
    # ---------- Offenses
    offenses = []
    for charge in soup.find_all(type="offenceDescription"):
        offenseText = charge.find(type='offenceCategory')['value']
        if charge.find(type='offenceSubcategory'):
            offenseText += " > " + charge.find(type='offenceSubcategory')['value']
        offenses.append(offenseText)
        
    formatted += count_offenses(offenses)
    
    for verdict in soup.find_all(type='verdictDescription'):
        verdictText = verdict.find(type='verdictCategory')['value']
        
    formatted += ' - ' + verdictText
    print formatted
    
def count_offenses(offenses):
    cnt = Counter()
    counted_string = "";
    for offense in offenses:
        cnt[offense] += 1
    
    for offense, count in cnt.iteritems():
        if count > 1:
            counted_string += offense + " (x{0})".format(count)
        else:
            counted_string += offense
    return counted_string

def parse_folder(folder):
    for filename in os.listdir(folder):
        parse(os.path.join(folder,filename))

parse_folder('data')
