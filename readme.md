# Personal Library Management API Documentation

## Overview

The Personal Library Management API is a RESTful API developed using Django and Django REST Framework. It is designed to manage a personal library system, allowing users to perform CRUD operations on their book collection. Each book entry contains information such as title, authors, publication date, ISBN, and a short description.



## Models

### Book
- Title: CharField, required
- Authors: CharField, required
- Publication Date: DateField, optional
- ISBN: CharField, required, unique
- Description: TextField, optional

## API Endpoints

### List Books
- Method: GET
- Endpoint: `/api/books/`
- Description: Returns a list of all books in the library.

### Add Book
- Method: POST
- Endpoint: `/api/books/`
- Description: Allows adding a new book to the library. All book details must be provided, except for the optional ones.

### Book Details
- Method: GET
- Endpoint: `/api/books/<isbn>/`
- Description: Retrieves the details of a book identified by its ISBN.

### Update Book
- Method: PUT
- Endpoint: `/api/books/<isbn>/`
- Description: Updates the details of a specific book. All book details must be provided, as this is a complete update.

### Delete Book
- Method: DELETE
- Endpoint: `/api/books/<isbn>/`
- Description: Deletes a specific book from the library.

## Implementation

### Setting Up the Project Locally

1. **Clone the Repository**: 

``` 
git clone <repository_url> 
```
2. **Install Dependencies**: 
```
pip install -r requirements.txt

```
3. **Migrate Database**: 
```
python manage.py migrate

```
4. **Run Server**: 
```
python manage.py runserver
```




## Testing the API Locally

You can test the API endpoints using tools like `curl`, Postman, or any other REST client.

#### Example CURL Commands:

1. List Books:
```
curl http://localhost:8000/api/books/
```

2. Add Book:
```
curl -X POST http://localhost:8000/api/books/ -H "Content-Type: application/json" -d "{\"title\": \"New Book\", \"authors\": \"New Author\", \"isbn\": \"9876543210987\"}"
```

3. Retrieve Book Details:
```
curl http://localhost:8000/api/books/9876543210987/
```

4. Update Book:
```
curl -X PUT http://localhost:8000/api/books/9876543210987/ -H "Content-Type: application/json" -d "{\"title\": \"Updated Title\", \"authors\": \"Updated Author\", \"isbn\": \"9876543210987\"}"
```

5. Delete Book:

```
curl -X DELETE http://localhost:8000/api/books/9876543210987/
```



