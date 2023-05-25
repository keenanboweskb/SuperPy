# Imports
import pandas as pd
import os
from record_buy import record_buy
from handle_date import handle_date
pd.options.mode.chained_assignment = None


def bought(id, product, price, quantity, buy_date, exp_date):
    if not (handle_date(exp_date)) | (handle_date(buy_date)):
        print("This is the incorrect date string format. It should be YYYY-MM-DD")
        return
    if not os.path.isfile("inventory.csv"):
        inventory = pd.DataFrame(
            columns=[
                "Product_ID",
                "Product_name",
                "Quantity",
                "Expiration_date",
            ]
        )
        count_row = inventory.shape[0]
        id = count_row + 1
        new_row = {
            "Product_ID": id,
            "Product_name": product,
            "Quantity": quantity,
            "Expiration_date": exp_date,
        }
        inventory = inventory.append(new_row, ignore_index=True)
        print(product + " was added to inventory")
        print("Updated inventory:")
        print(inventory.to_string(index=False))
        record_buy(id, product, price, buy_date, quantity, exp_date)
        return inventory.to_csv("inventory.csv", index=False)
    elif os.path.isfile("inventory.csv"):
        inventory = pd.read_csv("inventory.csv")
        product_exists = (
            (inventory["Product_name"] == product)
            & ((inventory["Expiration_date"] == exp_date))
        ).any()
        if not product_exists:
            count_row = inventory.shape[0]
            id = count_row + 1
            new_row = {
                "Product_ID": id,
                "Product_name": product,
                "Quantity": quantity,
                "Expiration_date": exp_date,
            }
            inventory = inventory.append(new_row, ignore_index=True)
            print(product + " was added to inventory")
            print("Updated inventory:")
            print(inventory.to_string(index=False))
            record_buy(id, product, price, buy_date, quantity, exp_date)
            return inventory.to_csv("inventory.csv", index=False)
        elif product_exists:
            product_index = inventory[
                (
                    (inventory["Product_name"] == product)
                    & ((inventory["Expiration_date"] == exp_date))
                )
            ].index.tolist()
            product_index = product_index[0]
            id = int(inventory["Product_ID"].iloc[product_index])
            current_quantity = inventory["Quantity"].iloc[product_index]
            new_quantity = int(current_quantity) + int(quantity)
            inventory["Quantity"].iloc[product_index] = new_quantity
            print(
                product + " is already in inventory, quantity is updated to:",
                new_quantity,
            )
            print("Updated inventory:")
            print(inventory.to_string(index=False))
            record_buy(id, product, price, buy_date, quantity, exp_date)
            return inventory.to_csv("inventory.csv", index=False)

