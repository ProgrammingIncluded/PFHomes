import numpy as np
from crawler import Crawler
import basemodel as bm

# We can skip any major sites
SKIP = ["zillow", "redfin", "apartments"]

# Calculate success rate
def detected(results):
    count = 0
    for p in results:
        if p[1] == True:
            count += 1
    return count

def main():
    # Read form our list of sites
    sites = np.genfromtxt("site_full.txt", dtype="str")
    bot = Crawler(bm.BaseModel(), SKIP)
    # bot.downloadHTML(sites)
    results = bot.parseCache("cache")
    print(results)
    print(detected(results))


if __name__ == "__main__":
    main()