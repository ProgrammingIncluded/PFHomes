# Desc: Grab search results from search engine.
#       Operates with local storage to reduce scraping.
#
# Due to the nature of this file, we cannot push this file
# publically otherwise we violate TOS.

# Grab a list of files and save them to a txt

import numpy as np
import googlesearch as glg
from bs4 import BeautifulSoup
import urllib.parse as urllib
import urllib.request as urllib2
import traceback
import random
import time

RESULTS = []

def search_bing(query, iter):
    for i in range(0, iter):
        global RESULTS
        address = "http://www.bing.com/search?q=%s&count=10&first=%d" % (urllib.quote_plus(query), i * 10)

        getRequest = urllib2.Request(address, None, {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0'})

        urlfile = urllib2.urlopen(getRequest)
        htmlResult = urlfile.read(200000)
        urlfile.close()

        soup = BeautifulSoup(htmlResult, features="html5lib")

        results = soup.findAll('li', { "class" : "b_algo" })
        for result in results:
            RESULTS.append(result.find("a")["href"])
            print(result.find("a")["href"])
        
        # Save the file every 5 loops
        if i % 5 == 0:
            np.savetxt("site_full.txt", np.array(RESULTS), fmt="%s")

        # Cooldown
        time.sleep(random.randint(10, 50))

def search_google(query):
    for url in glg.search(query, stop=5000, pause=2):
        global RESULTS
        print(url)
        # Sleep after batches of 10.
        RESULTS.append(url)
        if len(results) % 9 == 0:
            time.sleep(random.randint(10, 100))

def main():
    # print(bs.scrape("test").text())

    query = "address here"

    try:
        search_bing(query, 50)
    except:
        traceback.print_exc()

    global RESULTS
    np.savetxt("site_full.txt", np.array(RESULTS), fmt="%s")

if __name__ == "__main__":
    main()