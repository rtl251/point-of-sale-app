import datetime
import numbers
now = datetime.datetime.now()


products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}]

product_ids=[] 
running_total_price = 0
accepted_ids=["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20"]

def product_input_process():
        product_id =input("Please input a product indentifier, or 'DONE' if there are no more items:")
        if product_id == "DONE":
            pass
        elif product_id in accepted_ids:
            product_ids.append(int(product_id))
            product_input_process()
        else:
            print("Product not found. Are you sure that product identifier is correct? Please try again!")
            product_input_process()

product_input_process()


print("* * * * * * * * * * * * * * *")
print("Barter Bob's")
print("888-555-9818")
print("www.BarterBobs.com")
print(now.strftime("%A %B %d, %Y" + " at " + "%I:%M%p"))
print("* * * * * * * * * * * * * * *")
print("SHOPPING CART ITEMS")
for product_id in product_ids:
    matching_products = [product for product in products if product["id"] == product_id]
    matching_product = matching_products[0]
    running_total_price += matching_product["price"]
    price_usd = '${0:.2f}'.format(matching_product["price"])
    print(" + " + matching_product["name"] +" " + str(price_usd))
print("* * * * * * * * * * * * * * *")
running_total_price_usd = '${0:.2f}'.format(running_total_price)
print("TOTAL: " + str(running_total_price_usd))
tax_owed = running_total_price * .08875
tax_owed_usd =  '${0:.2f}'.format(tax_owed)
print("PLUS NYC SALES TAX: " + str(tax_owed_usd))
total_owed = running_total_price + tax_owed
total_owed_usd = '${0:.2f}'.format(total_owed)
print("---------------")
print("AMOUNT DUE: " + str(total_owed_usd))
print("* * * * * * * * * * * * * * *")
print("Thank you for making trades at Barter Bob's! Enjoy and hope")
print("to see you again soon!")
print("* * * * * * * * * * * * * * *")

file_name = 'receipts-' + now.strftime('%Y-%m-%d-%I-%M-%p') + '.txt'

with open(file_name, "w") as file:
    file.write("* * * * * * * * * * * * * * *")
    file.write("\n")
    file.write("Barter Bob's")
    file.write("\n")
    file.write("888-555-9818")
    file.write("\n")
    file.write("www.BarterBobs.com")
    file.write("\n")
    file.write(now.strftime("%A %B %d, %Y" + " at " + "%I:%M%p")) # file.writes date and time
    file.write("\n")
    file.write("* * * * * * * * * * * * * * *")
    file.write("\n")
    file.write("SHOPPING CART ITEMS")
    file.write("\n")
    for product_id in product_ids:
        matching_products = [product for product in products if product["id"] == product_id]
        matching_product = matching_products[0]
        running_total_price += matching_product["price"]
        price_usd = '${0:.2f}'.format(matching_product["price"])
        file.write(" + " + matching_product["name"] +" " + str(price_usd))
        file.write("\n")
    file.write("\n")
    file.write("* * * * * * * * * * * * * * *")
    file.write("\n")
    running_total_price_usd = '${0:.2f}'.format(running_total_price)
    file.write("TOTAL: " + str(running_total_price_usd))
    file.write("\n")
    tax_owed = running_total_price * .08875
    tax_owed_usd =  '${0:.2f}'.format(tax_owed)
    file.write("PLUS NYC SALES TAX: " + str(tax_owed_usd))
    file.write("\n")
    total_owed = running_total_price + tax_owed
    total_owed_usd = '${0:.2f}'.format(total_owed)
    file.write("---------------")
    file.write("\n")
    file.write("AMOUNT DUE: " + str(total_owed_usd))
    file.write("\n")
    file.write("* * * * * * * * * * * * * * *")
    file.write("\n")
    file.write("Thank you for making trades at Barter Bob's! Enjoy and hope")
    file.write("\n")
    file.write("to see you again soon!")
    file.write("\n")
    file.write("* * * * * * * * * * * * * * *")
