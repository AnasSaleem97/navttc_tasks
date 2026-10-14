import os
from datetime import datetime
import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PRODUCTS_FILE = os.path.join(BASE_DIR, "data", "products.csv")
ORDERS_FILE = os.path.join(BASE_DIR, "data", "orders.csv")


def get_products():
    """Load all products from CSV file."""
    return pd.read_csv(PRODUCTS_FILE)


def get_orders():
    """Load orders from CSV or return empty DataFrame if file doesn't exist."""
    try:
        return pd.read_csv(ORDERS_FILE)
    except (FileNotFoundError, pd.errors.EmptyDataError):
        return pd.DataFrame(columns=["order_id", "product_name", "quantity", "total_price", "date", "channel"])


# Product CRUD operations
def add_product(name, category, price, stock):
    df = get_products()
    new_id = int(df["product_id"].max() + 1) if not df.empty else 1
    new_row = {
        "product_id": new_id,
        "name": name.strip(),
        "category": category,
        "price": int(price),
        "stock": int(stock)
    }
    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    df.to_csv(PRODUCTS_FILE, index=False)


def update_product(product_name, new_price, new_stock):
    df = get_products()
    df.loc[df["name"] == product_name, ["price", "stock"]] = [int(new_price), int(new_stock)]
    df.to_csv(PRODUCTS_FILE, index=False)


def delete_product(product_name):
    df = get_products()
    df = df[df["name"] != product_name]
    df.to_csv(PRODUCTS_FILE, index=False)


def get_low_stock(threshold=10):
    df = get_products()
    return df[df["stock"] < threshold]


# Calculate total, discount (10% if Rs 1000 or more), and net amount
def calculate_cart_totals(cart):
    subtotal = sum(item["price"] * item["quantity"] for item in cart)
    discount = round(subtotal * 0.10, 2) if subtotal >= 1000 else 0.0
    grand_total = round(subtotal - discount, 2)
    return subtotal, discount, grand_total


def atomic_checkout(cart, channel):
    """
    Validates stock, updates product inventory, and saves transaction.
    If any item is out of stock, cancels the whole checkout.
    """
    if not cart:
        return False, "Cart is empty."

    df_products = get_products()

    # check stock for all cart items first
    for item in cart:
        match = df_products[df_products["name"] == item["name"]]
        if match.empty:
            return False, f"Product '{item['name']}' not found in inventory."

        available_stock = int(match.iloc[0]["stock"])
        if item["quantity"] > available_stock:
            return False, f"Not enough stock for '{item['name']}' (Only {available_stock} available)."

    # calculate totals and apply 10% discount if subtotal >= 1000
    subtotal, discount, grand_total = calculate_cart_totals(cart)
    discount_factor = (grand_total / subtotal) if subtotal > 0 else 1.0

    df_orders = get_orders()
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    start_id = len(df_orders) + 1
    new_orders = []

    # deduct stock and prepare order records
    for i, item in enumerate(cart):
        idx = df_products[df_products["name"] == item["name"]].index[0]
        df_products.loc[idx, "stock"] -= item["quantity"]

        item_total = round(item["price"] * item["quantity"] * discount_factor, 2)
        new_orders.append({
            "order_id": start_id + i,
            "product_name": item["name"],
            "quantity": item["quantity"],
            "total_price": item_total,
            "date": now_str,
            "channel": channel
        })

    # save changes to CSV files
    df_products.to_csv(PRODUCTS_FILE, index=False)
    updated_orders = pd.concat([df_orders, pd.DataFrame(new_orders)], ignore_index=True)
    updated_orders.to_csv(ORDERS_FILE, index=False)

    return True, {
        "orders": new_orders,
        "subtotal": subtotal,
        "discount": discount,
        "grand_total": grand_total
    }


def get_sales_analysis(filtered_orders=None):
    """Calculates total items sold, total sales revenue, and top selling item."""
    df = filtered_orders if filtered_orders is not None else get_orders()
    if df.empty:
        return {
            "total_items_sold": 0,
            "total_revenue": 0.0,
            "best_selling_product": "N/A",
            "best_selling_quantity": 0,
            "product_sales": pd.Series(dtype=int)
        }

    total_items = int(df["quantity"].sum())
    total_revenue = round(float(df["total_price"].sum()), 2)
    sales_by_item = df.groupby("product_name")["quantity"].sum().sort_values(ascending=False)
    best_item = sales_by_item.index[0] if not sales_by_item.empty else "N/A"
    best_qty = int(sales_by_item.iloc[0]) if not sales_by_item.empty else 0

    return {
        "total_items_sold": total_items,
        "total_revenue": total_revenue,
        "best_selling_product": best_item,
        "best_selling_quantity": best_qty,
        "product_sales": sales_by_item
    }