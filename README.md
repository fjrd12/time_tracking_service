# Time Tracking Microservice

## Overview

The Time Tracking Microservice is a Flask-based application that helps users track the time they spend on various tasks. The application supports user, task, and category entities. Each user can perform multiple tasks, and each task can belong to multiple categories. However, a task can only exist once within a category for a given user. The microservice also provides RESTful endpoints for time tracking and reporting.

## Key Features

- Create, read, update, and delete users, tasks, and categories.
- Track time spent on tasks.
- Detailed records of time spent by user.

## Installation

### Prerequisites (ref: requirements.txt file)

- Python 3.10+
- Flask
- Flask-Admin
- Flask-Migrate
- Flask-Restx
- SQLite (for local development)

### Steps

1. Clone the repository:
    ```sh
    git clone <this repository>
    cd timetracking_ms
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Database Initialization

1. Initialize the database:
    ```sh
    flask db init
    ```

2. Generate the initial migration:
    ```sh
    flask db migrate -m "Initial migration."
    ```

3. Apply the migration to the database:
    ```sh
    flask db upgrade
    ```

## Running the Application

1. Start the Flask development server:
    ```sh
    flask run
    ```

2. Access the application in your web browser at `http://127.0.0.1:5000` (port can vary according setup).

## Flask-Admin

this microservice has an admin panel to manage mainly the users creation but categories can be also managed from 
this panel.

For accessing to this panel go to this link:
`http://127.0.0.1:5000/admin` (port can vary according setup).

Before testing the API services a user creation it's need it.

## API Swagger documentation

This microservice counts with Swagger API Documentation, for understanding and demo purposes.

For visualizing the swagger API documentation please go to this link:
`http://127.0.0.1:5000/api_doc/` (port can vary according setup).

## RESTful API Endpoints

### User Endpoints

- **Get all users:**
  - `GET /api/users/`

- **Get user task summary for the current month:**
  - `GET /api/users/<int:user_id>/summary`

- **Get all user records:**
  - `GET /api/users/<int:user_id>/records`

### Task Endpoints

- **Create or update a task for a user:**
  - `POST /api/user/<int:user_id>/tasks`
  - Request body:
    ```json
    {
      "name": "Task Name",
      "category_id": 1
    }
    ```

### Category Endpoints

- **Get all categories:**
  - `GET /api/categories/`

- **Create a new category:**
  - `POST /api/categories/`
  - Request body:
    ```json
    {
      "name": "Category Name"
    }
    ```

## Contributing

We welcome contributions! Please fork the repository and submit pull requests.

# License

MIT License

Copyright (c) 2024 Andres A. Reyes

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


---

Happy time tracking!