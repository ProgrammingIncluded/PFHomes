REM Update Code
git pull origin master

REM Scrape Bing
python grab_results.py "ADDRESS HERE"

REM Run the Crawler to get Site Data
REM Run ML learning and generate a list of potential websites then email.
python main.py

