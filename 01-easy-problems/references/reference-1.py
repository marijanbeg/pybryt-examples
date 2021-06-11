import pybryt


def rectangle_area(a, b):
    area = a*b
    pybryt.Value(area,
                 name='area',
                 success_message='SUCCESS: Great! You learned how to compute the area of a triangle.',
                 failure_message='ERROR: Hmmm... Are you sure that is how the area is calculated?')

    return area


pybryt.Value(rectangle_area(5, 3),
             name='solution')
