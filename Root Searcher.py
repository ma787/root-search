def get_num(message):
    """Validates an input and converts it into an float."""
    while 1:
        b = input(message)
        try:
            b = float(b)
            return b
        except ValueError:
            print("Please enter an integer.")


def f(x, co):
    """Evaluates a polynomial function with known coefficients for a given
    value of x"""
    result = 0

    for a, b in enumerate(reversed(co)):
        result += x**a * b

    return result


accuracy = 10**-10  
# a point is considered a root if the value of the function at that point is less than this value

d_msg = "Please enter the degree of the polynomial (must be >= 2): "

while 1:
    degree = int(get_num(d_msg))
    if degree < 2:  # function only works for quadratics or higher
        print("Degree must be at least 2.")
    else:
        break

coefficients = []

for i in range(degree, -1, -1):
    value = get_num("Please enter the coefficient of x^{}: ".format(i))
    coefficients.append(value)

question = """1: Bisection Method
2: Newton-Raphson Method
Please enter the number of the method you would like to use: """

while 1:
    choice = get_num(question)
    if choice not in (1, 2):
        print("Please enter a valid number.")
    else:
        choice = int(choice)
        break

if choice == 1:
    ub = get_num("Please enter the upper bound of the interval: ")
    lb = get_num("Please enter the lower bound: ")
    check = f(ub, coefficients) * f(lb, coefficients)
# there must be a change in sign for the algorithm to find a root

    if check > 0:
        print("This method cannot determine a root in the given interval.")

    elif check == 0:
        if f(ub, coefficients) == 0:
            print("The solution is {}".format(ub))
        else:
            print("The solution is {}".format(lb))

    else:
        midpoint = (ub + lb) / 2
        point = f(midpoint, coefficients)

        while abs(point) > accuracy:
            upper = f(ub, coefficients)
            lower = f(lb, coefficients)

            if point == 0:
                print("The solution is {}".format(midpoint))

            if point * upper > 0:
                ub = midpoint
# there is no change in sign between the midpoint and upper bound
# so the root must lie in between the midpoint and the lower bound
            else:
                lb = midpoint

            midpoint = (ub + lb) / 2
            point = f(midpoint, coefficients)

        print("The solution is {}".format(midpoint))
else:
    val = get_num("Please enter a starting value of x: ")
    point = f(val, coefficients)

    diff = []

    for power, c in enumerate(reversed(coefficients)):
        new = power * c
        diff.append(new)

    diff.remove(0)
# differentiates the polynomial by multiplying the coefficients by their
# corresponding power and decreasing the degree (length of list) by 1

    success = True

    while abs(point) > accuracy:
        try:
            grad = f(val, diff)
            val -= (point/grad)
            point = f(val, coefficients)

        except OverflowError:
            print("""
This method is unable to determine the solution with the given point.""")
            success = False
            break

    if success:
        print("The solution is {}".format(val))
