letters = ["a", "b", "c"]

items = [0, "a"]

# it gives tuple using enumerate. Also unpacking works in tuple too.
for index, letter in enumerate(letters):
    print(index, letter)
