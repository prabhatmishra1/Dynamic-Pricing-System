
Project Overview
This project provides a pricing system with the following main components:

Products: Different types of products (e.g., seasonal products, bulk products) with customizable pricing rules.
Discounts: Discount mechanisms (percentage-based or fixed amount) applied to orders.
Orders: Calculates total prices based on included products and discounts.
The main logic is implemented with OOP principles in a separate dynamic_project.py file and further enhanced with Django models and REST APIs for real-world use.

Features
Dynamic Pricing: Calculate product prices dynamically based on conditions like seasonal discounts or bulk purchases.
Discounts: Apply discounts to orders, either as a percentage or a fixed amount.
REST API: Exposes endpoints for creating products, discounts, and orders with Django REST Framework.
Unit Tests: Test cases to validate product pricing, discount application, and order total calculations.
Project Structure
dynamic_project.py: Contains the core pricing and discount classes with OOP principles.
order app:
models.py: Contains Django models for Products, Discounts, and Orders.
serializers.py: DRF serializers for API representation of Products, Discounts, and Orders.
views.py: API views for managing products, discounts, and orders.
tests.py: Unit tests for models and API endpoints.
requirements.txt: Lists dependencies to install for running the project.
Installation
Clone the Repository:

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

POST /api/products/: Create a basic product.
POST /api/seasonal-products/: Create a seasonal product.
POST /api/bulk-products/: Create a bulk product.
Discounts:

POST /api/percentage-discounts/: Create a percentage discount.
POST /api/fixed-discounts/: Create a fixed amount discount.
Orders:

POST /api/orders/: Create an order with products and an optional discount, returning the total price.