import sys
from datetime import datetime
import database as db


def display_products():
    """Display all products with price and stock."""
    df = db.get_products()
    print("\n" + "=" * 50)
    print(f"{'ID':<4} {'Product Name':<22} {'Price (Rs)':<12} {'Stock':<6}")
    print("-" * 50)
    for _, row in df.iterrows():
        print(f"{row['product_id']:<4} {row['name']:<22} {row['price']:<12} {row['stock']:<6}")
    print("=" * 50)


def add_to_cart(cart, product_name, price, quantity):
    """Add or update an item in the cart."""
    for item in cart:
        if item["name"].lower() == product_name.lower():
            item["quantity"] += quantity
            return
    cart.append({
        "name": product_name,
        "price": price,
        "quantity": quantity
    })


def calculate_total(cart):
    """Calculate subtotal from cart items."""
    return sum(item["price"] * item["quantity"] for item in cart)


def apply_discount(subtotal):
    """Apply 10% discount if subtotal is Rs. 1000 or more."""
    if subtotal >= 1000:
        discount = round(subtotal * 0.10, 2)
        return discount, round(subtotal - discount, 2)
    return 0.0, float(subtotal)


def generate_bill(orders, subtotal, discount, grand_total):
    """Print formatted bill."""
    print("\n" + "=" * 44)
    print("            AL-FATAH SUPER STORE")
    print("                 CASH RECEIPT")
    print("=" * 44)
    print(f"Date: {datetime.now().strftime('%d-%b-%Y %I:%M %p')}")
    print("-" * 44)
    print(f"{'Item':<20} {'Qty':<5} {'Price':<8} {'Total':<8}")
    print("-" * 44)
    for item in orders:
        name = item.get("product_name", item.get("name", "Item"))
        qty = item["quantity"]
        item_total = item.get("total_price", item.get("price", 0) * qty)
        unit_price = item.get("price") or (round(item_total / qty, 2) if qty else 0)
        print(f"{name[:19]:<20} {qty:<5} {unit_price:<8} {item_total:<8}")

    print("-" * 44)
    print(f"Subtotal:       Rs. {subtotal:,.2f}")
    if discount > 0:
        print(f"Discount (10%): -Rs. {discount:,.2f}")
    print(f"Grand Total:    Rs. {grand_total:,.2f}")
    print("=" * 44)
    print("       Thank you for shopping with us!")
    print("=" * 44 + "\n")


def customer_shopping():
    """Customer shopping workflow: select items, check stock, and checkout."""
    df = db.get_products()
    if df.empty:
        print("No products available in the store.")
        return

    cart = []
    display_products()

    while True:
        choice = input("\nEnter product ID or name to add (or 'done' to checkout, 'cancel' to exit): ").strip()
        if choice.lower() == 'done':
            break
        if choice.lower() == 'cancel':
            print("Shopping cancelled.")
            return

        # match by ID or name
        match = df[df["name"].str.lower() == choice.lower()]
        if match.empty and choice.isdigit():
            match = df[df["product_id"] == int(choice)]

        if match.empty:
            print("Product not found. Please check the product list.")
            continue

        product = match.iloc[0]
        prod_name = product["name"]
        prod_price = int(product["price"])
        prod_stock = int(product["stock"])

        try:
            qty = int(input(f"Enter quantity for '{prod_name}' (In stock: {prod_stock}): "))
            if qty <= 0:
                print("Quantity must be greater than 0.")
                continue
            if qty > prod_stock:
                print(f"Sorry, only {prod_stock} units available.")
                continue
        except ValueError:
            print("Invalid input. Quantity must be a number.")
            continue

        add_to_cart(cart, prod_name, prod_price, qty)
        print(f"Added {qty}x '{prod_name}' to cart.")

    if not cart:
        print("Cart is empty.")
        return

    # Review cart and confirm checkout
    subtotal = calculate_total(cart)
    discount, grand_total = apply_discount(subtotal)

    print("\n--- Cart Summary ---")
    for item in cart:
        print(f"{item['name']} x{item['quantity']} = Rs. {item['price'] * item['quantity']}")
    print(f"Subtotal: Rs. {subtotal:,.2f}")
    if discount > 0:
        print(f"10% Discount: -Rs. {discount:,.2f}")
    print(f"Total to Pay: Rs. {grand_total:,.2f}")

    confirm = input("\nProceed with checkout? (y/n): ").strip().lower()
    if confirm == 'y':
        success, result = db.atomic_checkout(cart, channel="physical")
        if success:
            generate_bill(result["orders"], result["subtotal"], result["discount"], result["grand_total"])
        else:
            print(f"Checkout failed: {result}")
    else:
        print("Checkout cancelled.")


def show_sales_analysis():
    """Display sales metrics and best selling product."""
    orders = db.get_orders()
    analysis = db.get_sales_analysis(orders)

    print("\n" + "=" * 44)
    print("             SALES ANALYSIS")
    print("=" * 44)
    print(f"Total Transactions:      {len(orders)}")
    print(f"Total Items Sold:        {analysis['total_items_sold']}")
    print(f"Total Revenue:           Rs. {analysis['total_revenue']:,.2f}")
    print(f"Best-Selling Product:    {analysis['best_selling_product']} ({analysis['best_selling_quantity']} units sold)")
    print("=" * 44)

    if not analysis["product_sales"].empty:
        print("\nTop Products by Sales:")
        for name, qty in analysis["product_sales"].head(5).items():
            print(f"- {name}: {qty} sold")
    print()


def manager_menu():
    """Manager operations for product CRUD."""
    while True:
        print("\n--- Manager Inventory Controls ---")
        print("1. View Products")
        print("2. Add New Product")
        print("3. Update Price and Stock")
        print("4. Delete Product")
        print("5. Check Low Stock Items")
        print("6. Back to Main Menu")

        choice = input("Enter choice (1-6): ").strip()

        if choice == '1':
            display_products()
        elif choice == '2':
            name = input("Enter product name: ").strip()
            category = input("Enter category (Grocery/Dairy/Snacks/etc): ").strip()
            try:
                price = int(input("Enter price (PKR): "))
                stock = int(input("Enter initial stock: "))
                if price <= 0 or stock < 0:
                    print("Price must be positive and stock cannot be negative.")
                    continue
                db.add_product(name, category, price, stock)
                print(f"Product '{name}' added successfully.")
            except ValueError:
                print("Price and stock must be numbers.")
        elif choice == '3':
            name = input("Enter exact product name to update: ").strip()
            try:
                new_price = int(input("Enter new price: "))
                new_stock = int(input("Enter new stock: "))
                db.update_product(name, new_price, new_stock)
                print(f"Updated '{name}' successfully.")
            except ValueError:
                print("Price and stock must be numbers.")
        elif choice == '4':
            name = input("Enter product name to delete: ").strip()
            db.delete_product(name)
            print(f"Product '{name}' deleted.")
        elif choice == '5':
            low = db.get_low_stock(10)
            if low.empty:
                print("All items have healthy stock levels (>= 10 units).")
            else:
                print("\nLow stock items:")
                for _, r in low.iterrows():
                    print(f"- {r['name']}: {r['stock']} units remaining")
        elif choice == '6':
            break
        else:
            print("Invalid option. Please enter 1-6.")


def main():
    """Main application loop."""
    while True:
        print("\n" + "=" * 44)
        print("    AL-FATAH SUPERMARKET MANAGEMENT SYSTEM")
        print("=" * 44)
        print("1. View Products")
        print("2. Shop / New Bill (Customer & POS)")
        print("3. Sales Analysis & Reports")
        print("4. Manager Inventory Controls (CRUD)")
        print("5. Exit")
        print("=" * 44)

        choice = input("Select an option (1-5): ").strip()

        if choice == '1':
            display_products()
        elif choice == '2':
            customer_shopping()
        elif choice == '3':
            show_sales_analysis()
        elif choice == '4':
            manager_menu()
        elif choice == '5':
            print("\nThank you for using Al-Fatah System. Goodbye!")
            sys.exit(0)
        else:
            print("Invalid input. Please choose a valid option between 1 and 5.")


if __name__ == "__main__":
    main()
