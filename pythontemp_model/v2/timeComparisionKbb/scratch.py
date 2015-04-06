#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: scratch.py

import argparse
import requests
from bs4 import BeautifulSoup

from scrape.util import construct_base_url, construct_parameters
from scrape.util import url_fetch
from scrape.util import parse_new, parse_single, parse_list
import modelkbb_v1_debug
import time

description = """Scrape data from KBB"""

parser = argparse.ArgumentParser(description=description)
# Positional (pass them in proper order, and yes they are required)
parser.add_argument('make', help='Make')
parser.add_argument('model', help='Model')
parser.add_argument('year', help='Year')
parser.add_argument('style', help='Style')
# Optional
optional_args_names = ['intent', 'pricetype', 'mileage']
parser.add_argument('-i', '--intent', dest='intent', help='Intent')
parser.add_argument('-p', '--pricetype', dest='pricetype', help='Price Type')
parser.add_argument('-m', '--mileage', dest='mileage', help='Mileage')


def directExtract(args):   
    url = construct_base_url(args.make, args.model, args.year, args.style)
    optional_parameters = ['intent', 'pricetype', 'mileage']
# we use the built in command 'vars' to convert the argparse.Namespace
# to a standard python dictionary... what even is an argparse.Namespace?
    parameters = construct_parameters(vars(args), optional_parameters)
    url_fetched = url_fetch(url, parameters)
    tempprice=modelkbb_v1_debug.extractPricekbb(url_fetched.text)
    #print tempprice
diction=['ce-sedan-4d','le-sedan-4d','se-sedan-4d','xle-sedan-4d','hybrid-sedan-4d']
sumtime=0
for term in diction:
    time1=time.time()
    tempar='toyota camry 2007 '+term+' -i buy-used -p private-party -m 111000'
    args = parser.parse_args(tempar.split())
    price=directExtract(args)
    time2=time.time()
    sumtime+=time2-time1

time1=time.time()
pricelist=modelkbb_v1_debug.getKbbPrice('toyota','camry','2007','111000')
time2=time.time()
print time2-time1,sumtime


sumtime=0
for term in diction:
    time1=time.time()
    tempar='toyota corolla 2007 '+term+' -i buy-used -p private-party -m 111000'
    args = parser.parse_args(tempar.split())
    price=directExtract(args)
    time2=time.time()
    sumtime+=time2-time1

time1=time.time()
pricelist=modelkbb_v1_debug.getKbbPrice('toyota','corolla','2007','111000')
time2=time.time()
print time2-time1,sumtime


hondadiction=['si-coupe-2d','lx-coupe-2d','dx-coupe-2d','ex-coupe-2d','ex-coupe-2d','ex-sedan-4d','hybrid-sedan-4d','gx-sedan-4d','lx-sedan-4d','si-sedan-4d','dx-sedan-4d']
sumtime=0
for term in hondadiction:
    time1=time.time()
    tempar='honda accord 2007 '+term+' -i buy-used -p private-party -m 111000'
    args = parser.parse_args(tempar.split())
    price=directExtract(args)
    time2=time.time()
    sumtime+=time2-time1

time1=time.time()
pricelist=modelkbb_v1_debug.getKbbPrice('honda','accord','2007','111000')
time2=time.time()
print time2-time1,sumtime


sumtime=0
for term in hondadiction:
    time1=time.time()
    tempar='honda civic 2007 '+term+' -i buy-used -p private-party -m 111000'
    args = parser.parse_args(tempar.split())
    price=directExtract(args)
    time2=time.time()
    sumtime+=time2-time1

time1=time.time()
pricelist=modelkbb_v1_debug.getKbbPrice('honda','civic','2007','111000')
time2=time.time()
print time2-time1,sumtime
#example_url = 'http://www.kbb.com/kia/optima/2012-kia-optima/ex-sedan-4d/?pricetype=private-party&mileage=25000'

#url_requested = requests.get(example_url)
#print url_requested.status_code
#if url_requested.status_code == 200:
#    prices = []
    #print url_requested.text
#    soup = BeautifulSoup(url_requested.text)

#    for div in soup.find_all('div', class_='value'):
#        print div.text

