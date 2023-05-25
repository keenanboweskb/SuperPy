
import os


def reset_files(input):
    if input == "bought":
        if os.path.isfile("./bought.csv"):
            os.remove("./bought.csv")
        if os.path.isfile("./bought.pdf"):
            os.remove("./bought.pdf")
    elif input == "sold":
        if os.path.isfile("./sold.csv"):
            os.remove("./sold.csv")
        if os.path.isfile("./sold.pdf"):
            os.remove("./sold.pdf")
    elif input == "inventory":
        if os.path.isfile("./inventory.csv"):
            os.remove("./inventory.csv")
        if os.path.isfile("./inventory.pdf"):
            os.remove("./inventory.pdf")
    else:
        if os.path.isfile("./inventory.csv"):
            os.remove("./inventory.csv")
        if os.path.isfile("./bought.csv"):
            os.remove("./bought.csv")
        if os.path.isfile("./sold.csv"):
            os.remove("./sold.csv")
        if os.path.isfile("./inventory.pdf"):
            os.remove("./inventory.pdf")
        if os.path.isfile("./bought.pdf"):
            os.remove("./bought.pdf")
        if os.path.isfile("./sold.pdf"):
            os.remove("./sold.pdf")
        if os.path.isfile("./Expired.csv"):
            os.remove("./Expired.csv")
        if os.path.isfile("./Bought.csv"):
            os.remove("./Bought.csv")
        if os.path.isfile("./Sold.csv"):
            os.remove("./Sold.csv")

