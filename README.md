Email Sending Serverless API Project
Overview

This project is a Serverless REST API built with Python that allows sending emails through an HTTP POST request. It is designed to run both locally using serverless-offline and on AWS Lambda with API Gateway.

The project handles input validation, error handling, and returns appropriate HTTP status codes to indicate success or failure.

Features

Send emails using SMTP (smtplib)

REST API endpoint: /send (POST)

Input validation (checks for required fields: to, subject, body)

Returns standard HTTP responses:

200 → Email sent successfully

400 → Missing required fields

404 → Resourses not found

500 → Server or function error

Easily test locally with serverless-offline

Environment variables for secure configuration (EMAIL_host, EMAIL_prt, EMAIL_name, EMAIL_password)

Technology Stack

Python 3.12

Serverless Framework

SMTP (smtplib)

serverless-offline for local testing

Setup & Usage

Clone the repository

Create a .env file with your SMTP credentials

Install dependencies

Run locally:

npx serverless offline


Send POST requests to /dev/send using Thunder Client, Postman, or curl.

Notes

Do not commit .env or sensitive information

Make sure your SMTP credentials are valid and allow external connections

by Vruk(Yuvraj D Sirganor)
