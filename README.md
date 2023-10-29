
# API Testing Framework

## Overview

This API Testing Framework is a robust, scalable, and easy-to-use solution designed to make API testing a breeze. Built with Python, this framework leverages popular libraries to provide a straightforward way to write, organize, and run your API tests.

## Features

- 📦 **Modular Codebase**: The code is organized into modules for ease of maintenance and scalability.
- 🚀 **Fast Execution**: Tests are designed to run quickly and efficiently.
- 📋 **Easy to Use**: Simple setup and execution procedures.
- 📚 **Well Documented**: Each module and function comes with clear documentation.
- 🛠 **Utility Scripts**: A range of utility scripts to make your testing life easier.

## Directory Structure

```
.
├── main.py
├── tests/
│   └── test_google_maps_api.py
├── utils/
│   ├── api.py
│   ├── checking.py
│   ├── http_method.py
│   └── logger.py
```

## Prerequisites

- Python 3.x
- Required Python packages: `pytest`, `requests`, `allure-pytest`

## Setup

1. Clone the repository to your local machine.
    ```bash
    git clone https://github.com/your_username/api-testing-framework.git
    ```
2. Navigate to the project directory.
    ```bash
    cd apiProject
    ```
3. Install the required Python packages.
    ```bash
    pip install -r requirements.txt
    ```
4. Optional: Install Allure command-line tools for generating allure reports. [Allure Installation Guide](https://docs.qameta.io/allure/#_installing_a_commandline)


## Running Tests

To run all the tests, simply execute the `main.py` file.

```bash
python main.py
```

Alternatively, you can run specific tests using `pytest`.

```bash
pytest tests/test_google_maps_api.py
```

## Utility Modules

- `api.py`: Contains generic API request methods.
- `checking.py`: For all your validation needs.
- `http_method.py`: Enumerations for HTTP methods.
- `logger.py`: Logging utilities.

## Contributing

Feel free to fork the project, open a PR, or submit an issue.

## Author

Narek Amaryan

---

