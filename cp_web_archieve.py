# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 15:07:52 2017

@author: srayamajhi
"""
import re,xlsxwriter
import pandas as pd
import datetime
from optparse import OptionParser
from bs4 import BeautifulSoup as bs
import requests, sys, json,os
from selenium import webdriver
driver = webdriver.PhantomJS()
from googletrans import Translator
translator = Translator()
import random

class historical_website_discount():
    links = []
    def __init__(self):
        pass

    def parserOption(self):
        parser = OptionParser()
        parser.add_option("-y", "--year", dest="year",
                          help='-y year',
                          metavar="FILE")
        parser.add_option("-m", "--month", dest="month",
                          help='-m month',
                          metavar="FILE")
        parser.add_option("-d", "--day", dest="day",
                          help='-d day',
                          metavar="FILE")
        (options, args) = parser.parse_args()

        return options, args

    def read_excel(self):
        df = pd.read_excel(self.file, sheet="FSD")
        print(df.head())
        return

    def scraper(self, url,country):
        session = requests.Session()
        response = session.get(url)
        soup = bs(response.content, 'html.parser')
        list1 = []
        list2=[]
        index1=[]
        index2 =[]
        list3 = []
        list4 = []
        if country=='US':
            class1="banner-headline"
            class2 ="teaser-headline"
        elif country=='UK':
            class1="banner-text-content"
            class2 = "text-container"
        elif country=='China':
            class1="banner-text-content"
            class2 = "text-container"
        elif country=='Germany':
            #print("class germany",country)
            class1="banner-headline"
            class2 = "teaser-headline"
        ####

        for data in soup.find_all('div', {"class": class1}):
            if country=='Germany':
                #print("case germany")
                if not (re.search("OFF|[0-9]|SALE", translator.translate(data.text).text.replace("DISCOUNT","OFF"))== None):
                    list1.append(translator.translate(data.text).text.replace("DISCOUNT","OFF"))
            else:
                if not (re.search("OFF|[0-9]|SALE",data.text)==None):
                    list1.append(data.text)

        for data in soup.find_all('div', {"class": class2}):
            if country=='Germany':
                #print("case germany")
                if not (re.search("OFF|[0-9]|SALE", translator.translate(data.text).text.replace("DISCOUNT","OFF")) == None):
                    list2.append(translator.translate(data.text).text.replace("DISCOUNT","OFF"))
            else:
                if not (re.search("OFF|[0-9]|SALE",data.text)==None):
                    list2.append(data.text)

        ### Remove duplicates
        for i in list1:
            if i not in list3:
                list3.append(i)
        for i in list2:
            if i not in list4:
                list4.append(i)

        list1=list3
        list2=list4

        if not(len(list1)==0):
            for i,j in enumerate(list1):
                if not (re.search("OFF", j) == None):
                    index1.append(i)
            for i, j in enumerate(list1):
                if not (re.search("[0-9]", j) == None):
                    index1.append(i)
            for i, j in enumerate(list1):
                if not (re.search("'SALE'", j) == None):
                    index1.append(i)
            #print(index1)

        if not(len(list2)==0):
            for x,y in enumerate(list2):
                if not (re.search("OFF", y) == None):
                    index2.append(x)
            for x, y in enumerate(list2):
                if not (re.search("[0-9]", y) == None):
                    index2.append(x)
            for x, y in enumerate(list2):
                if not (re.search("'SALE'", y) == None):
                    index2.append(x)
            #print(index2)
        return list1,list2,index1,index2

    def snapshot_taker(self,links,year,month,day,country):
        driver.set_window_size(1960,1080)  # set the window size that you need \
        for i,link in enumerate(links):
            driver.get(link)
            driver.save_screenshot(str(year)+str(month)+str(day)+str(country)+'.png')
        print(" Screenshot file "+str(year)+str(month)+str(day)+str(country)+'.png'+" has been created")
        return


    def compareOffer(self, index, offer):
        if len(index) > 1:
            first_offer = offer[0][index[0] - 2:index[0]]
            second_offer = offer[1][index[1] - 2:index[1]]
            if int(first_offer) > int(second_offer):
                return first_offer, offer
            else:
                return second_offer, offer
        elif len(index)==1:
            offer = [offer[0], '']
            return offer[0][index[0] - 2:index[0]], offer
        else:
            return None,None


    def historical_puller(self, link,country):
        year = str(datetime.datetime.now().year)
        month = str(datetime.datetime.now().month)
        day = str(datetime.datetime.now().day)
        list=[]
        list1,list2,index1,index2=self.scraper(link,country)
        discount=''
        print("list1",list1,"list2",list2)
        print(country+"\n")

        # if not(list1[index1[0]].find('%')==-1) and not(list2[index2[0]].find('%')==-1):
        #     discount=str(max(int(list1[index1[0]][list1[index1[0]].find('%')-2:list1[index1[0]].find('%')]),
        #                  int(list2[index2[0]][list2[index2[0]].find('%') - 2:list2[index2[0]].find('%')])))
        # elif not(list1[index1[0]].find('%')==-1):
        #     discount=list1[index1[0]][list1[index1[0]].find('%')-2:list1[index1[0]].find('%')]
        # elif not(list2[index2[0]].find('%')==-1):
        #     discount=list2[index2[0]][list2[index2[0]].find('%')-2:list2[index2[0]].find('%')]
        # discount=discount+'%'

        if len(list1)==0 and not(len(list2)==0):
            if not (list2[index2[0]].find('%') == -1):
                discount = list2[index2[0]][list2[index2[0]].find('%') - 2:list2[index2[0]].find('%')]
                discount = discount + '%'

            if not(len( index2)==0):
                list.append(
                    {
                        "year": year,
                        "month": month,
                        "link": link,
                        "Top Banner": '',
                        "Additional discount message on the page": list2[index2[0]],
                        "Max discount": discount,
                        "day": day
                    }
                )

        elif not(len(list1)==0) and len(list2)==0:
            if not (list1[index1[0]].find('%') == -1):
                discount = list1[index1[0]][list1[index1[0]].find('%') - 2:list1[index1[0]].find('%')]
                discount = discount + '%'

            if not(len(index1)==0):
                list.append(
                    {
                        "year": year,
                        "month": month,
                        "link": link,
                        "Top Banner": list1[index1[0]],
                        "Additional discount message on the page": '',
                        "Max discount": discount,
                        "day": day
                    }
                )

        elif not(len(list1) == 0) and not(len(list2) == 0):
            if not (list1[index1[0]].find('%') == -1) and not (list2[index2[0]].find('%') == -1):
                discount = str(max(int(list1[index1[0]][list1[index1[0]].find('%') - 2:list1[index1[0]].find('%')]),
                                   int(list2[index2[0]][list2[index2[0]].find('%') - 2:list2[index2[0]].find('%')])))
                discount = discount + '%'
            list.append(
                {
                    "year": year,
                    "month": month,
                    "link": link,
                    "Top Banner":list1[index1[0]],
                    "Additional discount message on the page": list2[index2[0]],
                    "Max discount": discount,
                    "day": day
                }
            )

        else:
            list.append(
                {
                    "year": year,
                    "month": month,
                    "link": link,
                    "Top Banner": '',
                    "Additional discount message on the page": '',
                    "Max discount": discount,
                    "day": day
                }
            )

        return list

if __name__ == "__main__":
    year = str(datetime.datetime.now().year)
    month = str(datetime.datetime.now().month)
    day = str(datetime.datetime.now().day)
    hour = str(datetime.datetime.now().hour)
    minute = str(datetime.datetime.now().minute)
    second = str(datetime.datetime.now().second)
#    path=os.getcwd()
    path="/home/cians/hm/weekend/xoxo"
    newpath =path+"/"+str(year)+str(month)+str(day)+str(hour)+str(minute)+str(second)
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    os.chdir(newpath)
    df = pd.DataFrame()
    obj = historical_website_discount()
#    new_dict = {"US":"https://web.archive.org/web/20170917012730/http://www.hm.com/us","UK":"https://web.archive.org/web/20170917012730/http://www2.hm.com/en_gb/index.html",
#                "China":"https://web.archive.org/web/20170917012730/http://www2.hm.com/en_cn/index.html",
#        "Germany":'https://web.archive.org/web/20170917012730/http://www.hm.com/de'}

    new_dict = {"US":"http://www.hm.com/us","UK":"http://www2.hm.com/en_gb/index.html",
                "China":"http://www2.hm.com/en_cn/index.html","Germany":'http://www.hm.com/de'}


    writer = pd.ExcelWriter("historical_hm"+str(year)+str(month)+str(day)+".xlsx", engine='xlsxwriter')
    for k,v in new_dict.items():
        op=obj.historical_puller(v,k)
        df = pd.DataFrame(op)
        df=df.reindex_axis(['year','month','day','Top Banner','Additional discount message on the page','Max discount'],axis=1)
        df.to_excel(writer,index=False,sheet_name=k)
        obj.snapshot_taker([v],year,month,day,k)
        #sys.exit()
    writer.save()
    print("Excel file "+"historical_hm"+str(year)+str(month)+str(day)+".xlsx"+" has been created")




