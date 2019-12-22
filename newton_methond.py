import math

#
# Testing Newton's method to find the roots (zeros) of a function in an area defined by a point (x0)

#
# Useful format function
def format_func(sfunc, coeff, degree):
  if coeff == 0:
    return sfunc
  
  res = sfunc
  if coeff > 0:
    if len(res) > 0:
      res = res + ' + ' + str(coeff)
    else:
      res = str(coeff)
    
  else:
    res = res + ' - ' + str(abs(coeff))

  if degree == 1:
    res = res + '*x'
  elif degree > 0:
    res = res + '*x^' + str(degree)

  return res

def polinom_func(x0, coeff, name):
  max_degree = len(coeff)-1
  res = coeff[max_degree]
  sfunc = ""
  for i in range(0, max_degree):
    degree = max_degree - i
    res = res + coeff[i] * math.pow(x0, degree)
    sfunc = format_func(sfunc, coeff[i], degree) 

  sfunc = format_func(sfunc, coeff[max_degree], 0) 
  if not name is None:
    print(name + ' = ' + sfunc)

  return res

def derivative_func(x0, coeff, name):
  coeff_int = coeff[:]
  max_degree = len(coeff_int)-1
  del coeff_int[-1]
  for i in range(0, max_degree-1):
    coeff_int[i] = coeff_int[i] * (max_degree - i)

  return polinom_func(x0, coeff_int, name)

def newton_method_base(x0, coeff):
  y = polinom_func(x0, coeff, None)
  d = derivative_func(x0, coeff, None)
  if d == 0:
    res = float('nan')
  else:
    res = x0 - (y/d)
  return res

#
# Newton's method
def newton_method(x0, coeff, num):
  x0_int = x0
  for i in range(num):
    x1 = newton_method_base(x0_int, coeff)
    x0_int = x1

  return x0_int

#
# Example
#
coeff = [5, -10, -7]
polinom_func(3, coeff, 'f(x)')
derivative_func(3, coeff, "f'(x)")
for i in range (-3, 3):
  res = newton_method(i, coeff, 7)
  print('x0: ' + str(i) + ' = ' + str(res))


