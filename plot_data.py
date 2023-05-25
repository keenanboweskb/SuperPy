import pandas as pd
import os


def plot_data(input):
    data = pd.read_csv(input + ".csv")
    plot = data.plot.bar(
        x="Product_name",
        y="Quantity",
        rot=45,
        color="b",
        title="Overview of quantity of different products",
    )
    if not os.path.isfile("./" + input + ".pdf"):
        print("File ./" + input + ".pdf is created in current directory")
        plot.get_figure().savefig("./" + input + ".pdf", format="pdf")
    elif os.path.isfile("./" + input + ".pdf"):
        os.remove("./" + input + ".pdf")
        print("File ./" + input + ".pdf is updated")
        plot.get_figure().savefig("./" + input + ".pdf", format="pdf")
