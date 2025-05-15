# Simple Store – Django E-commerce App

A modern, responsive e-commerce web application built with Django. This project demonstrates a clean frontend, session-based cart, and dummy product data, making it perfect for learning, portfolio, or as a starting point for a real store.

## Features

- 🛒 **Product Listing**: Browse a grid of stylish products with images, descriptions, and prices.
- 📄 **Product Detail**: View detailed information for each product.
- ➕ **Add to Cart**: Add products to your cart from the list or detail page (session-based, no login required).
- 🛍️ **Cart Summary**: See all items in your cart, quantities, and total price.
- ❌ **Delete from Cart**: Remove individual items from your cart.
- 💎 **Modern UI**: Beautiful, responsive design with Google Fonts, sticky header, and smooth interactions.
- ⚡ **No Database Setup Needed**: Uses hardcoded dummy data for products.

## Functions & Views

- `product_list`: Shows all products on the home page.
- `product_detail`: Shows details for a single product.
- `add_to_cart`: Adds a product to the cart (POST only).
- `cart_summary`: Displays all cart items and the total.
- `remove_from_cart`: Removes a product from the cart (POST only).

## Project Structure

```
simple_store/         # Django project settings
shop/                 # Main app with views, templates, static files
  ├── templates/shop/ # HTML templates
  └── static/images/  # Product images
manage.py             # Django management script
requirements.txt      # Python dependencies
README.md             # This file
```

## Setup & Run Locally

1. **Clone the repo:**
   ```bash
   git clone https://github.com/YOUR-USERNAME/eecomerce-django.git
   cd eecomerce-django
   ```
2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run migrations:**
   ```bash
   python manage.py migrate
   ```
5. **Run the server:**
   ```bash
   python manage.py runserver
   ```
6. **Open in your browser:**
   [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

7. **(Optional) Add product images:**
   Place images named `tshirt.jpg`, `jeans.jpg`, `sneakers.jpg`, `jacket.jpg` in `shop/static/images/` for best results.

## Customization
- Add more products by editing the `PRODUCTS` list in `shop/views.py`.
- Enhance the UI or add new features as needed!

![Screenshot 2025-05-15 125342](https://github.com/user-attachments/assets/f9b91c3f-d953-4524-a64f-339867c80dae)
![Screenshot 2025-05-15 125337](https://github.com/user-attachments/assets/c1a1d677-4554-43ea-b9e8-b188c6643b2c)
![Screenshot 2025-05-15 125333](https://github.com/user-attachments/assets/670b0e37-ac5e-4d83-9d22-101ddea9f540)

