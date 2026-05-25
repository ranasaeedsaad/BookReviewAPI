# Book Review API

## Project Description

Book Review API is a RESTful API built using Django REST Framework.

The system allows users to:
- Register a new account
- Log in and obtain a JWT access token
- Browse books
- View details of a specific book
- Add reviews to books
- View reviews for a specific book
- Edit or delete their own reviews
- Change their password

Admin users can create, update, and delete books.

---

## Technologies Used

- Python 3
- Django 4+
- Django REST Framework
- djangorestframework-simplejwt
- SQLite3
- Postman

---

## Models

### Book

The Book model stores book information.

Fields:
- title
- author
- description

### Review

The Review model stores user reviews for books.

Fields:
- book
- user
- rating
- comment
- created_at

The project uses Django's default User model for authentication.

---

## Authentication

This project uses JWT Authentication.

Users log in through:

```http
POST /api/token/
```

After login, the system returns:

- access token
- refresh token

The access token is used in protected endpoints using Bearer Token authentication.

Example header:

```http
Authorization: Bearer <access_token>
```

---

## API Endpoints

### Authentication

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/register/` | Register a new user |
| POST | `/api/token/` | Log in and obtain JWT |
| POST | `/api/token/refresh/` | Refresh JWT access token |
| POST | `/api/change-password/` | Change user password |

### Book Management

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/books/` | List all books |
| GET | `/api/books/<id>/` | Retrieve book details |
| POST | `/api/books/` | Add a new book |
| PUT | `/api/books/<id>/` | Edit a book |
| DELETE | `/api/books/<id>/` | Delete a book |

### Review Management

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/books/<book_id>/reviews/` | Add a review to a book |
| GET | `/api/books/<book_id>/reviews/` | Get all reviews for a specific book |
| PUT | `/api/reviews/<id>/` | Edit a review |
| DELETE | `/api/reviews/<id>/` | Delete a review |

---

## Permissions

- Only authenticated users can add reviews.
- Users can only edit or delete their own reviews.
- Admin users can create, update, and delete books.

---

## How to Run the Project Locally

### 1. Install required packages

```bash
pip install django
pip install djangorestframework
pip install djangorestframework-simplejwt
```

### 2. Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 3. Create a superuser

```bash
python manage.py createsuperuser
```

### 4. Run the server

```bash
python manage.py runserver
```

The server will run at:

```http
http://127.0.0.1:8000/
```

---

## How to Test the Endpoints Using Postman

### Register User

```http
POST /api/register/
```

Body:

```json
{
  "username": "user1",
  "email": "user1@gmail.com",
  "password": "User12345"
}
```

### Login and Get Token

```http
POST /api/token/
```

Body:

```json
{
  "username": "user1",
  "password": "User12345"
}
```

Copy the access token and use it in Postman:

Authorization → Bearer Token

### Refresh Token

```http
POST /api/token/refresh/
```

Body:

```json
{
  "refresh": "your_refresh_token"
}
```

### Change Password

```http
POST /api/change-password/
```

Body:

```json
{
  "old_password": "User12345",
  "new_password": "Newpass123"
}
```

### List Books

```http
GET /api/books/
```

### Book Details

```http
GET /api/books/1/
```

### Add Review to a Book

```http
POST /api/books/1/reviews/
```

Body:

```json
{
  "rating": 5,
  "comment": "Great book"
}
```

### Get Reviews for a Book

```http
GET /api/books/1/reviews/
```

### Update Review

```http
PUT /api/reviews/1/
```

Body:

```json
{
  "rating": 4,
  "comment": "Updated review"
}
```

### Delete Review

```http
DELETE /api/reviews/1/
```

---

## Testing

All required endpoints were tested using Postman.
