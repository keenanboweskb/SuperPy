import pandas as pd
import os
from handle_date import handle_date


def export(selection, date):
    if not handle_date(date):
        print("This is the incorrect date string format. It should be YYYY-MM-DD")
        return
    elif handle_date(date):
        date = pd.to_datetime(date)
    if selection == "expired":
        if os.path.isfile("inventory.csv"):
            print("There is no data in the current inventory")
        elif os.path.isfile("inventory.csv"):
            inventory = pd.read_csv("inventory.csv")
            inventory["Expiration_date"] = pd.to_datetime(
                inventory["Expiration_date"], format="%Y-%m-%d"
            )
            inventory["Expired"] = inventory["Expiration_date"] < date
            inventory_selection = inventory[inventory["Expired"]]
            if inventory_selection.empty:
                print("There are no expired products at this date")
            else:
                print("Expired products on selected date:")
                print(inventory_selection.to_string(index=False))
                print("Data is exported to Expired.csv")
                return inventory_selection.to_csv("Expired.csv", index=False)
    if selection == "bought":
        if not os.path.isfile("bought.csv"):
            print("There is no data in the bought administration")
        elif os.path.isfile("inventory.csv"):
            bought = pd.read_csv("bought.csv")
            bought["Buy_date"] = pd.to_datetime(bought["Buy_date"])
            bought["Bought"] = bought["Buy_date"] <= date
            bought_selection = bought[bought["Bought"]]
            if bought_selection.empty:
                print("No bought products before or on this date")
            else:
                print("Bought products on selected date:")
                print(bought_selection.to_string(index=False))
                print("Data is exported to Bought.csv")
                return bought_selection.to_csv("Bought.csv", index=False)
    if selection == "sold":
        if not os.path.isfile("sold.csv"):
            print("There is no data in the sold administration")
        elif os.path.isfile("sold.csv"):
            sold = pd.read_csv("sold.csv")
            sold["Sell_date"] = pd.to_datetime(sold["Sell_date"])
            sold["Sold"] = sold["Sell_date"] <= date
            sold_selection = sold[sold["Sold"]]
            if sold_selection.empty:
                print("No sold products before or on this date")
            else:
                print("Sold products on selected date:")
                print(sold_selection.to_string(index=False))
                print("Data is exported to Sold.csv")
                return sold_selection.to_csv("Bought.csv", index=False)

