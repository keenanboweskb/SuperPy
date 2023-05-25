# Imports
import os
import pandas as pd
from record_sell import record_sell
from handle_date import handle_date


def sold(product, price, sell_date, quantity):

    if not handle_date(sell_date):
        (print(+"This is the incorrect date string format. It should be YYYY-MM-DD"))
        return
    if not os.path.isfile("inventory.csv"):
        print("There is nothing the current inventory")

    elif os.path.isfile("inventory.csv"):
        inventory = pd.read_csv("inventory.csv")
        inventory["Quantity"] = pd.to_numeric(inventory["Quantity"])
        product_exists = (
            (inventory["Product_name"] == product)
            & (inventory["Quantity"] >= quantity)
        ).any()

        if not product_exists:
            print(product + " " + "is not (sufficeiently) present in inventory")
        elif product_exists:
            product_index = inventory[
                (
                    (inventory["Product_name"] == product)
                    & (inventory["Quantity"] >= quantity)
                )
            ].index.tolist()
            product_index = product_index[0]
            if pd.to_datetime(
                inventory["Expiration_date"].iloc[product_index], format="%Y-%m-%d"
            ) > pd.to_datetime(sell_date, format="%Y-%m-%d"):
                print("Product is already expired at this Sell date")
            else:
                id = inventory["Product_ID"].iloc[product_index]
                record_sell(id, product, price, sell_date, quantity)
                new_quantity = int(inventory["Quantity"].iloc[product_index]) - int(
                    quantity
                )
                if new_quantity == 0:
                    inventory = inventory.drop(inventory.index[product_index])
                    print("Updated inventory:")
                    print(inventory.to_string(index=False))
                    return inventory.to_csv("inventory.csv", index=False)
                else:
                    inventory["Quantity"].iloc[product_index] = new_quantity
                    print("Updated inventory:")
                    print(inventory.to_string(index=False))
                    return inventory.to_csv("inventory.csv", index=False)
    
