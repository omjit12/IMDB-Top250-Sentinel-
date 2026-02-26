🛡 IMDb Top250 Sentinel
Automated IMDb Rank Monitoring & Alert System

IMDb Top250 Sentinel is an end-to-end automated data pipeline that monitors IMDb Top 250 movie rankings, tracks rank changes over time, and sends real-time alerts when the #1 position changes.
This project demonstrates real-world data engineering concepts including web scraping, ETL processing, database management, automation workflows, and analytics integration.

🚀 Project Overview

The system performs the following operations automatically:
Scrapes IMDb Top 250 movies using Scrapy
Cleans and transforms the raw data using Python (Pandas)
Stores historical snapshots in MySQL
Compares latest and previous rankings
Sends automated email alerts via n8n when Rank #1 changes
Enables Power BI dashboard analysis for insights
This project simulates a real production-grade monitoring system.

🛠 Tech Stack

Python 3.12
Scrapy
Pandas
MySQL
SQLAlchemy
n8n (Automation)
Power BI (Dashboard & Analytics)

📊 Data Collected

For each movie:
Rank
Title
Year
Rating
Votes
Genres
Duration (ISO + minutes)
Certificate
Directors
Poster URL
IMDb URL
Scrape Timestamp

📈 Analytics Capabilities

Using Power BI, the system enables:
Genre distribution analysis
Rating trends by year
Duration bucket analysis
Top directors frequency
Rank movement tracking
Historical snapshot comparison

🎯 Key Features

✔ Fully automated pipeline
✔ Historical rank tracking
✔ Intelligent rank-change detection
✔ Production-style ETL process
✔ Dashboard-ready structured database
✔ Modular and scalable architecture
