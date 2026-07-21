# 🚀 QA Automation Framework

A modern **UI Test Automation Framework** built with **Python**, **Selenium 4**, and **Pytest** following the **Page Object Model (POM)** design pattern. This project demonstrates industry-standard practices for building maintainable, scalable, and reusable automated UI tests.

> **Status:** Active Development 🚧

---

## ✨ Features

* ✅ Selenium 4 UI Automation
* ✅ Pytest Test Framework
* ✅ Page Object Model (POM)
* ✅ Explicit Waits
* ✅ Parameterized Test Cases
* ✅ Automatic Screenshot Capture on Failure
* ✅ HTML Test Reports
* ✅ Centralized Configuration
* ✅ Logging with Loguru
* ✅ GitHub Actions CI
* ✅ Modern dependency management with `uv`
* ✅ Clean, modular project structure

---

## 🛠️ Tech Stack

| Category          | Tools             |
| ----------------- | ----------------- |
| Language          | Python 3.13       |
| Automation        | Selenium 4        |
| Test Framework    | Pytest            |
| Driver Management | webdriver-manager |
| Reporting         | pytest-html       |
| Logging           | Loguru            |
| Code Quality      | Ruff              |
| Package Manager   | uv                |
| CI/CD             | GitHub Actions    |
| Version Control   | Git & GitHub      |

---

## 📂 Project Structure

```text
qa-automation-framework-python/
│
├── config/
│   └── settings.py
│
├── pages/
│   ├── base_page.py
│   └── login_page.py
│
├── tests/
│   └── test_login.py
│
├── utils/
│   ├── driver_factory.py
│   └── logger.py
│
├── screenshots/
├── reports/
├── logs/
│
├── .github/
│   └── workflows/
│       └── qa.yml
│
├── conftest.py
├── pytest.ini
├── README.md
└── .gitignore
```

---

## 🎯 Test Scenarios

Current automated scenarios include:

* Valid Login
* Invalid Login
* Empty Username
* Empty Password
* Empty Credentials
* Locked User Login

More scenarios such as Product Search, Cart, Checkout, Logout, and End-to-End Purchase Flow will be added.

---

## 🌐 Test Application

This framework automates the SauceDemo application.

**Website**

https://www.saucedemo.com/

**Test Credentials**

Username: `standard_user`

Password: `secret_sauce`

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/RohanSharma-exe/qa-automation-framework-python.git

cd qa-automation-framework-python
```

Install dependencies

```bash
uv sync
```

---

## ▶️ Run Tests

Execute all tests

```bash
uv run pytest
```

Run a specific test

```bash
uv run pytest tests/test_login.py
```

---

## 📊 Generate HTML Report

```bash
uv run pytest
```

The report is generated in:

```text
reports/report.html
```

---

## 📸 Failure Screenshots

Whenever a test fails, a screenshot is automatically saved to:

```text
screenshots/
```

This helps speed up debugging and failure analysis.

---

## 🔄 Continuous Integration

Every push and pull request automatically:

* Installs dependencies
* Executes the test suite
* Verifies framework integrity

using **GitHub Actions**.

---

## 📈 Future Improvements

* Cross-browser execution (Chrome, Edge, Firefox)
* Data-driven testing
* Parallel execution
* API automation integration
* Docker support
* Playwright implementation
* Browser matrix testing
* Retry mechanism for flaky tests

---

## 💡 Why This Project?

This project demonstrates practical skills expected from a QA Automation Engineer, including:

* Automation framework design
* Test case implementation
* UI testing best practices
* Maintainable Page Object Model architecture
* Continuous Integration
* Logging and reporting
* Clean code organization

---

## 👨‍💻 Author

**Rohan Sharma**

GitHub: https://github.com/RohanSharma-exe

LinkedIn: https://linkedin.com/in/rohan-sharma-372ab2252

Email: [rohan.sharma1234987650@gmail.com](mailto:rohan.sharma1234987650@gmail.com)

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
