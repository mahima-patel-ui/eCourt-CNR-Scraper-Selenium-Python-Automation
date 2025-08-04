
# 🧑‍⚖️ Court CNR Scraper – Internship Project

This Python script automates the process of fetching case details from the Indian eCourts portal using a 16-digit CNR number.

## 📌 Features

- Accepts a valid 16-digit CNR (e.g., HRFB010018772023)
- Opens the official eCourts website
- Waits for the user to manually solve the CAPTCHA
- Scrapes and displays:
  - Party Name
  - Filing Date
  - Next Hearing Date
  - Case Status
  - Judge & Court Number (if available)

## ⚙️ Tech Stack

- Python
- Selenium WebDriver (Chrome)
- Manual CAPTCHA handling

## ▶️ How to Run

1. Make sure `chromedriver.exe` is in the same folder as `court_scraper.py`
2. Install Selenium:

```bash
pip install selenium
```

3. Run the script:

```bash
python court_scraper.py
```

4. Enter the 16-digit CNR number
5. Solve the CAPTCHA manually when the browser opens
6. Press Enter in terminal once done
7. View the extracted case details in the terminal

## 📄 Sample Output

```
Court: District and Sessions Court, Faridabad
Case Type: UNTRACE/CANCELLATION REPORT
Filing Date: 09-02-2023
Case Status: Case disposed
Decision Date: 11-02-2023
Petitioner: STATE OF HARYANA (Advocate - PP)
Respondent: PARKASH BHADANA S/O DESHRAJ
```

## 📁 Folder Structure

```
court-scraper/
├── court_scraper.py
├── chromedriver.exe
├── requirements.txt
├── README.md
```

## 🧠 Notes

- Works with valid CNR only (e.g., from Haryana courts)
- CAPTCHA must be solved manually
- ChromeDriver version must match your installed Chrome browser

---

**Built by Mahima Patel for internship assessment at Labmantix.**
