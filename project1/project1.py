import pandas as pd
import numpy as np
from typing import List, Dict, Any
import nltk
from nltk.corpus import state_union

import re
from nltk.tokenize import PunktSentenceTokenizer
import os
import glob
import io
from nltk.corpus import wordnet

def readFile(filename):

    # Load in a text file
    file = open(filename,'r')
    text_file = file.read()

    return text_file


def read_textfiles_from_directory(directory, file_regexp):

    #print(directory, file_regexp)
    # Get all of the file names
    files = sorted(os.listdir(directory))

    file_name1 = [f for f in files if re.search(file_regexp, f)]
    # Construct a list of text from those that match the regexp
    list_of_textfiles1 = [readFile(directory + "/" + f) for f in files if re.search(file_regexp, f) ]

    directory = directory + "/otherfiles1/"
    files = sorted(os.listdir(directory))

    list_of_textfiles2 = [readFile(directory  + f) for f in files if re.search(file_regexp, f) ]
    file_name2 = [f for f in files if re.search(file_regexp, f)]

    list_of_textfiles = list_of_textfiles1 + list_of_textfiles2
    file_name = file_name1+file_name2
    return (file_name,list_of_textfiles)


def WriteFile(filename):
    train_text = state_union.raw("2003-GWBush.txt")
    with open(fileName, 'w') as f:
        f.write(train_text)


def names(text):
    tokens = nltk.tokenize.word_tokenize(text)
    pos = nltk.pos_tag(tokens)
    sentt = nltk.ne_chunk(pos)
    personlist = []
    person = []
    name = ""
    for subtree in sentt.subtrees(filter=lambda t: t.label() == 'PERSON'):
        for leaf in subtree.leaves():
            person.append(leaf[0])
        if len(person) > 1: 
            for part in person:
                name += part + ' '
            if name[:-1] not in personlist:
                personlist.append(name[:-1])
            name = ''
        else :
            personlist.append(person[0])            
        person = []
    return (personlist)
  

def getlocation(text):
    tokens = nltk.tokenize.word_tokenize(text)
    pos = nltk.pos_tag(tokens)
    sentt = nltk.ne_chunk(pos)
    place_list = []
    place = []
    name = ""
    for subtree in sentt.subtrees(filter=lambda t: t.label() == 'GPE'):
        for leaf in subtree.leaves():
            place.append(leaf[0])
        if len(place) > 1:
            for part in place:
                name += part + ' '
            if name[:-1] not in place_list:
                place_list.append(name[:-1])
            name = ''
        else :
            place_list.append(place[0])
        place = []
    return (place_list)


# Extracting Date:
def date(text):
    list1 = re.findall(r'\d{1,4}.\d{1,2}.\d{1,4}|\d{1,2}?[ \t.-]*[A-Za-z]+[ \t.-]* \d{1,4}|\w{3,9}[ \t.-]*\d{1,2}[ \t.-]*\d{1,4}|\w{3,9}[ \t.-]*\d{1,4}',text)
    return(list1)



# phone numbers
def number(text):
    pattern = r'[+]?\d{0,2}[ .-]?\(?\d{3,4}\)?[ .-]\d{3,4}[ .-]\d{4}|\d{10}'
    list2 = re.findall(pattern,text)
    return list2

# Genders
def genders(text):
    pattern = r' [hH]e | [Ss]he | [Hh]is | [Hh]er | [Hh]im | [Hh]imself | [Hh]erself | [Hh]ers | [sS]on | [Dd]addy| mom| dad| brother| sister| mommy | man| men| wom[ae]n'
    list3 = re.findall(pattern,text)
    return list3

#address :
def address(text):
    pattern = r'[0-9]{2,4} [A-Za-z]+ [A-Za-z.\n]{2,}[ A-Za-z,.\n]{4,} [0-9]{5,6}|#?[0-9-/]{6,9} [A-Za-z\n]+ [A-Za-z.\n]{2,55}[ A-Za-z,.]{4,55} [0-9]{5,6}'
    list4 = re.findall(pattern,text)
    return list4


# Concepts:
def concepts(text,concept):
    SentenceList = nltk.tokenize.line_tokenize(ls[0])
    list5=[]
    synaset = wordnet.synsets(concept)
    meanings= []
    for i in range(len(synaset)):
        meanings.append(synaset[i].lemmas()[0].name())
    for line in range(len(SentenceList)):
        for i in range(len(meanings)):
            if meanings[i] in SentenceList[line]:
                list5.append(SentenceList[line])
    return list5


#Redation
def redaction(file,concept):
    text=file
    j=0
    #Frequency_of_fields = [len(names(text)),len(getlocation(text)),len(date(text)),len(number(text)),len(genders(text)),len(address(text)),len(concepts(text,concept)])
    lists = names(text)+getlocation(text)+date(text)+number(text)+genders(text)+address(text)+concepts(text,concept)
    for i in range(len(lists)):
        j=j+1
        pattern = lists[i]
        text = re.sub(lists[i],u'\u2588'*len(lists[i]),text)
    return Frequency_of_fields,text


def store_redactedfiles(redacted_file):
    file_pattern = ".redacted"
    file_redc_name=[]
    j=0
    for i in range(len(redacted_file)):
        file_redc_name.append(Directory + '/Redactedfiles/' + re.sub('.txt','.redacted',filename[i]))


    for i in range(len(file_redc_name)):
        with io.open(file_redc_name[i], 'w',encoding="utf-8") as f:
            f.write(redacted_file[i])


def redation_summary(text,concept):
    Frequency_of_fields = [len(names(text)),len(date(text)),len(number(text)),len(genders(text)),len(address(text)),len(concepts(text,concept))]

    return Frequency_of_fields



def Writing_statistics(stats,file, filename):
    text = """Statistics:
       File_name  name  date  phone  gender  address  concepts
    """
    for i in range(len(stats)):
        text = text + '\n' + filename[i] + '  -  ' + str(stats[i][0])+ '     ' + str(stats[i][1])+  '     ' +str(stats[i][2])+  '     ' + str(stats[i][3])+  '      ' + str(stats[i][4]) +  '      ' + str(stats[i][5])+ '\n'

    with open(file, 'w') as f:
        f.write(text)




