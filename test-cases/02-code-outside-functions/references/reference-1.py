import pybryt


v1 = 10000  # velocity in ms**-1

v2 = v1 * 3.6  # velocity in kmh**-1
pybryt.Value(v2,
             name='v2',
             success_message='SUCCESS: Great! You converted the velocity in m/s to km/h.',
             failure_message='ERROR: Hmmm... It seems your conversion to km/h is wrong.')

v3 = v1 / 1000  # velocity in kms**-1
pybryt.Value(v3,
             name='v3',
             success_message='SUCCESS: Wow! The velocity in km/s you calculated is correct.',
             failure_message='ERROR: Oops... Are you sure your conversion to km/s is correct?')
