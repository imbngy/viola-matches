# viola-matches

### Description
Viola-Matches is a Python script designed to scrape all matches played by Fiorentina in the current Serie A season from the website adamchoi.co.uk. It utilizes Selenium for web scraping, allowing you to easily gather information about Fiorentina's performance during the season.

### Requirements

To run Viola-Matches, you need to have the following dependencies installed:
- [Python 3.11.6](https://www.python.org/downloads/)
- Selenium
- Pandas
- tqdm

You can install the required packages using the following commands:

```bash
pip install selenium
```

```bash
pip install pandas
```

```bash
pip install tdqm
```

> [!NOTE]
> Manually installing a WebDriver for Chrome is not required anymore as of Selenium 4.14.0

### Usage 

1. Clone the repository:

```bash
git clone https://github.com/imbngy/viola-matches.git
```
2. Navigate to the project directory:

```bash
cd viola-matches
```
3. Run the script:

```
py main.py
```

The script will launch a headless Chrome browser, navigate to adamchoi.co.uk, and scrape the match data for Fiorentina from the last Serie A season.

### Output

Viola-Matches will generate a CSV file named `matches.csv` containing the following information for each match:

- Date
- Team Name
- Score
- Opponent Team Name

Feel free to customize the script to include additional data or modify the output format according to your needs.

### Contributing

If you find any issues or have suggestions for improvements, please open an issue or submit a pull request. Contributions are welcome!
