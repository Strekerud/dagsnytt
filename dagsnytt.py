#!/usr/bin/env python
# coding:utf-8

import requests
from xml.etree import ElementTree
from fabric.colors import blue, green
import datetime
import duolingoer

import bbc_world

import xkcd
import smbc

import sys

from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint 
from pyfiglet import figlet_format


api = "http://podkast.nrk.no/program/dagsnytt_atten.rss"
weather = "https://wttr.in/oslo"

def printshows():
   
    feed = requests.get(api)
    tree = ElementTree.fromstring(feed.content)

    titles = [(item.find('title').text.encode('utf-8'), item.find('description').text.encode('utf-8')) for item in tree.findall('./channel/item')]

    print "=== DAGSNYTT ATTEN ==="
    for title, description in titles[:5]:
        print '=== {} ==='.format(blue(title))
        print description

def printWeather():
    response = requests.get(weather)
    print response.content

def getCountdown(day, month, year):
    print " === MASHACOUNTER ======================================"
    return (datetime.datetime(year, month, day) - datetime.datetime.now())

def colorPrint(text):
    cprint(figlet_format(" " + str(text) + " dager", font='starwars'),
       'white', attrs=['bold'])

def getDaysUntilMasha(day, month, year):
    print " === MASHACOUNTER ======================================"
    time_left = (datetime.datetime(year, month, day) - datetime.datetime.now())
    days_left = str(time_left.days + 1)
    colorPrint(days_left)


if __name__ == '__main__':
    print green("Retrieving the weather...")
    printWeather()
    print green("Getting the news...")
    printshows()
    bbc_world.getBBCWorldNews()
    #print green("Waiting for Masha<3...")
    #getDaysUntilMasha(23,6,2018)
    #print " ========================================================="
    print green("Showing latest XKCD")
    xkcd.show_todays_xkcd()
    print green("Showing latest SMBC")
    smbc.show_todays_smbc()
    print green("Finding duolingo stats...")
    duolingoer.printProgress()
