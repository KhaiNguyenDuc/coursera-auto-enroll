# Auto enroll coursera

Welcome to [Your Python Library Name]! This library does [brief description].

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Installation](#installation)
   - [Step 1: Install Python](#step-1-install-python)
   - [Step 2: Install the library](#step-2-install-the-library)
3. [Usage](#usage)


## Prerequisites

Before you begin, ensure you have the following installed:

- [Python](https://www.python.org/downloads/) (version 9.0 or higher)
- Coursera bussiness acount

## Installation

Follow these steps to set up and install [Your Python Library Name]:

### Step 1: Install Python

Download and install Python from the official website: [Python Downloads](https://www.python.org/downloads/)

### Step 2: Install the library

Install the library: 
```bash
git clone https://github.com/KhaiNguyenDuc/coursera-auto-enroll
```

Install the requirement: 
```bash
pip install requirement.txt
```

## Usage

Login in coursera with your bussiness account

Using F12 ( dev tool ) and search for below API:

![image](https://github.com/KhaiNguyenDuc/coursera-auto-enroll/assets/71761537/b9a9f076-54b2-4c0a-82cf-e23f08ee6adf)


Under headers tab, get all cookies:

![image](https://github.com/KhaiNguyenDuc/coursera-auto-enroll/assets/71761537/849f2579-d6a8-4a2c-8b46-2d7aa7ab2f10)

Passing all of your cookies inside cookies.txt

If you want to adjust the thread, consider modify thread count in thread.txt. Default is 5

After done all above. Open terminal in library directory and using below command:

```
python main.py
```

Your account will automatically enroll for all available code, wait some time :D
