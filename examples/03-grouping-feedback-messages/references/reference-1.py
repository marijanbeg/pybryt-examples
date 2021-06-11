import pybryt


def square(a):
    res = []
    pybryt.Value(res,
                 success_message='SUCCESS: Great! You start with an empty list.',
                 failure_message='ERROR: Hmmm... Did you define an empty list before the loop?')
    for i in a:
        i_squared = i**2
        pybryt.Value(i_squared,
                     success_message='SUCCESS: Amazing! You are computing the squares of individual elements.',
                     failure_message='ERROR: Please check if you compute the squares of individual elements?')

        res.append(i**2)
        pybryt.Value(res,
                     success_message='SUCCESS: Wow! You are appending the squared elements.',
                     failure_message='ERROR: Oops... Please check if you are appending the individual elements?')

    return res


pybryt.Value(square([-55, 13, 57, 0, 1, 2, -44]),
             success_message='SUCCESS: Your final solution is correct.',
             failure_message='ERROR: The final solution is wrong.')
