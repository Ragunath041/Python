import csv

data = {
'Movie_1': 'The Shawshank Redemption',
'Movie_2': 'The Godfather',
'Movie_3': 'The Dark Knight',
'Movie_4': 'Pulp Fiction',
'Movie_5': 'Forrest Gump',
'Movie_6': 'The Matrix',
'Movie_7': 'Titanic',
'Movie_8': 'Gladiator',
'Movie_9': 'The Lion King',
'Movie_10': 'The Lord of the Rings: The Fellowship of the Ring',
'Movie_11': 'The Lord of the Rings: The Two Towers',
'Movie_12': 'The Lord of the Rings: The Return of the King',
'Movie_13': 'The Godfather: Part II',
'Movie_14': "Schindler's List",
'Movie_15': '12 Angry Men',
'Movie_16': 'Inception',
'Movie_17': 'Fight Club',
'Movie_18': 'The Green Mile',
'Movie_19': 'The Shawshank Redemption',
'Movie_20': 'The Godfather',
'Movie_21': 'The Dark Knight',
'Movie_22': 'Pulp Fiction',
'Movie_23': 'Forrest Gump',
'Movie_24': 'The Matrix',
'Movie_25': 'Titanic'
}

# Specify the file path
file_path = 'data.csv'

# Write data to CSV file
with open(file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    # Write header
    writer.writerow(['Date', 'Value'])
    # Write data
    for date, value in data.items():
        writer.writerow([date, value])

print("Data has been written to", file_path)
print(data)
