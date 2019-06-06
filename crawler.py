############################################
# Project: P5Home
# File: crawler.py
# By: ProgrammingIncluded
# Website: ProgrammingIncluded.com
# Desc: File to contain web crawling related
# functionalities.
############################################
from bs4 import BeautifulSoup
import requests
import urllib.parse as up
import traceback
from selenium import webdriver
import time
import os

# Crawler to get all the text that is available from a given site
# requires an array of websites.
class Crawler:
    # Go into each site
    def __init__(self, model, skip):
        self.sites = None
        self.skip = set()
        self.model = model
        for s in skip:
            self.skip.add(s)
    
    # Get the downloaded data from local files
    def parseCache(self, cacheFolder, fileNames=None):

        results = []
        t = 0
        for f in os.listdir(cacheFolder):
            if not f.endswith(".html"):
                continue

            soup = BeautifulSoup(open(os.path.join(cacheFolder, f), encoding="utf-8"), "html.parser")
            texts = soup.find_all("body")
            stats = [
                i.text for i in texts
            ]
            res = self.model.run(''.join(stats))
            if fileNames == None:
                results.append((f, res))
            else:
                results.append((fileNames[t], res))

            # Increase counter
            t += 1
        return results

    # Get the data
    def downloadHTML(self, sites):
        self.sites = sites
        results = []
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0'}
        for i in range(0, self.sites.shape[0]):
            site = self.sites[i]
            puri = up.urlparse(site)
            domain = '{uri.netloc}'.format(uri=puri)

            if domain in self.skip:
                continue

            html = None
            soup = None
            driver = webdriver.Chrome()
            try:
                driver.get(site)
                time.sleep(10)
                # Save the html
                wf = open("cache/" + str(i) + ".html", "w", encoding="utf-8")
                wf.write(driver.page_source)
                wf.close()
            except:
                traceback.print_exc()
                print("\31[Failed: ", site)
                driver.quit()
                continue
            driver.quit()


        return results