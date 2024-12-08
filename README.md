# Library System
Library system made using Django,Django-Rest and PostgreSQl

## Features:
JWT User authentication

Hashed Passwords

User- Add, view, update, and delete

Books-Add, view, update, and delete books

## Functionality

### api/books
 GET-The list of books is visible to anyone

 POST- A book can be added only by the admin

### api/books/id
  GET- The details of the book can only be viewd if the user is authenticated
 
  PATCH | PUT | DELETE- Can only be done by admin

### api/auth/register
  POST-To register User

### api/auth/login
  POST-To login User

### api/users
  GET | POST - Can only be viewed and added by the admin

### api/users/username 
GET | PATCH | PUT | DELETE- The admin and the user with the username have permissions to view their details, modify them, and delete

