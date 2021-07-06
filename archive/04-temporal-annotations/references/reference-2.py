# This code is not working. It is a suggestion for defining temporal annotations.
import pybryt
import numpy as np


def lucas(n):
    container = pybryt.Container(sucess_message='SUCCESS 0: ...',
                                 failure_message='ERROR 0: ...')  # Container
    lucas_series = np.zeros(n, dtype=int)

    lucas_series[0] = 2
    container.add(pybryt.Value(lucas_series,
                               name='first_element',
                               success_message='SUCCESS 1: Your first element is correct.',
                               failure_message='ERROR 1: Please check your first element in the series.'))
    if n == 1:
        return lucas_series

    lucas_series[1] = 1
    container.add(pybryt.Value(lucas_series,
                               name='second_element',
                               success_message='SUCCESS 2: Your second element is correct.',
                               failure_message='ERROR 2: Please check your second element in the series.'))

    if n == 2:
        return lucas_series

    for i in range(2, n):
        lucas_series[i] = lucas_series[i-1] + lucas_series[i-2]
        container.add(pybryt.Value(lucas_series,
                                   name='other_elements',
                                   success_message='SUCCESS 3: You are generating n>2 elements right.',
                                   failure_message='ERROR 3: Hmmm... Are you summing the previous two elements right?'))

    return lucas_series


pybryt.Value(lucas(20),
             name='final',
             success_message='SUCCESS 4: Amazing! Your final solution is correct.',
             failure_message='ERROR 4: The Lucas series you computed is wrong.')
