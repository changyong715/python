#!/usr/bin/env python
# coding=utf-8

'''
从小说网站抓取一本小说内容

'''
import urllib2 #python库提供一系列针对URL的操作方法
import re      #Re正则表达式库，提供了一系列针对正则表达式的方法

from bs4 import BeautifulSoup

import sys
#获取页面内容
def OpenPage(url):
    MyHeaders={}
    #urlib2.Request 填写两个参数，①URL，②我们的请求头headers
    request = urllib2.Request(url,headers=MyHeaders)  #构建了一个请求
    #获取返回对象，类文件对象
    f=urllib2.urlopen(request)
    #f.read()读取响应的内容
    data=f.read()
    #编码解码方法 decode 解码  encode 编码
    return data.decode("GBK").encode("utf-8")
    #return data

#测试访问页面内容
def Test1():
    print OpenPage("http://www.shengxu6.com/book/2967.html")

def ParseMainPage(page):
    #调用BeaytifulSoup库解析页面
    soup=BeautifulSoup(page,"html.parser")
    #find_all方法查询所有的指定内容
    #包含read字符串的href链接，通过正则表达式
    list_charts=soup.find_all(href=re.compile("read"))

    #url_list=["http://www.shengxu6.com"+item['href'] for item in list_charts]

    url_list=[]
    for item in list_charts:
        url_list.append("http://www.shengxu6.com"+item['href'])
    return url_list

#解析主页内容，获取url列表
def Test2():
    print ParseMainPage("http://www.shengxu6.com/book/2967.html")

def WriteDataToFlie(file_path,data):
    f=open(file_path,"a+")
    f.write(data)
    f.close()
    #with open(file_path,"a+") as f:

def Test4():
    WriteDataToFlie("tmp.txt","aisedfregdfgd\n")
    WriteDataToFlie("tmp.txt","sfrgfdvxzcgf\n")

#将获取的内容保存在文件中

if __name__=="__main__":
    Test1()






















