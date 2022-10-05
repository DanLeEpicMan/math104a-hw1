import math


def f(x: float):
    '''
    This denotes out function f that takes any real number x as input.
    '''
    return math.exp(-x**2)

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

def q(h: float):
    '''
    The approximator function given in Q4.
    '''
    N = int(1/h)
    T_1 = generate_T(a=0, b=1, N=N)
    T_2 = generate_T(a=0, b=1, N=2*N)
    T_4 = generate_T(a=0, b=1, N=4*N)
    return (T_2(f) - T_1(f))/(T_4(f) - T_2(f))

value_of_q = 0
counter = 0
while value_of_q != 4:
    counter+=1
    value_of_q = q(1/counter)

print(f'Necessary h for q(h) ~= 4: 1/{counter}')

def approx_error(h: float):
    '''
    Calculating the approximate error using the method outlined.
    '''
    N=int(1/h)
    T_1 = generate_T(a=0, b=1, N=N)
    T_2 = generate_T(a=0, b=1, N=2*N)
    return (4/3) * (T_2(f) - T_1(f))

error = approx_error(1/counter)

print(f'Approximate Error: {error}')

T_1 = generate_T(a=0, b=1, N=counter)

print(f'Value for S_h: {T_1(f) + error}')


