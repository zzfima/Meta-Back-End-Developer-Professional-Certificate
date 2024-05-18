# value = key * 2
usingRange = {x: x * 2 for x in range(10)}
print("Using range: ", usingRange)

# value = key ^ 2
number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
nums1 = {x: x**2 for x in number}
print("Using list: ", nums1)

# using zip to use 2 lists
months = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "June",
    "July",
    "Aug",
    "Sept",
    "Oct",
    "Nov",
    "Dec",
]

calendar = {k: v for (k, v) in zip(number, months)}
print("Using zip: ", calendar)
