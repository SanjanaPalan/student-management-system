# Student Management System

## Overview

Student Management System is a web-based application developed to manage student records efficiently.

The system allows administrators to:

- Add student records
- View student details
- Filter students by department
- Filter students by semester
- Monitor attendance information
- Delete student records

The project was developed as a prototype during a hackathon to demonstrate student data management in an educational institution.

---

## Features

### Dashboard

- Total Students Count
- Average Attendance Percentage

### Student Management

- Add New Student
- View Student Records
- Delete Student Records

### Department Management

- Computer Science (CSE)
- Artificial Intelligence & Machine Learning (AIML)
- Electronics & Communication Engineering (ECE)
- Mechanical Engineering (MECH)
- Civil Engineering (CIVIL)

### Semester Filtering

- Semester 1 to Semester 8

### Attendance Tracking

- Store and display attendance percentage for each student

---

## Technologies Used

### Frontend

- HTML
- CSS

### Backend

- Python
- Flask

### Database

- SQLite

### Tools

- VS Code
- Git
- GitHub

---

## Project Structure

```text
student-management-system/

├── app.py
├── students.db
│
├── templates/
│   ├── index.html
│   └── add_student.html
│
├── static/
│   └── style.css
│
└── README.md
```

---

## Database Schema

```sql
CREATE TABLE students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    department TEXT,
    semester TEXT,
    email TEXT,
    attendance INTEGER
);
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/student-management-system.git
```

### Navigate to Project Folder

```bash
cd student-management-system
```

### Install Flask

```bash
py -m pip install flask
```

### Run Application

```bash
py app.py
```

### Open Browser

```text
http://127.0.0.1:5000
```

---

## Future Enhancements

- Student Login System
- Faculty Login System
- Attendance Management Module
- Marks and Result Management
- Student Search and Sorting
- Export Reports to Excel
- Role-Based Access Control

---

## Learning Outcomes

- Flask Web Development
- SQLite Database Integration
- CRUD Operations
- HTML & CSS Frontend Development
- Git and GitHub Version Control

---

## Author

Sanjana S Palan
