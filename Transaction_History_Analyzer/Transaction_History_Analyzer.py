
# EXERCISE 3: TRANSACTION HISTORY ANALYZER

import random
from collections import defaultdict

LAST_NAME = "Ogena"
SEED_NUM = 2
FAVORITE_ARTIST = "Yeng Constantino"
STUDENT_ID = "TUPM-26-7952"  # Replace if needed

def make_rng(offset=0):
    artist_value = sum(
        (i + 1) * ord(char)
        for i, char in enumerate(FAVORITE_ARTIST)
    )
    return random.Random(SEED_NUM + artist_value + offset)

rng = make_rng(3)

customers = [f"{LAST_NAME}_C{i}" for i in range(1, 6)]

prices = {
    "NOTEBOOK": 50.00,
    "PEN": 15.00,
    "USB": 250.00,
    "HEADPHONES": 500.00,
    "CALCULATOR": 350.00
}

products = list(prices.keys())
records = []

for customer in customers:
    for product in products:
        quantity = rng.randint(1, 5)
        records.append({
            "customer": customer,
            "product": product,
            "quantity": quantity,
            "price": prices[product],
            "value": round(quantity * prices[product], 2)
        })

# One repeated customer-product transaction
records.append(records[0].copy())

print("=" * 90)
print("TRANSACTION HISTORY ANALYZER")
print("=" * 90)
print(f"LAST NAME: {LAST_NAME}")
print(f"ID: {STUDENT_ID}")
print(f"Seed: {SEED_NUM}")
print(f"Favorite Artist: {FAVORITE_ARTIST}")
print(f"Total Transactions: {len(records)}")

print("\nPRODUCT PRICE LIST")
for product, price in prices.items():
    print(f"{product:<18} PHP {price:.2f}")

print("\nGENERATED TRANSACTION RECORDS")
print(f"{'NO.':<5}{'CUSTOMER':<18}{'PRODUCT':<18}"
      f"{'QUANTITY':<12}{'PRICE':<12}{'VALUE':<12}{'FLAG'}")

seen = set()
for i, r in enumerate(records, 1):
    key = (r["customer"], r["product"])
    flag = "DUPLICATE" if key in seen else ""
    seen.add(key)

    print(
        f"{i:<5}{r['customer']:<18}{r['product']:<18}"
        f"{r['quantity']:<12}"
        f"{r['price']:<12.2f}{r['value']:<12.2f}{flag}"
    )

print("\nCUSTOMER SUMMARIES")
for customer in customers:
    customer_records = [
        r for r in records if r["customer"] == customer
    ]
    total_quantity = sum(r["quantity"] for r in customer_records)
    total_value = sum(r["value"] for r in customer_records)

    print(
        f"{customer:<18} Transactions={len(customer_records):<4} "
        f"Quantity={total_quantity:<4} "
        f"Total=PHP {total_value:.2f}"
    )

print("\nPRODUCT SUMMARIES")
for product in products:
    product_records = [
        r for r in records if r["product"] == product
    ]
    total_quantity = sum(r["quantity"] for r in product_records)
    total_value = sum(r["value"] for r in product_records)
    unique_customers = len({
        r["customer"] for r in product_records
    })

    print(
        f"{product:<18} Quantity={total_quantity:<4} "
        f"Customers={unique_customers:<3} "
        f"Sales=PHP {total_value:.2f}"
    )

print("\nREPEATED/DISTINCT TRANSACTIONS")
print(f"Total transaction records: {len(records)}")
print(f"Distinct customer-product pairs: {len(seen)}")
print(f"Repeated records: {len(records) - len(seen)}")

print("\nORDERED RESULTS (highest transaction value first)")
for r in sorted(records, key=lambda x: x["value"], reverse=True):
    print(
        f"{r['customer']:<18} {r['product']:<18} "
        f"Qty={r['quantity']:<3} "
        f"Value=PHP {r['value']:.2f}"
    )

print("\nOVERALL TRANSACTION SUMMARY")
total_quantity = sum(r["quantity"] for r in records)
total_value = sum(r["value"] for r in records)
unique_customers = len({r["customer"] for r in records})
unique_products = len({r["product"] for r in records})

print(f"Total records: {len(records)}")
print(f"Distinct customer-product pairs: {len(seen)}")
print(f"Repeated records: {len(records) - len(seen)}")
print(f"Distinct customers: {unique_customers}")
print(f"Distinct products: {unique_products}")
print(f"Total quantity sold: {total_quantity}")
print(f"Overall transaction value: PHP {total_value:.2f}")
print("Final Consolidated Transaction Report: COMPLETE")