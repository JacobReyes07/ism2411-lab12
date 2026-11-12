# Disclosure! I used ChatGPT to explain the errors
# I was getting on exercises 5 and 8 then tried to fix them and
# got new errors which I again used ChatGPT to explain until I made
# something that worked.

# csv_practice

import csv
SALES_FILE = "data/sales.csv"
CLEANED_FILE = "data/cleaned.csv"
LOG_FILE = "data/run_log.txt"

def ex(num):
    return print(f"--- Exercise {num} ---")

ex(1)

with open(SALES_FILE, "r") as f:
    print(f"Opened {SALES_FILE}.")

ex(2)
with open(SALES_FILE, "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

ex(3)
with open(SALES_FILE, "r") as f:
    reader = csv.reader(f)
    header = next(reader)
    print(f"Header: {header}")
    for row in reader:
        print(row)

ex(4)
total_revenue = 0
with open(SALES_FILE, "r") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        product, price_str, qty_str = row
        price = float(price_str)
        quantity = int(qty_str)
        total = price * quantity
        total_revenue += total
        print(f"{product}: {quantity} units X ${price:.2f} = ${total:.2f}")

print(f"Total revenue: ${total_revenue:.2f}")

ex(5)

high_value = []
rows_read = 0
with open(SALES_FILE, "r", newline="") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        if not row:
            continue
        rows_read += 1
        product, price_str, qty_str = row
        price = float(price_str)
        quantity = int(qty_str)
        total = price * quantity
        if total > 100:
            high_value.append([product, f"{price:.2f}", quantity, f"{total:.2f}"])
with open(CLEANED_FILE, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["product", "price", "quantity", "total"])
    writer.writerow(high_value)
print(f"{len(high_value)} rows written out of {rows_read} rows read.")

ex(6)

dict_total = 0
with open(SALES_FILE, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        price = float(row["price"])
        quantity = int(row["quantity"])
        product = str(row["product"])
        print(f"{product}: {quantity} units x ${price} = ${price * quantity}")

# I prefer the exercise 6 one over the exercise 4 one.
# I found the exercise 6 one to be easier to read an looking at it
# I am better able to understand what each line of code does.

ex(7)

summary = {}


with open(SALES_FILE, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        product = row["product"]
        total = float(row["price"]) * int(row["quantity"])
        summary[product] = summary.get(product, 0) + total
for product in sorted(summary):
    print(f"{product}: ${summary[product]:.2f}")

ex(8)

from datetime import datetime

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open(LOG_FILE, "a") as f:
    f.write(f"{timestamp} total revenue: ${total_revenue:.2f}\n")

entries = 0
with open(LOG_FILE, "r") as f:
    for line in f:
        entries += 1
        print(line.strip())

print(f"Log entries so far: {entries}")

# Self Reflection 1
# Using python was a very different experience than doing the same
# thing manually in excel. I think for smaller data sets like the ones
# we used today and like the ones I usually see it would still be faster to
# just manually input it but I can definitely see how this is much more scalable
# and would be much faster for big datasets.

# Self Reflection 2
# Every month I look through my dad's receipts, I then sort them, and then I total them
# and then I compare it to the bank statements and account for anything that he doesn't
# get a receipt for like tolls and other bills that are automatically charged and do not give
# a physical paper receipt and making sure it adds up correctly. Then I have
# to put everything into an excel table template that my parents gave me
# which I then give to them and they give to their accountant. I think
# though that I can use this to turn the bank statement into a csv like we used here
# then I could compare it to the paper receipts and automatically then fill out the excel template
# with the new months stuff.