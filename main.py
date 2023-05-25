# Imports
import argparse
from export import export
from bought import bought
from sold import sold
from profit import profit
from plot_data import plot_data
from reset_files import reset_files

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.


def handle_args(args):
    if args.command == "buy":
        bought(
            id=id,
            product=args.product,
            quantity=args.quantity,
            price=args.price,
            buy_date=args.buy_date,
            exp_date=args.exp_date,
        )
    elif args.command == "sell":
        sold(
            product=args.product,
            price=args.price,
            quantity=args.quantity,
            sell_date=args.sell_date,
        )
    elif args.command == "export":
        export(selection=args.file, date=args.date)
    elif args.command == "profit":
        profit(args.date)
    elif args.command == "plot":
        plot_data(args.file)
    elif args.command == "reset":
        reset_files(args.file)


def main():
    parser = argparse.ArgumentParser(
        prog="main.py", description="Keep track of inventory."
    )
    subparsers = parser.add_subparsers(help="type of action", dest="command")
    subparsers.required = True

    buy_parser = subparsers.add_parser("buy", help="Purchase a product")
    buy_parser.add_argument(
        "--product", dest="product", type=str, help="product name", required=True
    )
    buy_parser.add_argument(
        "--buy-price",
        type=float,
        dest="price",
        help="product purchase price",
        required=True,
    )
    buy_parser.add_argument(
        "--quantity",
        type=int,
        dest="quantity",
        help="product quantity",
        default=1,
    )
    buy_parser.add_argument(
        "--buy-date",
        type=str,
        dest="buy_date",
        help="product date of purchase (format YYYY-MM-DD)",
        required=True,
    )
    buy_parser.add_argument(
        "--exp-date",
        type=str,
        dest="exp_date",
        help="product expiration date (format YYYY-MM-DD)",
        required=True,
    )

    sell_parser = subparsers.add_parser("sell", help="Sell a product")
    sell_parser.add_argument(
        "--product", type=str, dest="product", help="product name", required=True
    )
    sell_parser.add_argument(
        "--sell-price",
        type=float,
        dest="price",
        help="product selling price",
        required=True,
    )
    sell_parser.add_argument(
        "--quantity",
        type=int,
        dest="quantity",
        help="product quantity",
        default=1,
    )

    sell_parser.add_argument(
        "--sell-date",
        type=str,
        dest="sell_date",
        help="product sell date (format YYYY-MM-DD)",
        required=True,
    )
    export_parser = subparsers.add_parser(
        "export",
        help="Export selection of data on specified date",
    )
    export_parser.add_argument(
        "--file",
        type=str,
        dest="file",
        help="Data to be exported to .csv file",
        choices=["expired", "bought", "sold"],
        required=True,
    )
    export_parser.add_argument(
        "--date",
        type=str,
        dest="date",
        help="Select required date (format YYYY-MM-DD)",
        required=True,
    )

    profit_parser = subparsers.add_parser(
        "profit",
        help="Calculate profit on specfied date",
    )
    profit_parser.add_argument(
        "--date",
        type=str,
        dest="date",
        help="Select required date (format YYYY-MM-DD)",
        required=True,
    )

    plot_parser = subparsers.add_parser(
        "plot",
        help="Create a bar graph of products in inventory, bought or sold list",
    )
    plot_parser.add_argument(
        "--file",
        type=str,
        dest="file",
        help="File to be plotted",
        choices=["bought", "sold", "inventory"],
        required=True,
    )

    reset_parser = subparsers.add_parser(
        "reset",
        help="Reset a selection of files or reset all files",
    )
    reset_parser.add_argument(
        "--file",
        type=str,
        dest="file",
        help="Files to be reset",
        choices=["bought", "sold", "inventory", "all"],
        default="all",
    )

    args = parser.parse_args()
    return handle_args(args)


if __name__ == "__main__":
    main()
