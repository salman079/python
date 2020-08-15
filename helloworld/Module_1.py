#%load Module_2.py

import Module_2
tax_for_this_order = Module_2.calc_tax(sales_total=102123.37,tax_rate=.05)
print(tax_for_this_order)

import math_module as m
print(m.add(6,9))

import math_module
x = math_module.add(7,9)
print(x)