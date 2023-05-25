# Imports
import pandas as pd
import os


def record_sell(id, product, price, sell_date, quantity):
    if not os.path.isfile("sold.csv"):
        sold = pd.DataFrame(
            columns=[
                "Product_ID",
                "Product_name",
                "Sell_price",
                "Sell_date",
                "Quantity",
            ]
        )
        new_row = {
            "Product_ID": id,
            "Product_name": product,
            "Sell_price": price,
            "Sell_date": sell_date,
            "Quantity": quantity,
        }
        sold = sold.append(new_row, ignore_index=True)
        print(product + " was added to SELL administration")
        return sold.to_csv("sold.csv", index=False)
    elif os.path.isfile("sold.csv"):
        sold = pd.read_csv("sold.csv")
        new_row = {
            "Product_ID": id,
            "Product_name": product,
            "Sell_price": price,
            "Sell_date": sell_date,
            "Quantity": quantity,
        }
        sold = sold.append(new_row, ignore_index=True)
        print(product + " was added to SELL administration")
        return sold.to_csv("sold.csv", index=False)
