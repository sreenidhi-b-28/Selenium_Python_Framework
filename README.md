# Selenium Python Automation Framework

Selenium Python Automation Framework with Pytest

## Installation

Install the requirements using the below,

```bash
pip install -r requirements.txt
```


## Project features

**Page Object Model**: This project follows the POM design pattern enhancing maintainability and readability.

**Data-driven tests** - Tests are data-driven with data being fetched from Excel (.xlsx) file

**Logger** - Logging mechanism is implemented in each test case for debugging.

**Pytest** - Testing framework for executing test cases

**Pytest-html** - Used to generate detailed HTML reports for test results.


## Execution

Move to the tests folder and execute the below command,

```bash
pytest -rA --tb=no reports='../reports/report.html'
```
The above command will generate an HTML named `report.html` under reports folder that can be analyzed for detailed test case results.
