import collections

Car = collections.namedtuple('Car',['price','mileage','brand'])

car1 = Car(25000, 2000, 'BMW')
assert car1.price == 25000
assert car1.mileage == 2000
assert car1.brand == 'BMW'
assert isinstance(car1, tuple)

# Note that indexing works also!
# This means that if you change a tuple into a namedtuple,
# the change will be backwards compatible.
assert car1[2] == 'BMW'

print('All good!')

