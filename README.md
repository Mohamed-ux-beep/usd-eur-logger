# 💱 USD to EUR Daily Exchange Rate Logger

This project automatically logs the daily exchange rate of **USD to EUR** by scraping data from [wise.com](https://wise.com/de/currency-converter/usd-to-eur-rate) and storing it in a CSV file using a scheduled GitHub Actions workflow.

## 🚀 Features

- ✅ Scrapes live USD→EUR exchange rate from Wise
- 📅 Logs exchange rate daily at 07:00 UTC (can be adjusted)
- 📄 Appends data to a local CSV file `exchange_rates.csv`
- ☁️ Fully automated using GitHub Actions
- 🔍 Cleaned and structured format ready for data analysis

## 🛠️ How it works

- A Python script (`log_to_csv.py`) uses `requests` and `BeautifulSoup` to extract the current exchange rate.
- The script writes the result into a CSV file with columns:
  - `Date time`
  - `USD`
  - `EUR`
- A GitHub Actions workflow (`log_csv.yml`) runs this script every day and commits the updated CSV to the repository.

## 📊 Sample Output (CSV)

Date time,USD,EUR 2025-03-22 07:00:00,1000,924.6 2025-03-23 07:00:00,1000,926.1


## 🤖 Future Plans: Machine Learning

In the next phase of this project, we aim to integrate **machine learning models** to:

- Predict future USD/EUR exchange rates
- Analyze trends and seasonal patterns
- Visualize prediction confidence over time

We'll use historical data collected by this logger as a foundation for training and evaluating our models (e.g. using regression, time series forecasting, etc.).

## 📦 Tech Stack

- Python 3
- BeautifulSoup4
- Requests
- GitHub Actions
- CSV file storage


## 🧠 Authors & Contributors

Created by Mohamed Abokahf 
Feel free to fork, contribute, or open issues.

---

*Data provided by [wise.com](https://wise.com). This project is for educational and non-commercial use.*

