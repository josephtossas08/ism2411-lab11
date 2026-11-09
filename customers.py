# Reflection Questions

# 1. I would use .get() when working with information that might be missing, such as a customer's phone number or email. I would use bracket notation when I know a key exists and need its value. My rule of thumb is to use .get() to avoid errors with missing information and brackets when the information is required.

# 2. Exercise 8 reminds me of using SUMIF in Excel because it groups and adds values based on a specific category. Python is more useful for large datasets because it can automatically process thousands of records using loops instead of requiring me to organize and calculate everything manually.

# EXERCISE 1 - One Customer


customer = {
    "name": "Alice",
    "email": "alice@example.com",
    "tier": "bronze",
    "ytd_spend": 1250
}

# Print each field individually

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])

# Print the entire dictionary
print(customer)



# EXERCISE 2 - Update and Add


# Add a phone field
customer["phone"] = "813-555-1234"
print(customer)

# Update the customer's tier
customer["tier"] = "platinum"
print(customer)

# Delete the email field
del customer["email"]
print(customer)



# EXERCISE 3 - Safe Lookup


# Use get() to look up the deleted email field
email = customer.get("email", "no email on file")
print(email)

# Use bracket notation and catch the KeyError
try:
    print(customer["email"])
except KeyError:
    print("KeyError: email does not exist in the dictionary")


# EXERCISE 4 - Iterate


# Iterate through the dictionary using items()
for key, value in customer.items():
    print(f"{key}: {value}")

# Iterate without using items()
# This method gives us the keys, so we use customer[key]
# to access each corresponding value.
for key in customer:
    print(f"{key}: {customer[key]}")


# EXERCISE 5 - Lookup Table


tier_discounts = {
    "bronze": 0,
    "silver": 0.05,
    "gold": 0.10,
    "platinum": 0.15
}

# Look up the customer's discount
discount_rate = tier_discounts.get(customer["tier"], 0)

# Calculate the discount on a $200 purchase
purchase_price = 200
discount_amount = purchase_price * discount_rate
final_price = purchase_price - discount_amount

print("Tier:", customer["tier"])
print("Discount rate:", discount_rate)
print("Discount amount: $", discount_amount)
print("Final price: $", final_price)


# EXERCISE 6 - List of Dictionaries


customers = [
    {"name": "Alice", "tier": "platinum"},
    {"name": "Bob", "tier": "silver"},
    {"name": "Charlie", "tier": "gold"}
]

# Use the same $200 purchase amount for each customer
for customer_info in customers:
    tier = customer_info["tier"]
    discount_rate = tier_discounts.get(tier, 0)
    discount_amount = 200 * discount_rate

    print(
        f"Name: {customer_info['name']}, "
        f"Tier: {tier}, "
        f"Discount amount: ${discount_amount:.2f}"
    )


# EXERCISE 7 - Nested Catalog


catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8}
}

# Check each product's stock
for product, details in catalog.items():
    if details["stock"] < 20:
        print(product, "- LOW STOCK")


# EXERCISE 8 - Sales by Region


transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200}
]

# Create an empty summary dictionary
sales_by_region = {}

# Add up sales for each region
for transaction in transactions:
    region = transaction["region"]
    amount = transaction["amount"]

    sales_by_region[region] = sales_by_region.get(region, 0) + amount

# Print the final summary sorted by region name
for region in sorted(sales_by_region):
    print(f"{region}: ${sales_by_region[region]}")
