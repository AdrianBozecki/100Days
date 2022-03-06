import pandas

data = pandas.read_csv("squirrel.csv")
fur_color_column = data["Primary Fur Color"]
amount_of_gray_squirrels = len(data[fur_color_column == "Gray"])
amount_of_red_squirrels = len(data[fur_color_column == "Cinnamon"])
amount_of_black_squirrels = len(data[fur_color_column == "Black"])


data_dict = {
    "color": ["Gray", "Red", "Black"],
    "count": [amount_of_gray_squirrels, amount_of_red_squirrels, amount_of_black_squirrels]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
