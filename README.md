
## Project Overview
This is Dynamic pricing system:

## Object-oriented programming (OOP)

This is a dynamic pricing system, and I have implemented it using object-oriented programming (OOP) principles. You can check the codebase in the dynamic_project.py file. I have added further implementations using Django models and a REST API. To run the system, install the dependencies from the requirements.txt file, migrate the database, and test the API. The codebase is located in the order app, and I have created test cases that you can run using python manage.py test

## Installation

- Clone the Repository:

bash
Copy code
git clone <repository_url>
cd dynamic-pricing-system
Create a Virtual Environment:

bash
Copy code
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
Install Dependencies:

bash
Copy code
pip install -r requirements.txt
Migrate the Database:

bash
Copy code
python manage.py migrate
Usage
Running the Project
Start the Django Development Server:

bash
Copy code
python manage.py runserver
Access the API Documentation (optional):

If you have Django REST Framework’s built-in browsable API enabled, you can access the documentation at http://127.0.0.1:8000/api/.
API Endpoints
Products:

- POST /api/products/: Create a basic product.
- POST /api/seasonal-products/: Create a seasonal product.
- POST /api/bulk-products/: Create a bulk product.
Discounts:

- POST /api/percentage-discounts/: Create a percentage discount.
- POST /api/fixed-discounts/: Create a fixed amount discount.
- Orders:

- POST /api/orders/: Create an order with products and an optional discount, returning the total price.
