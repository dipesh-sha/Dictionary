data = {
    "Computer": "A computer is a digital electronic machine that can be programmed to carry out sequences of arithmetic or logical operations (computation) automatically.",
    "Keyboard": "A computer keyboard is a peripheral input device modeled after the typewriter keyboardwhich uses an arrangement of buttons or keys to act as mechanical",
    "Mouse": "A computer mouse (plural mice, sometimes mouses) is a hand-held pointing device that detects two-dimensional motion relative to a surface.",
    "Laptop": "Find a great collection of Laptops at HP. Enjoy Low Prices and Free Shipping when you buy now online",
}

# getDataFromUser
print("Enter your word")
dataFromUser = input()

fetchdata = data.get(dataFromUser)
print(fetchdata)