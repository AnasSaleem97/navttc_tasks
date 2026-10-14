import streamlit as st
import pandas as pd
from datetime import datetime

import database as db

# Page setup
st.set_page_config(page_title="Al-Fatah Super Store", layout="wide")


# Helper functions
def display_products(df):
    """Display product table with relevant fields."""
    st.dataframe(
        df[["name", "category", "price", "stock"]],
        use_container_width=True,
        hide_index=True
    )


def add_to_cart(cart_key, product_name, price, quantity):
    """Add a product or increment quantity in the cart."""
    if cart_key not in st.session_state:
        st.session_state[cart_key] = []

    for item in st.session_state[cart_key]:
        if item["name"] == product_name:
            item["quantity"] += quantity
            return

    st.session_state[cart_key].append({
        "name": product_name,
        "price": int(price),
        "quantity": int(quantity)
    })


def calculate_total(cart):
    """Calculate subtotal for cart items."""
    return sum(item["price"] * item["quantity"] for item in cart)


def apply_discount(subtotal):
    """Apply 10% discount if the bill is Rs. 1000 or more."""
    if subtotal >= 1000:
        discount = round(subtotal * 0.10, 2)
        return discount, round(subtotal - discount, 2)
    return 0.0, float(subtotal)


def generate_bill(orders, subtotal, discount, grand_total, channel="Counter"):
    """Format and return a printable text receipt."""
    bill = [
        "========================================",
        "         AL-FATAH SUPER STORE",
        "             SALES BILL",
        "========================================",
        f"Date:    {datetime.now().strftime('%d-%b-%Y %I:%M %p')}",
        f"Channel: {channel}",
        "----------------------------------------",
        f"{'Item':<20} {'Qty':<4} {'Total'}",
        "----------------------------------------"
    ]
    for item in orders:
        name = item.get("product_name", item.get("name", "Item"))
        qty = item["quantity"]
        total = item.get("total_price", item.get("price", 0) * qty)
        bill.append(f"{name[:19]:<20} x{qty:<3} Rs. {total:,.2f}")

    bill.append("----------------------------------------")
    bill.append(f"Subtotal:        Rs. {subtotal:,.2f}")
    if discount > 0:
        bill.append(f"Discount (10%): -Rs. {discount:,.2f}")
    bill.append(f"Grand Total:     Rs. {grand_total:,.2f}")
    bill.append("========================================")
    bill.append("        Thank you for your visit!")
    bill.append("========================================")
    return "\n".join(bill)


def show_low_stock_banner(threshold=10):
    """Show alert if any item is running out of stock."""
    low_stock = db.get_low_stock(threshold)
    if not low_stock.empty:
        items_str = ", ".join([f"{r['name']} ({r['stock']} left)" for _, r in low_stock.iterrows()])
        st.warning(f"Low Stock Warning (< {threshold} units): {items_str}")


def render_cart(cart_key, channel_label):
    """Render items currently in cart, show discount calculation, and handle checkout."""
    cart = st.session_state.get(cart_key, [])
    st.subheader(f"Current Cart ({len(cart)} items)")

    if not cart:
        st.info("Cart is currently empty.")
        return None

    cart_df = pd.DataFrame(cart)
    cart_df["Total (PKR)"] = cart_df["price"] * cart_df["quantity"]
    st.dataframe(cart_df[["name", "price", "quantity", "Total (PKR)"]], use_container_width=True, hide_index=True)

    subtotal = calculate_total(cart)
    discount, grand_total = apply_discount(subtotal)

    col1, col2, col3 = st.columns(3)
    col1.metric("Subtotal", f"Rs. {subtotal:,.2f}")
    if discount > 0:
        col2.metric("Discount (10%)", f"-Rs. {discount:,.2f}")
        st.success(f"10% discount applied for bill of Rs. 1,000 or more! Saved: Rs. {discount:,.2f}")
    else:
        col2.metric("Discount (10%)", "Rs. 0.00")
        diff = 1000 - subtotal
        st.info(f"Add Rs. {diff:,.2f} more to qualify for 10% discount.")

    col3.metric("Grand Total", f"Rs. {grand_total:,.2f}")

    c1, c2 = st.columns([2, 1])
    with c1:
        if st.button(f"Complete {channel_label} Checkout", type="primary", use_container_width=True):
            success, result = db.atomic_checkout(cart, channel=channel_label.lower())
            if success:
                st.session_state[cart_key] = []
                return result
            else:
                st.error(result)

    with c2:
        if st.button("Clear Cart", use_container_width=True):
            st.session_state[cart_key] = []
            st.rerun()

    return None


# Page 1: Home
def page_home():
    st.title("Welcome to Al-Fatah Super Store")
    role = st.session_state["role"]
    st.write(f"Logged in as: **{role}**")

    if role == "Customer":
        st.info("Browse our grocery catalog and order online.")
        if st.button("Shop Online", type="primary"):
            st.session_state["nav_selection"] = "Shop Online"
            st.rerun()
    elif role == "Cashier":
        st.info("Point-of-Sale counter ready for in-store billing and receipts.")
        if st.button("Open POS Billing", type="primary"):
            st.session_state["nav_selection"] = "Physical Billing"
            st.rerun()
    else:
        st.info("Admin Portal: Manage inventory stock, view orders, and sales reports.")
        c1, c2 = st.columns(2)
        with c1:
            if st.button("Manage Products", use_container_width=True):
                st.session_state["nav_selection"] = "Products"
                st.rerun()
        with c2:
            if st.button("View Orders & Analytics", use_container_width=True):
                st.session_state["nav_selection"] = "Orders & Analytics"
                st.rerun()


# Page 2: Products Catalog & Management
def page_products():
    st.title("Product Catalog")
    show_low_stock_banner()

    df = db.get_products()
    display_products(df)

    if st.session_state["role"] != "Admin":
        st.info("Read-Only View: Switch role to Admin in the sidebar to add, edit, or delete items.")
        return

    st.subheader("Manage Inventory")
    tab_add, tab_edit, tab_del = st.tabs(["Add Product", "Update Price & Stock", "Delete Product"])

    with tab_add:
        with st.form("form_add", clear_on_submit=True):
            name = st.text_input("Product Name")
            category = st.selectbox("Category", ["Grocery", "Dairy", "Bakery", "Snacks", "Beverages", "Detergent", "Personal Care", "Frozen Foods"])
            price = st.number_input("Price (PKR)", min_value=1, step=10, value=100)
            stock = st.number_input("Stock Quantity", min_value=1, step=5, value=20)
            if st.form_submit_button("Save Product"):
                if name.strip():
                    db.add_product(name, category, price, stock)
                    st.success(f"Product '{name}' added successfully.")
                    st.rerun()
                else:
                    st.warning("Please enter a valid product name.")

    with tab_edit:
        if not df.empty:
            chosen = st.selectbox("Select Product to Edit", df["name"].tolist(), key="edit_item")
            row = df[df["name"] == chosen].iloc[0]
            with st.form("form_edit"):
                new_price = st.number_input("New Price", value=int(row["price"]), min_value=1, step=10)
                new_stock = st.number_input("New Stock", value=int(row["stock"]), min_value=0, step=1)
                if st.form_submit_button("Update"):
                    db.update_product(chosen, new_price, new_stock)
                    st.success(f"Updated '{chosen}' successfully.")
                    st.rerun()

    with tab_del:
        if not df.empty:
            chosen_del = st.selectbox("Select Product to Delete", df["name"].tolist(), key="del_item")
            if st.button("Delete Product", type="primary"):
                db.delete_product(chosen_del)
                st.success(f"Removed '{chosen_del}'.")
                st.rerun()


# Page 3: Online Shopping
def page_shop_online():
    st.title("Online Shopping")

    if "online_cart" not in st.session_state:
        st.session_state["online_cart"] = []

    df = db.get_products()
    display_products(df)

    st.subheader("Select Products")
    col1, col2, col3 = st.columns([3, 2, 2])
    with col1:
        chosen_prod = st.selectbox("Select Product", df["name"].tolist(), key="online_item")
    with col2:
        prod_row = df[df["name"] == chosen_prod].iloc[0]
        qty = st.number_input(f"Quantity (In Stock: {prod_row['stock']})", min_value=1, value=1, step=1, key="online_q")
    with col3:
        st.write("")
        st.write("")
        if st.button("Add to Cart", key="btn_add_online"):
            add_to_cart("online_cart", chosen_prod, prod_row["price"], qty)
            st.success(f"Added {qty}x '{chosen_prod}' to cart.")
            st.rerun()

    result = render_cart("online_cart", channel_label="Online")
    if result:
        grand_total = result["grand_total"]
        discount = result["discount"]
        if discount > 0:
            st.success(f"Order placed successfully! Total: Rs. {grand_total:,.2f} (Included 10% discount of Rs. {discount:,.2f})")
        else:
            st.success(f"Order placed successfully! Total: Rs. {grand_total:,.2f}")


# Page 4: Cashier Counter POS
def page_physical_billing():
    st.title("Store Billing & POS")
    show_low_stock_banner()

    if "pos_cart" not in st.session_state:
        st.session_state["pos_cart"] = []

    df = db.get_products()
    col1, col2, col3 = st.columns([3, 2, 2])
    with col1:
        chosen_prod = st.selectbox("Select Product", df["name"].tolist(), key="pos_item")
    with col2:
        prod_row = df[df["name"] == chosen_prod].iloc[0]
        qty = st.number_input(f"Quantity (In Stock: {prod_row['stock']})", min_value=1, value=1, step=1, key="pos_q")
    with col3:
        st.write("")
        st.write("")
        if st.button("Add to Bill", key="btn_add_pos"):
            add_to_cart("pos_cart", chosen_prod, prod_row["price"], qty)
            st.success(f"Added {qty}x '{chosen_prod}' to bill.")
            st.rerun()

    result = render_cart("pos_cart", channel_label="Physical")
    if result:
        st.success("Transaction completed successfully.")
        receipt = generate_bill(
            result["orders"],
            result["subtotal"],
            result["discount"],
            result["grand_total"],
            channel="Counter POS"
        )
        st.markdown(f"```text\n{receipt}\n```")


# Page 5: Orders & Analytics
def page_orders():
    st.title("Sales & Inventory Dashboard")
    
    df_orders = db.get_orders()
    df_products = db.get_products()

    # KPI summary cards
    st.subheader("Summary Metrics")
    kpi1, kpi2, kpi3, kpi4, kpi5 = st.columns(5)
    
    total_products = len(df_products)
    total_stock = int(df_products["stock"].sum()) if not df_products.empty else 0
    analysis = db.get_sales_analysis(df_orders)

    kpi1.metric("Total Products", total_products)
    kpi2.metric("Total Stock", f"{total_stock:,}")
    kpi3.metric("Total Revenue", f"Rs. {analysis['total_revenue']:,.2f}")
    kpi4.metric("Total Items Sold", f"{analysis['total_items_sold']:,}")
    kpi5.metric("Best-Selling Item", analysis['best_selling_product'], f"{analysis['best_selling_quantity']} sold")

    st.markdown("---")

    # Visual charts
    st.subheader("Analytics & Charts")
    tab_sales, tab_inventory = st.tabs(["Sales Analysis", "Inventory Overview"])

    with tab_sales:
        if not df_orders.empty:
            c1, c2 = st.columns(2)
            with c1:
                st.write("**Top Selling Products (Quantity)**")
                top_items = df_orders.groupby("product_name")["quantity"].sum().sort_values(ascending=False).head(8)
                st.bar_chart(top_items)
            with c2:
                st.write("**Revenue by Channel**")
                channel_rev = df_orders.groupby("channel")["total_price"].sum()
                st.bar_chart(channel_rev)
        else:
            st.info("No order history to display yet.")

    with tab_inventory:
        if not df_products.empty:
            c1, c2 = st.columns(2)
            with c1:
                st.write("**Stock by Category**")
                stock_cat = df_products.groupby("category")["stock"].sum()
                st.bar_chart(stock_cat)
            with c2:
                st.write("**Lowest Stock Items**")
                low_stock = df_products.sort_values(by="stock").head(8).set_index("name")["stock"]
                st.bar_chart(low_stock)
        else:
            st.info("No products found.")

    st.markdown("---")

    # Order history table
    st.subheader("Order Records")
    if df_orders.empty:
        st.info("No orders recorded yet.")
        return

    filter_choice = st.radio("Filter By Channel:", ["All", "online", "physical"], horizontal=True)
    filtered = df_orders if filter_choice == "All" else df_orders[df_orders["channel"] == filter_choice]
    st.dataframe(filtered, use_container_width=True, hide_index=True)


# Main navigation
def main():
    st.sidebar.title("Role Access")
    role = st.sidebar.selectbox("Select Role:", ["Admin", "Cashier", "Customer"], key="role_picker")
    st.session_state["role"] = role

    permissions = {
        "Admin": ["Home", "Products", "Shop Online", "Physical Billing", "Orders & Analytics"],
        "Cashier": ["Home", "Physical Billing", "Products", "Orders & Analytics"],
        "Customer": ["Home", "Shop Online"]
    }
    allowed = permissions[role]

    if "nav_selection" not in st.session_state or st.session_state["nav_selection"] not in allowed:
        st.session_state["nav_selection"] = allowed[0]

    st.sidebar.markdown("---")
    st.sidebar.title("Navigation")
    choice = st.sidebar.radio("Navigate to:", allowed, index=allowed.index(st.session_state["nav_selection"]))
    st.session_state["nav_selection"] = choice

    views = {
        "Home": page_home,
        "Products": page_products,
        "Shop Online": page_shop_online,
        "Physical Billing": page_physical_billing,
        "Orders & Analytics": page_orders,
    }
    views[choice]()


if __name__ == "__main__":
    main()

