# Task 1: Load and inspect restaurant dataset using pandas
import pandas as pd

columns = [
    "Restaurant_ID", "Restaurant_Name", "Country_Code", "City",
    "Address", "Locality", "Locality_Verbose",
    "Longitude", "Latitude", "Cuisines",
    "Average_Cost_for_two", "Currency",
    "Has_Table_booking", "Has_Online_delivery",
    "Is_delivering_now", "Switch_to_order_menu",
    "Price_range", "Aggregate_rating",
    "Rating_color", "Rating_text", "Votes"
]

df = pd.read_csv("restaurant.csv", names=columns)

print(df.head())
print(df.info())
