# create a mathematical function and display it in a windows with matplotlib


import matplotlib.pyplot as plt


def f(x):
    return x**2


# create a list of x values from -10 to 10
x_values = [i for i in range(-10, 11)]
# create a list of y values with the function f
y_values = [f(i) for i in x_values]
# create a plot with the x and y values
plt.plot(x_values, y_values)
# show the plot
plt.show()
