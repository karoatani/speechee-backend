# Introduction

This is the backend that powers speeche the all in one content creation platform.

## Setup Guide

You will need python3 installed, [install here](https://www.python.org/downloads/)


## Activate a virtual environment using :
` python -m venv venv  && venv\Scripts\activate.bat`


## Install requirements.txt
` pip install -r requirements.txt `

## Run migrations
` python manage.py makemigrations && python manage.py migrate `

## Start Development Server
` python manage.py runserver `