import timeit
from classes import Calculator

# Import for tests
setup = 'from classes import Calculator'

# Sum test cases
case = """
calc = Calculator('1', '1')
calc.sum()
"""
elapsed_time = timeit.timeit(case, setup, number=1)
print(f'Calculated in {elapsed_time:.10f} seconds')

case = """
calc = Calculator('10', '10')
calc.sum()
"""
elapsed_time = timeit.timeit(case, setup, number=1)
print(f'Calculated in {elapsed_time:.10f} seconds')

case = """
calc = Calculator('975', '345')
calc.sum()
"""
elapsed_time = timeit.timeit(case, setup, number=1)
print(f'Calculated in {elapsed_time:.10f} seconds')

case = """
calc = Calculator('1975', '1345')
calc.sum()
"""
elapsed_time = timeit.timeit(case, setup, number=1)
print(f'Calculated in {elapsed_time:.10f} seconds')

case = """
calc = Calculator('11975', '11345')
calc.sum()
"""
elapsed_time = timeit.timeit(case, setup, number=1)
print(f'Calculated in {elapsed_time:.10f} seconds')

case = """
calc = Calculator('111975', '111345')
calc.sum()
"""
elapsed_time = timeit.timeit(case, setup, number=1)
print(f'Calculated in {elapsed_time:.10f} seconds')

case = """
calc = Calculator('1111975', '1111345')
calc.sum()
"""
elapsed_time = timeit.timeit(case, setup, number=1)
print(f'Calculated in {elapsed_time:.10f} seconds')

case = """
calc = Calculator('11111975', '11111345')
calc.sum()
"""
elapsed_time = timeit.timeit(case, setup, number=1)
print(f'Calculated in {elapsed_time:.10f} seconds')

case = """
calc = Calculator('111111975', '111111345')
calc.sum()
"""
elapsed_time = timeit.timeit(case, setup, number=1)
print(f'Calculated in {elapsed_time:.10f} seconds')

case = """
calc = Calculator('1111111975', '1111111345')
calc.sum()
"""
elapsed_time = timeit.timeit(case, setup, number=1)
print(f'Calculated in {elapsed_time:.10f} seconds')

print('\n')

# Multiplication Test Cases
case = """
calc = Calculator('1', '1')
calc.karatsuba()
"""
elapsed_time = timeit.timeit(case, setup, number=1)
print(f'Calculated in {elapsed_time:.10f} seconds')

case = """
calc = Calculator('10', '10')
calc.karatsuba()
"""
elapsed_time = timeit.timeit(case, setup, number=1)
print(f'Calculated in {elapsed_time:.10f} seconds')

case = """
calc = Calculator('974', '345')
calc.karatsuba()
"""
elapsed_time = timeit.timeit(case, setup, number=1)
print(f'Calculated in {elapsed_time:.10f} seconds')

case = """
calc = Calculator('1975', '1345')
calc.karatsuba()
"""
elapsed_time = timeit.timeit(case, setup, number=1)
print(f'Calculated in {elapsed_time:.10f} seconds')

case = """
calc = Calculator('11975', '11345')
calc.karatsuba()
"""
elapsed_time = timeit.timeit(case, setup, number=1)
print(f'Calculated in {elapsed_time:.10f} seconds')

case = """
calc = Calculator('111975', '111345')
calc.karatsuba()
"""
elapsed_time = timeit.timeit(case, setup, number=1)
print(f'Calculated in {elapsed_time:.10f} seconds')

case = """
calc = Calculator('1111975', '1111345')
calc.karatsuba()
"""
elapsed_time = timeit.timeit(case, setup, number=1)
print(f'Calculated in {elapsed_time:.10f} seconds')

case = """
calc = Calculator('11111975', '11111345')
calc.karatsuba()
"""
elapsed_time = timeit.timeit(case, setup, number=1)
print(f'Calculated in {elapsed_time:.10f} seconds')

case = """
calc = Calculator('111111975', '111111345')
calc.karatsuba()
"""
elapsed_time = timeit.timeit(case, setup, number=1)
print(f'Calculated in {elapsed_time:.10f} seconds')

case = """
calc = Calculator('1111111975', '1111111345')
calc.karatsuba()
"""
elapsed_time = timeit.timeit(case, setup, number=1)
print(f'Calculated in {elapsed_time:.10f} seconds')

case = """
calc = Calculator('11111111975', '11111111345')
calc.karatsuba()
"""
elapsed_time = timeit.timeit(case, setup, number=1)
print(f'Calculated in {elapsed_time:.10f} seconds')

case = """
calc = Calculator('11111111975', '11111111345')
calc.karatsuba()
"""
elapsed_time = timeit.timeit(case, setup, number=1)
print(f'Calculated in {elapsed_time:.10f} seconds')
