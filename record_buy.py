# Imports
import pandas as pd
import os


def record_buy(id, product, price, buy_date, quantity, exp_date):
    if not os.path.isfile("bought.csv"):
        bought = pd.DataFrame(
            columns=[
                "Product_ID",
                "Product_name",
                "Buy_price",
                "Buy_date",
                "Quantity",
                "Expiration_date",
            ]
        )
        new_row = {
            "Product_ID": id,
            "Product_name": product,
            "Buy_price": price,
            "Buy_date": buy_date,
            "Quantity": quantity,
            "Expiration_date": exp_date,
        }
        bought = bought.append(new_row, ignore_index=True)
        print(product + " was added to inventory")
        return bought.to_csv("bought.csv", index=False)
    elif os.path.isfile("bought.csv"):
        bought = pd.read_csv("bought.csv")
        new_row = {
            "Product_ID": id,
            "Product_name": product,
            "Buy_price": price,
            "Buy_date": buy_date,
            "Quantity": quantity,
            "Expiration_date": exp_date,
        }
        bought = bought.append(new_row, ignore_index=True)
        print(product + " was added to inventory")
        return bought.to_csv("bought.csv", index=False)
