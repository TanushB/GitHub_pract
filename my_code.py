def calculate_total_price(base_price: float, tax_rate: float, discount_rate: float = 0) -> float:
    """
    Calculate the total price after applying tax and an optional discount.

    Parameters:
    - base_price (float): The initial price of the item.
    - tax_rate (float): The tax rate to apply, as a percentage (e.g., 5 for 5%).
    - discount_rate (float): The discount rate to apply, as a percentage (e.g., 10 for 10%).

    Returns:
    - float: The final price after tax and discount.
    """
    if base_price < 0 or tax_rate < 0 or discount_rate < 0:
        raise ValueError("Price, tax, and discount rates must be non-negative.")

    price_with_tax = base_price * (1 + tax_rate / 100)
    final_price = price_with_tax * (1 - discount_rate / 100)

    return final_price

# Usage examples
print(calculate_total_price(100, 5, 15))  # Example with discount
print(calculate_total_price(200, 5, 5))   # Example with smaller discount
print(calculate_total_price(300, 10))     # Example with no discount

