# Function to calculate the final price after discount
def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.
    If discount is >= 20%, apply it; otherwise return original price.
    """
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price


# Main program
try:
    # Prompt user for input
    price = float(input("Enter the original price of the item:100 "))
    discount_percent = float(input("Enter the discount percentage: 30"))

    # Calculate and display result
    final_price = calculate_discount(price, discount_percent)

    if final_price != price:
        print(f"Final price after {discount_percent}% discount: ${final_price:.2f}")
    else:
        print(f"No discount applied. Original price: ${price:.2f}")

except ValueError:
    print(" Invalid input. Please enter numeric values for price and discount.")
