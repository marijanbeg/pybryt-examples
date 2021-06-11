import pybryt


def maximum(a):
    res = a[0]
    pybryt.Value(res,
                 name='initial_value',
                 success_message='SUCCESS: Great! You declare the first element to be the largest before the loop.',
                 failure_message='ERROR: Hmmm... Did you declare the first element to be largest before the loop?')
    for i in a:
        if i > res:
            res = i
            pybryt.Value(res,
                         name='larger',
                         success_message='SUCCESS: Very nice! You are finding larger elements.',
                         failure_message='ERROR: Hmmm... Are you finding the larger elements than the declared one.')

    pybryt.Value(res,
                 name='res',
                 success_message='SUCCESS: Wow! You found the largest element.',
                 failure_message='ERROR: Hmmm... Something is wrong in your function.')
    return res


pybryt.Value(maximum([-3, 1, 0, 5, 19]), name='solution')
