import os
import pybryt


def pybryt_reference(lecture, exercise):
    basename = os.path.join('pybryt-references',
                            f'exercise-{lecture}_{exercise}')
    pyfilename = f'{basename}.py'
    pklfilename = f'{basename}.pkl'

    if os.path.isfile(pyfilename):
        pybryt.ReferenceImplementation.compile(pyfilename).dump(pklfilename)
    elif not os.path.isfile(pklfilename):
        raise FileNotFoundError('Reference pkl file does not exists.')

    return pklfilename