import pandas

data = pandas.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# gray = data[data["Primary Fur Color"] == "Gray"]
colors = data["Primary Fur Color"].to_list()

sum_colors = {
    "Fur Color": ["Gray", "Black", "Cinnamon"],
    "Count": [colors.count("Gray"), colors.count("Black"), colors.count("Cinnamon")],
}
data_frame = pandas.DataFrame(sum_colors)
print(data_frame)
data_frame.to_csv("./sum_colors.csv")
