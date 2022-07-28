from subprocess import ABOVE_NORMAL_PRIORITY_CLASS, CalledProcessError
from unittest.mock import _ArgsKwargs


x = [12,13,14,15,16,17,18,20,30,34,44]
x_odd = list(filter(lambda i: i%2!=0))
print(x_odd)