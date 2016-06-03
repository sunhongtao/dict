#-*-encoding:utf-8-*-
'''
Created on 2016年6月2日

@author: 1811
@contact: QQ:782666126
@version: 1.0
'''
from bs4 import BeautifulSoup
import urllib2
import re

BASEURL = "http://www.iciba.com/"


def exact_translate(word, example=False):
    '''
    @
    use the beautifulSoup to analysis the Html page
    @param cx: the part of speech of the word
    @param cc: the result of the word
    '''
    try:
        site = BASEURL + word
        url = urllib2.urlopen(site)
        soup = BeautifulSoup(url, "lxml")
        rs = soup.find_all(class_="base-list switch_part")
        s = rs[0].findAll("li")
        for t in s:
            cx = t.findAll("span", {"class": 'prop'})
            cc = t.findAll("p")
            print cx[0].contents[0]," ".join(cc[0].contents[0].split())
    except:
        word_1 = deal_word(word, example=True)
        print "You may want to find:" + word_1
        trans(word_1)

def deal_word(word):
    '''
    @attention: just to deal the word.such as "word 1"->"word","wo rd"->"word" or "中 国"->"中国"
    '''
    word = word.strip()
    word_1 = re.sub("[A-Za-z0-9\[\`\ \\~\!\@\#\$\^\&\*\(\)\=\|\{\}\'\:\;\'\,\[\]\.\<\>\/\?\~\！\@\#\\\&\*\%]", "", word)
    if word_1.strip():
        return word_1
    else:
        return "".join([ch for ch in word if ch.isalpha()])
    
def fuzzy_search(word):
    try:
        site = BASEURL + word
        url = urllib2.urlopen(site)
        soup = BeautifulSoup(url, "lxml")
        rs = soup.find_all(class_="base-list switch_part")
        s = rs[0].findAll("li")
        for t in s:
            cx = t.findAll("span", {"class": 'prop'})
            cc = t.findAll("p")
            yield cx[0].contents[0], " ".join(cc[0].contents[0].split())         
    except:
        word_1 = deal_word(word)
        print "You may want to find:" + word_1
        trans(word_1)

def is_chinese(uchar): 
    """判断一个unicode是否是汉字 """
    if  uchar >= u'\u4e00' and uchar<=u'\u9fa5': 
        return  True
    else:
        return  False
    
def trans(word,example=False):
    if example:
        "如果example为真，查询全局,精确翻译"
        exact_translate(word)
    else:
        for i in fuzzy_search(word):
            for d in i:
                print d,
            print "\n"
