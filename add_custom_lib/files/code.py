import sys
import os

try:
    from modules.module1 import reuse_module
except ModuleNotFoundError:
    sys.path.insert(1, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from modules.module1 import reuse_module
else:
    print('module already exist')

print(sys.path)

def execute_module():
    reuse_module()

if __name__ == '__main__':
    print(sys.path)
    execute_module()
