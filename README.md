# Library System
Library system made using Django,Django-Rest and PostgreSQL to manage books and users while protecting sensitive information and endpoints

## Features:
- JWT User authentication
- Hashed Passwords
- User- Add, view, update, and delete
- Books-Add, view, update, and delete books

## Functionality

#### api/books
 GET-The list of books is visible to anyone

 POST- A book can be added only by the admin

#### api/books/id
  GET- The details of the book can only be viewd if the user is authenticated
 
  PATCH | PUT | DELETE- Can only be done by admin

#### api/auth/register
  POST-To register User

#### api/auth/login
  POST-To login User

#### api/users
  GET | POST - Can only be viewed and added by the admin

#### api/users/username 
GET | PATCH | PUT | DELETE- The admin and the user with the username have permissions to view their details, modify them, and delete

## Backend Hosted URL
The backend is hosted on render at 
#### https://library-system-6.onrender.com


## To run the library system:

#### 1. Clone the repository:
   `git clone "https://github.com/thomasjames433/Library-system.git"`
#### 2. Navigate into the project directory:
   `cd Library-system`
#### 3. Install dependencies:
   - `python manage.py makemigrations`
   - `python manage.py migrate`  
   - `To createsuperuser: python manage.py createsuperuser`
#### 4. Run the system:
   `python manage.py runserver`

## Technologies Used
- Django
- Django-Rest-Framework
- JWT for Authentication
- PostgreSQL

## LICENSE
[MIT License](LICENSE)

