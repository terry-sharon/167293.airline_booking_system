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

   
---

## Detailed Explanation of Project Components**

#### **Models**
- **Flight**:
  - Represents the flights in the system.
  - Includes fields like `flight_number`, `departure`, and `capacity`.
- **Passenger**:
  - Represents passengers associated with a flight.
  - Includes fields like `first_name` and a ForeignKey relationship with `Flight`.

#### **Serializers**
- Used to serialize/deserialize model instances into JSON format.
- **FlightSerializer**:
  - Includes a list of related passengers via the `passengers` field.
- **PassengerSerializer**:
  - Includes a writable `flight` field to associate passengers with flights.

#### **Views/ViewSets**
- Used DRF’s `ModelViewSet` for CRUD operations.
- **FlightViewSet**:
  - Handles operations on flights.
- **PassengerViewSet**:
  - Handles operations on passengers, with support for filtering by `flight`.

#### **Notable Design Decisions**
1. **Validation**:
   - Enforced flight capacity limits via custom validation in the serializer.
2. **RESTful API Design**:
   - Used standard endpoints (`/api/flights/` and `/api/passengers/`) for clarity.
3. **Scalability**:
   - Added pagination to support large datasets.
