import json

f = open("orders_july_2023.json")
orders = json.load(f)
f.close()

def find_order_with_biggest_value(orders, param = "price"):
    max_value = 0
    order_no = ""
    for key in orders.keys():
        if orders[key][f"{param}"] > max_value:
            max_value = orders[key][f"{param}"]
            order_no = key
    return order_no

def filter_orders_by_date(orders):
    amount_of_orders = [0] * 31
    for key in orders:
        date_parts = orders[key]["date"].split("-")
        day = int(date_parts[1])
        amount_of_orders[day - 1] += 1
    return amount_of_orders

def filter_orders_by_user(orders):
    users = {}
    for key in orders.keys():
        if orders[key]["user_id"] not in users.keys():
            users[orders[key]["user_id"]] = 1
        else:
            users[orders[key]["user_id"]] += 1

    return users

def filter_orders_by_price(orders):
    users = {}
    for key in orders.keys():
        if orders[key]["user_id"] not in users.keys():
            users[orders[key]["user_id"]] = orders[key]["price"]
        else:
            users[orders[key]["user_id"]] += orders[key]["price"]

    return users

def find_avg(orders, param = "orders"):
    total = 0
    counter = 0
    if param == "orders":
        for key in orders.keys():
            total += orders[key]["price"]
            counter += 1
    elif param == "goods":
        for key in orders.keys():
            total += orders[key]["price"] / orders[key]["quantity"]
            counter += 1
    return total / counter


print(f"1. The priciest order in July is {find_order_with_biggest_value(orders)}")
print(f"2. Order with the biggest quantity in July is {find_order_with_biggest_value(orders, param="quantity")}")


amount_of_ord = filter_orders_by_date(orders)
answer_3 = list(i+1 for i in range(len(amount_of_ord)) if amount_of_ord[i] == max(amount_of_ord))
print(f"3. It seems that days with the biggest amount({max(amount_of_ord)}) of orders: ", *answer_3)


users = filter_orders_by_user(orders)
amount = max(users[key] for key in users.keys())
print(f"4. The majority orders was made by (all users) in the amount of {amount}") #print is correct for this file ONLY


users = filter_orders_by_price(orders)
total_price = max(users[key] for key in users.keys())
print(f"5. The biggest total price {total_price} of the orders have users with ids: {list(key for key in users.keys() if users[key] == total_price)}")

print(f"6. avg price of order is {find_avg(orders)}")
print(f"7. avg price of googs is {find_avg(orders, param = "goods")}") # not sure what is meant by avg. price of goods or how to calculate it