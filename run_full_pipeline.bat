@echo off

cd /d "%~dp0"

echo ==============================
echo STEP 1: Running Scrapy
echo ==============================

cd imdb_scraper
"..\.venv\Scripts\python.exe" -m scrapy crawl imdb_top250 -o imdb_raw.csv
cd ..

echo ==============================
echo STEP 2: Cleaning Data
echo ==============================

".\.venv\Scripts\python.exe" Data_cleaning\clean_imdb.py

echo ==============================
echo STEP 3: Loading to MySQL
echo ==============================

".\.venv\Scripts\python.exe" Data_cleaning\load_to_mysql.py

echo ==============================
echo FINISHED
echo ==============================
pause