# helpers.py

def calculate_total(quantity, price):
    """Calculate total for a single item"""
    return quantity * price

def format_currency(amount):
    """Format number as currency"""
    return f"${amount:,.2f}"

# The :.2f in the format string rounds floating point numbers to 2 decimal places - perfect for displaying money!