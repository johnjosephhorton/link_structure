#!/usr/bin/env python3

import csv
import os 
import subprocess
import json

def CleanURL(url):
    """Take the trailing '/' off a URL """
    if url[-1]=="/":
        return url[0:(len(url)-1)]
    else:
        return url
    
def OutboundURLs(url):
    """For a given URL, extract all the outbound links """
    result = subprocess.run(['lynx', '-listonly', "-nonumbers", "-dump", url],
                             stdout=subprocess.PIPE)
    outbound_urls = result.stdout.decode("utf-8").lower().strip().split("\n")
    outbound_urls.pop()
    return [CleanURL(url) for url in outbound_urls]

urls_to_products = dict({})
links = dict({})
with open("structure.csv", 'r') as csvfile:
    products = csv.reader(csvfile)
    header = next(products) # absorb the header
    for product in products:
        student, product, raw_url, html = product # read a line
        url = CleanURL(raw_url.strip().lower())
        outbound_urls = OutboundURLs(url)
        urls_to_products[url] = product.strip().lower()
        links[url] = outbound_urls
         
## write out the network structure 
with open("network_structure.csv", 'w') as csvfile:
    spamwriter = csv.writer(csvfile)
    for node in list(links.keys()):
        product = urls_to_products[node]
        for ob_link in links[node]:
            if ob_link in urls_to_products:
                spamwriter.writerow([product, urls_to_products[ob_link]])

         

