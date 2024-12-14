# 167293.airline_booking_system

## Description
This is a simplified airline booking system built with Django and Django Rest Framework (DRF). The system allows you to:
- Manage flights and passengers.
- Perform CRUD operations via an API.

## Features
- List, retrieve, create, and delete flights and passengers.
- Enforces relationships and constraints:
  - A flight can have multiple passengers.
  - A passenger must belong to exactly one flight.
- Includes API filtering and pagination for better usability.

## Requirements
- Python 3.13 or higher
- Django 5.1.4
- Django Rest Framework (DRF)

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/<Admin>/167293.airline_booking_system.git
   cd 167293.airline_booking_system
