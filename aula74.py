def soma(x, y, z=None):
    if z is not None:
        print(f'{x=} {y=} {z=}')
    else:
        print(f'{x=} {y=}')

soma(10, 20)
soma(30, 40, 7)
soma(z=5, x=50, y=70)