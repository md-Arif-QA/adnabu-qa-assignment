# AdNabu QA Assignment

## Tech Stack

- Python
- Selenium
- Pytest
- Page Object Model (POM)

---

## Features Covered

- Product listing
- Product search
- Predictive search validation
- Variant selection
- Add to cart
- Cart quantity update
- Subtotal validation
- Checkout page validation
- Cart verification

---

## Project Structure

adnabu-qa-assignment/
│
├── pages/
├── tests/
├── utils/
├── requirements.txt
├── pytest.ini
└── README.md

---

## Setup Instructions

### Clone Repository

git clone <repo_url>

### Create Virtual Environment

python -m venv venv

### Activate Virtual Environment

Windows:
venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

---

## Install Dependencies

pip install -r requirements.txt

---

## Run Tests

pytest

---

## Framework Highlights

- Explicit waits used throughout framework
- Modular Page Object Model design
- Readable and maintainable code
- No hardcoded sleeps used