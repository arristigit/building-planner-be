# **Building Planner API**

This repository contains the backend API for the Building Planner web application. It provides endpoints for saving, loading, and managing drawing data. The backend is built using **Django** and **Django Rest Framework (DRF)**.

## **Features**
- Save drawings created in the frontend.
- Load saved drawings by ID.
- List all saved drawings.
- Integrate with a React frontend built with Vite.

## **Tech Stack**
- **Backend**: Django, Django Rest Framework
- **Database**: SQLite (or any preferred database like PostgreSQL, MySQL)
- **API Format**: JSON

## **Getting Started**

### **1. Prerequisites**
Make sure you have the following installed on your machine:
- [Python](https://www.python.org/) (v3.7 or higher)
- `pip`

### **2. Installation**

1. Clone the repository:

   ```bash
   https://github.com/arristigit/building-planner-be
   ```
2. Navigate into the project directory:

   ```bash
   cd building-planner-be
   ```
3. Install dependencies:
   ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
   ```
4. Apply the database migrations:
   ```bash
   python manage.py migrate
   ```
### **3. Running the Server**
Start the Django development server:
   ```bash
   python manage.py runserver
   ```
   The API will be accessible at http://localhost:8000.

### **4. API Endpoints**
Here are the key API endpoints available for interacting with the application:

 - POST` trackdraw/api/drawings/` — Save a new drawing.
 - GET `trackdraw/api/drawings/` — Fetch all saved drawings.
 - GET `trackdraw/api/drawings/<id>/` — Fetch a single drawing by ID.
