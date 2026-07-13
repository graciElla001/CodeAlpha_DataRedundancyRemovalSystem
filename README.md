#  CodeAlpha Data Redundancy Removal System

A Flask-based web application developed as part of the **CodeAlpha Internship Program** to improve database quality by detecting duplicate records, validating user input, and classifying false positives before storing data.

---

##  Project Overview

This application helps organizations maintain clean and reliable databases by preventing duplicate entries and identifying records that may already exist.

The system combines **exact duplicate detection** (using email validation) with **fuzzy matching** (using RapidFuzz) to identify similar names. Users can review potential duplicates and choose whether to save them as **False Positives**, ensuring important records are not mistakenly rejected.

---

##  Features

*  Prevents duplicate email entries
*  Detects similar names using RapidFuzz
*  Classifies records as **Unique** or **False Positive**
*  Allows users to manually confirm potential duplicates
*  Stores validated records in an SQLite database
*  Simple and responsive web interface
*  Modular Flask project structure

---

##  Technologies Used

* Python
* Flask
* SQLite3
* RapidFuzz
* HTML5
* CSS3
* Git
* GitHub

---

##  Project Structure

```text
CodeAlpha_DataRedundancyRemovalSystem/
│
├── app.py
├── database.py
├── duplicate_checker.py
├── data.db
├── requirements.txt
├── README.md
│
├── static/
│   └── style.css
│
├── templates/
│   ├── index.html
│   ├── success.html
│   ├── duplicate.html
│   ├── warning.html
│   └── records.html
│
└── venv/
```

---

##  How It Works

1. User enters their information.
2. The system checks whether the email already exists.
3. If a duplicate email is found, the record is rejected.
4. If the email is unique, the system compares the name against existing records using RapidFuzz.
5. If a similar name is detected, the user is warned.
6. The user can either:

   * Cancel the operation, or
   * Save the record as a **False Positive**.
7. The validated record is stored in the database.

---

##  Installation

Clone the repository:

```bash
git clone https://github.com/graciElla001/CodeAlpha_DataRedundancyRemovalSystem.git
```

Navigate to the project folder:

```bash
cd CodeAlpha_DataRedundancyRemovalSystem
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment (Windows):

```bash
venv\Scripts\activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

---

## Future Improvements

* User authentication
* Dashboard with analytics
* Export records to CSV/Excel
* Cloud database integration
* REST API support
* AI-powered duplicate detection

---

##  Author

**Ijeoma Onwuasoanya**

Developed as part of the **CodeAlpha Internship Program**.
