# WDE

## Overview

WDE is a web based IDE like interface in which you can write HTML, CSS and JavaScript code, and get the output instantly.

You can write seperate code in individual blocks and get the combined output.

Follwoing are few screenshots for reference,

![Screenshot](/static/img/sc1.png)

Javascript is also executed as per behaviour
![Screenthot](/static/img/sc2.png)

## Prerequisite

1. Python >= 3.10

## Setup

### Installation
1. clone the repo
    ```sh
    git clone <repo_url>
    ```
2. Create and Activate virtual environment ( optional )
    ```sh
    python -m venv env
    ```
    For Windows
    ```sh
    env\Scripts\activate
    ```
    For Linux/Mac
    ```sh
    source env/bin/activate
    ```

3. Install dependencies
    ```sh
    pip install -r requirements.txt
    ```

4. For migrating database go to dir where manage.py is located and execute

     ```sh
    python manage.py makemigrations
    ```

    ```sh
    python manage.py migrate
    ```
   
5. Create superuser ( optional )

    ```sh
    python manage.py createsuperuser
    ```

## Usage

1. Run server

    ```sh
    python manage.py runserver
    ```

2. Visit [http://localhost:8000](http:127.0.0.1:8000) in your browser.


