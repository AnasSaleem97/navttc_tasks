# Al-Fatah Super Store Management System

A Python project for managing a mini supermarket store with inventory tracking, billing, 10% discount on orders of Rs. 1,000 or more, and basic sales analysis.

It includes both a command-line interface (`main.py`) and an interactive web dashboard (`app.py`) built with Streamlit. Both share the same CSV database files stored in the `data/` folder.

---

## Project Structure

```text
AlFatah_Retail_Store/
│
├── main.py             # Console / Terminal interface
├── app.py              # Streamlit Web UI and Dashboard
├── database.py         # CSV file operations & calculations
├── README.md           # Documentation
│
└── data/
    ├── products.csv    # Product catalog with price & stock
    └── orders.csv      # Order transaction records
```

---

## Features

1. **Product Catalog**: Lists all available products, categories, unit prices, and stock quantities.
2. **Shopping Cart & Checkout**:
   - Add items and quantities to cart.
   - Calculates subtotal.
   - Automatically applies a **10% discount** when the total is Rs. 1,000 or more.
   - Generates an itemized bill receipt.
3. **Inventory Management (CRUD)**:
   - Add new products.
   - Update price and stock.
   - Delete products.
   - Stock deduction after each checkout.
   - Low stock warning if quantity falls below 10.
4. **Sales Analysis & Reports**:
   - Calculates total items sold and total sales revenue.
   - Identifies the best-selling product.
   - Visual charts for sales and inventory in the Streamlit dashboard.

---

## How to Run

### 1. Requirements
Make sure Python is installed with `pandas` and `streamlit`:
```bash
pip install pandas streamlit
```

### 2. Run the Console / Terminal Version
From the project folder, run:
```bash
python main.py
```

### 3. Run the Streamlit Web App
To open the web interface in your browser:
```bash
streamlit run app.py
```
