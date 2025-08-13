📝 Discount Calculator Program
Description
This program calculates the final price of an item after applying a discount.

If the discount is 20% or higher, it’s applied to the price.

If the discount is less than 20%, the original price is returned (no discount applied).

How It Works
User inputs the original price and discount percentage.

The program checks:

If discount_percent >= 20 → Apply discount

Else → Keep the original price

It prints the final price formatted to 2 decimal places.

It also handles invalid inputs (non-numeric entries).

Code Flow
python
Copy
Edit
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price

try:
    price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))
    final_price = calculate_discount(price, discount_percent)

    if final_price != price:
        print(f"Final price after {discount_percent}% discount: ${final_price:.2f}")
    else:
        print(f"No discount applied. Original price: ${price:.2f}")

except ValueError:
    print("Invalid input. Please enter numeric values for price and discount.")
Example Run
yaml
Copy
Edit
Enter the original price of the item: 100
Enter the discount percentage: 30
Final price after 30% discount: $70.00
Key Features
✅ Applies discount only if it's 20% or more
✅ Handles invalid inputs gracefully
✅ Formats output to two decimal place