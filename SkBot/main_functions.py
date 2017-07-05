# -*- coding: utf-8 -*

import os

from tokenize import String

import skpy
import vk
from django.views.static import serve
from skpy import Skype
from skpy import SkypeContact
from skpy import SkypeContacts
from getpass import getpass
from skpy import SkypeChat
from skpy import SkypeUser
from skpy import SkypeGroupChat
import csv

from SkBot import hist




#sk = Skype()
#def auth():
#    sk = Skype(login, password)

#    return ""

def allContacts():
    login = hist.name
    password = hist.pwd
    sk = Skype(login, password)

    res = ''


    for val in sk.contacts:
            res += val.id + '\n'
    return res





def grayContacts():
    login = hist.name
    password = hist.pwd
    sk = Skype(login, password)

    res = ''
    for val in sk.contacts:
        if (val.authorised == False):
            if(val.blocked == False):
                res += val.id + "\n"
    return res

def sendGreeting(id, msg):
    login = hist.name
    password = hist.pwd
    cs = str(id).split( )
    sk = Skype(login, password)
    for val in cs:
        sk.contacts.search(val)[0].invite(msg)

    return ""

def sendMsg(text):
    login = hist.name
    password = hist.pwd
    sk = Skype(login, password)
    for val in sk.contacts:
        try:
            ch = val.chat
            ch.sendMsg(text)
        except:
            pass

    return ""


####!!!!!!!!!!!!!!!!!!!!!
def clear():
    login = hist.name
    password = hist.pwd
    sk = Skype(login, password)
    res = ''
    for val in sk.contacts:
        if (val.authorised == False):
            sk.contacts.user(val.id).block()
            res += val.id + "\n"

    return res


def Authorizing():
    login = hist.name
    password = hist.pwd
    sk = Skype(login, password)

    for val in sk.contacts:
        if (val.authorised == False):
            sk.contacts.user(val.id).invite("")

    return ""

#!!!!!!!!!!!!!!!!!!!!!!!!!
#def getChats():
#    sk = Skype(login, password)
#    res = ''
#    for val in sk.chats:
#       res += val. + "\n"


#    return ""


def sendChats(val):
    login = hist.name
    password = hist.pwd
    sk = Skype(login, password)
    for c in sk.chats.recent():
        try:
            sk.chats.chat(c).sendMsg(val)
        except:
            pass

    return ""

def contactsFromChats():
    login = hist.name
    password = hist.pwd
    sk = Skype(login, password)
    res = ''
    for val in sk.chats.recent():
        for usr in sk.chats.chat(val).users:
            try:
                res += usr.id + '\n'
            except:
                pass

    return res

def getLists():
    login = hist.name
    password = hist.pwd
    sk = Skype(login, password)
    res = ''
    for val in sk.contacts.groups:
        res += val.Id + "\n"


    return res

def sendGrays(msg):
    login = hist.name
    password = hist.pwd
    sk = Skype(login, password)
    res = ''
    for val in sk.contacts:
        try:
            if (val.authorised == False):
                sk.contacts.user(val.id).authorised = True
                ch = sk.chats.create(val.id)
                ch.sendMsg(msg)
        except:
            pass

    return res


def output(request):
    # !/usr/bin/env python
    # -*- coding:utf-8 -*-
    login = hist.name
    password = hist.pwd
    sk = Skype(login, password)
    f = open(sk.userId + ".csv", 'wt')

    writer = csv.writer(f)
    writer.writerow(("Login", "Name", 'Birthday', 'Country', 'Phone'))

    res = ''
    for val in sk.contacts:
        try:
            res += val.id + "," + sk.contacts.user(val.id).name.first + "," + sk.contacts.user(val.id).name.last +"\n"
        except:
            pass

    writer.writerow(res)
    f.close()

    return serve(request, os.path.basename(sk.userId + ".csv"), os.path.dirname(sk.userId + ".csv"))


def outputvk(lgn, pwd):

    session = vk.AuthSession('5870512', lgn, pwd)
    vk_api = vk.API(session)

    res = ''
    for val in vk_api.friends.get(fields="connections,skype"):
        if(str(val).__contains__("skype")):
            res += str(val)

        text_file = open("Output.txt", "w")
        text_file.write(res)
        text_file.close()

    return serve(os.path.basename("res.txt"), os.path.dirname("res.txt"))