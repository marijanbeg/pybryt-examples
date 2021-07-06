import pybryt


def insertion_sort(x):
    x_col = pybryt.Collection(enforce_order=False,
                              success_message='SUCCESS: Wow! Your algorithm updates the list as it should.',
                              failure_message='ERROR: Hmmm... It looks like your algorithm does not perform insertion sort.')
    current_col = pybryt.Collection(enforce_order=True,
                                    success_message='SUCCESS: Your outer loop iterates from the second element to the last. Well done!',
                                    failure_message='ERROR: Please make sure your outer loop iterates from the second element to the last.')
    j_col = pybryt.Collection(enforce_order=False,
                              success_message='SUCCESS: Great! Your inner loop iterates towards left.',
                              failure_message='ERROR: Please make sure your inner loop iterates towards left.')
    for i in range(1, len(x)):
        current = x[i]
        current_col.add(pybryt.Value(current))

        j = i-1
        j_col.add(pybryt.Value(j))
        while j >= 0 and current < x[j]:
            x[j+1] = x[j]
            j -= 1
            j_col.add(pybryt.Value(j))

        x[j+1] = current
        x_col.add(pybryt.Value(x))

    return x


pybryt.Value(insertion_sort([55, 111, -33, 65, 1001, -362, 451]),
             name='final',
             success_message='SUCCESS: Amazing! Your function returns the correct solution.',
             failure_message='ERROR: Your function returns a wrong solution.')
