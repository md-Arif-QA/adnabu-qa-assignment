# AdNabu QA Assignment

## 📋 Project Overview

This is an end-to-end test automation project for an e-commerce website using Selenium WebDriver and Pytest. The project implements the Page Object Model (POM) design pattern to create maintainable and scalable test automation code.

## 🛠️ Tech Stack

- **Python 3.12** - Programming language
- **Selenium WebDriver** - Browser automation
- **Pytest** - Testing framework
- **WebDriver Manager** - Automatic driver management
- **Page Object Model (POM)** - Design pattern for maintainable code

## ✨ Features Covered

### 🏠 Home Page
- Application navigation
- Store password authentication
- Featured products listing

### 🔍 Search Functionality
- Search icon interaction
- Product search with predictive results
- Products section validation
- Product selection from search results

### 📦 Product Page
- Product page verification
- Product variant selection (Sunset variant)
- Add to cart functionality

### 🛒 Cart Management
- Cart drawer verification
- Checkout button interaction
- Product presence validation in cart

### 💳 Checkout Process
- Payment page validation
- Navigation back to store
- Order summary verification

## 📁 Project Structure

```
AdNabu_Assignment/
│
├── pages/                          # Page Object Model classes
│   ├── __init__.py
│   ├── home_page.py               # Home page interactions
│   ├── search_page.py             # Search functionality
│   ├── product_page.py            # Product details and cart
│   ├── cart_page.py               # Cart management
│   └── checkout_page.py           # Checkout process
│
├── tests/                         # Test files
│   ├── __init__.py
│   └── test_complete_purchase_flow.py  # End-to-end test
│
├── utils/                         # Utility modules
│   ├── __init__.py
│   └── driver_setup.py            # WebDriver configuration
│
├── conftest.py                    # Pytest fixtures and configuration
├── pytest.ini                     # Pytest configuration
├── requirements.txt               # Python dependencies
├── .gitignore                     # Git ignore rules
└── README.md                      # Project documentation
```

## 🔧 Prerequisites

- **Python 3.12** or higher
- **Git** for version control
- **Google Chrome** browser (latest version recommended)
- **Internet connection** for downloading WebDriver

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/md-Arif-QA/adnabu-qa-assignment.git
cd adnabu-qa-assignment
```

### 2. Verify Python Version

Ensure you have Python 3.12 installed:

```bash
python --version
# Should show: Python 3.12.x
```

If you don't have Python 3.12, download it from [python.org](https://www.python.org/downloads/).

### 3. Create Virtual Environment

Create a virtual environment to isolate project dependencies:

```bash
# Create virtual environment named 'venv'
python -m venv venv
```

### 4. Activate Virtual Environment

Activate the virtual environment:

**Windows (PowerShell/Command Prompt):**
```bash
# PowerShell
venv\Scripts\Activate.ps1

# Command Prompt
venv\Scripts\activate.bat
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

After activation, your terminal prompt should show `(venv)` at the beginning.

### 5. Install Dependencies

Install all required Python packages:

```bash
pip install -r requirements.txt
```

This will install:
- `selenium` - Web browser automation
- `pytest` - Testing framework
- `webdriver-manager` - Automatic ChromeDriver management

### 6. Verify Installation

Verify that all packages are installed correctly:

```bash
pip list
```

You should see packages like:
- selenium
- pytest
- webdriver-manager

## 🧪 Running Tests

### Run All Tests

```bash
pytest
```

### Run Tests with Verbose Output

```bash
pytest -v
```

### Run Tests with Console Output

```bash
pytest -v -s
```

### Run Tests with HTML Report

```bash
pytest --html=reports/test_report.html --self-contained-html
```

This generates a detailed HTML report in the `reports/` directory.

### Run Tests with JUnit XML Report

```bash
pytest --junitxml=reports/test_results.xml
```

### Run Specific Test with Report

```bash
pytest tests/test_complete_purchase_flow.py::TestCompletePurchaseFlow::test_search_add_cart_checkout_flow --html=reports/test_report.html --self-contained-html -v -s
```

## 📊 Test Execution Details

The main test `test_search_add_cart_checkout_flow` performs a complete e-commerce purchase flow:

1. **Setup**: Initialize WebDriver and page objects
2. **Home Page**: Open application and enter store password
3. **Product Discovery**: List all featured products
4. **Search**: Search for "The Complete Snowboard"
5. **Product Selection**: Select product from search results
6. **Product Details**: Verify product page and select variant
7. **Add to Cart**: Add product to shopping cart
8. **Cart Verification**: Verify cart contents
9. **Checkout**: Proceed to checkout and verify payment page
10. **Navigation**: Return to store and verify cart persistence
11. **Teardown**: Close browser automatically

## 🔍 Test Results

Test execution provides detailed console output with:
- Step-by-step progress indicators
- Product listing information
- Verification confirmations
- Error details (if any)

## 📊 Test Reports

The project supports generating comprehensive test reports:

### HTML Reports
- Generated using `pytest-html` plugin
- Self-contained HTML files with detailed test results
- Includes screenshots, logs, and execution times
- Located in `reports/test_report.html`

### JUnit XML Reports
- Standard XML format for CI/CD integration
- Contains test results, durations, and failure details
- Located in `reports/test_results.xml`

### Viewing Reports
1. Run tests with report generation: `pytest --html=reports/test_report.html --self-contained-html`
2. Open the generated HTML file in any web browser
3. Review test execution details, timings, and any failures

**Note**: A sample test report (`reports/test_report.html`) is included in the repository for reference.

## 🛠️ Troubleshooting

### Common Issues

1. **ChromeDriver Issues**
   - Ensure Google Chrome is installed and updated
   - WebDriver Manager handles driver downloads automatically

2. **Virtual Environment Issues**
   - Ensure virtual environment is activated (check `(venv)` in prompt)
   - Try deactivating and reactivating: `deactivate` then activate again

3. **Import Errors**
   - Verify all dependencies are installed: `pip install -r requirements.txt`
   - Check Python version compatibility

4. **Test Failures**
   - Check internet connection for website access
   - Verify website is accessible and not under maintenance
   - Check console output for specific error messages

### Getting Help

If you encounter issues:
1. Check the console output for error messages
2. Verify all prerequisites are met
3. Ensure virtual environment is properly activated
4. Check that all dependencies are installed

## 📝 Notes

- Tests are designed to run in a real browser environment
- Chrome browser window will open and close automatically during test execution
- Test execution may take 1-2 minutes depending on network conditions
- All test data and URLs are configured for the AdNabu test environment

## 🤝 Contributing

1. Fork the repository: [https://github.com/md-Arif-QA/adnabu-qa-assignment](https://github.com/md-Arif-QA/adnabu-qa-assignment)
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Make your changes and add comments where needed
4. Run tests to ensure everything works: `pytest -v -s`
5. Commit your changes (`git commit -m 'Add your feature'`)
6. Push to your fork (`git push origin feature/your-feature`)
7. Submit a pull request with detailed description

## 📧 Contact & Support

For questions or issues, please open an issue on [GitHub Issues](https://github.com/md-Arif-QA/adnabu-qa-assignment/issues).

---

**Happy Testing! 🚀**