import math


def f(x: float):
    '''
    This denotes out function f that takes any real number x as input.
    '''
    return x*math.exp(x**2)

def generate_T(*, a: int, b: int, N: int):
    '''
    This returns an appropriate T depending on a, b, and N.

    Note that this returns a FUNCTION to be used for approximating, not a NUMBER.
    '''
    def wrap(func) -> float:
        h = (b - a)/N
        sum = 0
        for i in range(N + 1): # i = 0, 1, ..., N-1, N
            current_x = a + i * h
            scalar = 0.5 if i==0 or i==N else 1
            sum += func(current_x) * scalar

        return sum * h

    return wrap

def abs(x: float) -> float:
    '''
    Absolute value.
    '''
    return x if x>0 else -x

true_value = (math.e - 1)/2
T_10 = generate_T(a=0, b=1, N=10)
T_20 = generate_T(a=0, b=1, N=20)
T_40 = generate_T(a=0, b=1, N=40)
print(f'Error for T_10(f): {abs(true_value - T_10(f))}')
print(f'Error for T_20(f): {abs(true_value - T_20(f))}')
print(f'Error for T_40(f): {abs(true_value - T_40(f))}')
    