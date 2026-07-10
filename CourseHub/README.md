# Course Management Backend API

A backend REST API built with **FastAPI** and **MongoDB** that manages users, courses, enrollments, and reviews. The project demonstrates CRUD operations, server-side validation, and MongoDB Aggregation Framework features such as `$lookup`, `$group`, and `$facet`.

---

## Tech Stack

- Python 3
- FastAPI
- MongoDB
- PyMongo
- Pydantic
- Uvicorn

---

## Project Structure

```
app/
│
├── core/
│   ├── config.py
│   └── db.py
│
├── routers/
│   ├── users.py
│   ├── courses.py
│   ├── enrollments.py
│   ├── reviews.py
│   └── analytics.py
│
├── schemas/
│   ├── user.py
│   ├── course.py
│   ├── enrollment.py
│   └── review.py
│
├── services/
│   ├── user_service.py
│   ├── course_service.py
│   ├── enrollment_service.py
│   ├── review_service.py
│   └── analytics_service.py
│
├── utils/
│   └── helpers.py
│
└── main.py
```

---

## Features

### Users

- Create User
- Get All Users
- Get User by ID
- Update User
- Delete User

---

### Courses

- Create Course
- Get All Courses
- Get Course by ID
- Update Course
- Delete Course

---

### Enrollments

- Student Enrollment
- Duplicate Enrollment Prevention
- Student Validation
- Course Validation

---

### Reviews

- Add Review
- One Review per Student per Course
- Enrollment Validation
- Rating Validation (1–5)

---

## MongoDB Collections

### users

```json
{
    "_id": ObjectId,
    "name": "Adarsh",
    "email": "adarsh@example.com",
    "role": "student"
}
```

### courses

```json
{
    "_id": ObjectId,
    "title": "MongoDB Masterclass",
    "description": "...",
    "price": 2999,
    "instructorId": "..."
}
```

### enrollments

```json
{
    "_id": ObjectId,
    "userId": "...",
    "courseId": "..."
}
```

### reviews

```json
{
    "_id": ObjectId,
    "userId": "...",
    "courseId": "...",
    "rating": 5,
    "comment": "Excellent course!"
}
```

---

## Aggregation APIs

### 1. Enrollment Analytics

**Endpoint**

```
GET /analytics/enrollments
```

Uses:

- `$addFields`
- `$toObjectId`
- `$lookup`
- `$unwind`
- `$project`

Returns:

```json
[
    {
        "studentName": "Adarsh",
        "studentEmail": "adarsh@example.com",
        "courseTitle": "MongoDB Masterclass",
        "price": 2999
    }
]
```

---

### 2. Course Analytics

**Endpoint**

```
GET /analytics/courses
```

Uses:

- `$group`
- `$sum`
- `$lookup`
- `$project`

Returns:

```json
[
    {
        "courseTitle": "MongoDB Masterclass",
        "price": 2999,
        "totalEnrollments": 12
    }
]
```

---

### 3. Dashboard Analytics

**Endpoint**

```
GET /analytics/dashboard
```

Uses:

- `$facet`

Returns:

```json
{
    "totalUsers": 15,
    "totalCourses": 5,
    "totalEnrollments": 24,
    "recentEnrollments": [
        ...
    ]
}
```

---

## Validation

The project uses **Pydantic** for request validation.

Examples:

- Email validation
- ObjectId validation
- Rating validation
- Role validation
- Required fields
- String length validation

---

## Business Rules

- Email must be unique.
- Only students can enroll in courses.
- A student cannot enroll in the same course twice.
- A student can review a course only after enrollment.
- Only one review is allowed per student per course.

---

## Running the Project

### Clone

```bash
git clone <repository-url>
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Create `.env`

```
MONGODB_URL=<your_mongodb_connection_string>
DATABASE_NAME=<your_database_name>
```

### Start Server

```bash
uvicorn app.main:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

---

## Learning Outcomes

This project demonstrates:

- FastAPI REST API development
- Layered architecture (Router → Service → Database)
- MongoDB CRUD operations
- Schema validation with Pydantic
- MongoDB Aggregation Framework
- Collection relationships using `$lookup`
- Data grouping with `$group`
- Dashboard generation using `$facet`

---

## Future Improvements

- JWT Authentication
- Role-based Authorization
- Pagination
- Search & Filtering
- Vector Search
- Docker Support
- Unit Testing
- CI/CD Pipeline

---

## Author

**Adarsh Mishra**