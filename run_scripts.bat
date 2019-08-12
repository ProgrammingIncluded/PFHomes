echo "***LOGGER***" 
python log_archiver.py

REM Update Code
echo "***UPDATE***"  >> RESULTS.log 2>&1
git pull origin master >> RESULTS.log 2>&1

REM Scrape Bing
echo "***GRAB***"  >> RESULTS.log 2>&1
python grab_results.py >> RESULTS.log 2>&1

REM Run the Crawler to get Site Data
REM Run ML learning and generate a list of potential websites then email.
echo "***MAIN***"  >> RESULTS.log 2>&1
python main.py >> RESULTS.log 2>&1

REM Allows us to email ourselves the results from results.txt
echo "***EMAIL***"  >> RESULTS.log 2>&1
python email_results.py >> RESULTS.log 2>&1
