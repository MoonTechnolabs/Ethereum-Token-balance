# Django and React Authentication with JWT and HTTP-Only Cookies

This project implements a user authentication system using Django and React. It includes user registration, login, logout, and fetching user data. Authentication is handled using JWT (JSON Web Tokens) and HTTP-only cookies for improved security. The application's frontend is styled using Bootstrap.

The project consists of two directories: 

- `client`: Contains the React application
- `server`: Contains the Django backend

## Installation

To run this project on your local machine, follow the steps below:

### Prerequisites

Ensure you have the following installed on your local machine:

- Python 3.8 or higher
- Node.js v14.15.0 or higher
- npm 6.14.9 or higher

### Setup
Steps to Run the Django Project

1. Create a Virtual Environment:
    Ensure you have Python 3.8 or above installed.
    Create and activate a virtual environment:
        python3 -m venv env
        source env/bin/activate

2. Navigate to the Server Directory:
    cd server

3. Install Dependencies:
    pip install -r requirements.txt

4. Check the Django Project:
    python manage.py check

5. Make Migrations:
    python manage.py makemigrations

6. Apply Migrations:
    python manage.py migrate

7. Create a Superuser:
    python manage.py createsuperuser

8. Run the Django Development Server:
    python manage.py runserver


Steps to Run the React.js Project

1. Navigate to the Client Directory:
    cd client

2. Install Dependencies:
    npm install

3. Run the React Development Server:
    npm start

Now, your application should be running at `localhost:3000`.

Note:
- The Django server should be running at the same time as the React application for the system to function properly.
- The application uses the email field instead of the username field for user identification.


## Task
1. Add an input field for the user's Ethereum wallet address to the registration page. When a user registers an account, this wallet address must be saved to the database.
2. After login, the homepage must show the balance of the user's Ethereum wallet address.