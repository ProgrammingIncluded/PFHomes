@ECHO OFF

REM Update Code
git pull origin master

REM Scrape Bing
python grab_results.py

REM Run the Crawler to get Site Data
REM Run ML learning and generate a list of potential websites then email.
python main.py

REM Allows us to email ourselves the results from results.txt
python email_results.py
