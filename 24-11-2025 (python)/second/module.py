import sys
import os

# Add parent folder (python_workshops) to Python path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from My_package.funcadd import add

result = add(5, 8)
print("The sum is:", result)
