favorite_colors = ["red", "blue", "green", "black", "orange"]
print(favorite_colors[2])
favorite_colors.append("pink")
print("pink")
print("pink" in favorite_colors)
favorite_colors.pop (3)
print("black" in favorite_colors)
favorite_colors.sort()
print(favorite_colors)
favorite_movie = ["flash", "sonic", "jungle book"]
print(favorite_movie[0])
print(favorite_movie[1])
print(favorite_movie[-1])
def average(numbers):
    return sum(numbers) / len(numbers)
numbers = [45, 67, 89, 34, 76]
avg = average(numbers)
print("Average of numbers: ", avg)
numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
for i in numbers:
    if i % 2 == 0:
        print(i)


