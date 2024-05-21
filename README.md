# Web Development Environment

## Overview

This project will give you all the tools to develop a static web page efficiently.

You can write seperate code in individual blocks and get combined output

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

## Usage

1. First for migrating database go to dir where manage.py is located and execute

     ```sh
    python manage.py makemigrations
    ```

    ```sh
    python manage.py migrate
    ```
   

2. Run server

    ```sh
    python manage.py runserver
    ```


