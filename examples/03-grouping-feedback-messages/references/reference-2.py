import pybryt


def square(a):
    res = []
    pybryt.Value(res,
                 name='empty_list',
                 success_message='SUCCESS 1: Great! You start with an empty list.',
                 failure_message='ERROR 1: Hmmm... Did you define an empty list before the loop?')
    for i in a:
        i_squared = i**2
        pybryt.Value(i_squared,
                     name='i_squared',
                     success_message='SUCCESS 2: Amazing! You are computing the squares of individual elements.',
                     failure_message='ERROR 2: Please check if you compute the squares of individual elements?')

        res.append(i_squared)
        pybryt.Value(res,
                     name='appending',
                     success_message='SUCCESS 3: Wow! You are appending the squared elements.',
                     failure_message='ERROR 3: Oops... Please check if you are appending the individual elements?')

    return res


pybryt.Value(square([-55, 13, 57, 0, 1, 2, -44]),
             name='final',
             success_message='SUCCESS 4: Your final solution is correct.',
             failure_message='ERROR 4: The final solution is wrong.')
