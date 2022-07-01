# create a mathematical function and display it in a windows with matplotlib


import matplotlib.pyplot as plt
import numpy as np

NUMBER_OF_RANDOM_NUMBERS = 30
LENGTH_OF_X_AXIS = 100
SLOPE = 0.1

PLOT_SIZE = 5

rands = np.random.rand(NUMBER_OF_RANDOM_NUMBERS)


def f(x):
    result = 0

    for rand in rands:
        result += 1 * np.sin(rand * x)

    # result += SLOPE * x
    result /= NUMBER_OF_RANDOM_NUMBERS
    return result


# create a list of x values from 0 to 2pi with a step of 0.1
x_values = np.arange(2 * np.pi, LENGTH_OF_X_AXIS * np.pi, 0.01)
# create a list of y values with the function f
y_values = [f(i) for i in x_values]

# make plot 2 times wider than it is high
plt.figure(figsize=(PLOT_SIZE * 2.1, PLOT_SIZE * 1))


# search algorithm for the highest y value
init_x = np.random.randint(0, LENGTH_OF_X_AXIS)

# insert a point at x = x_init and y = f(x_init) as red dot
plt.scatter(init_x, f(init_x), color="red", marker="o")


# create a plot with the x and y values
plt.plot(x_values, y_values)

# show the plot
plt.show()
