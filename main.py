dict = {'one': 1, 'two': 2, 'thee': 3, 'four': 4, 'five': 5}
new_dict = {}
for key, value in dict.items():
    if value >= 3:
        new_dict[key] = value
print(new_dict)