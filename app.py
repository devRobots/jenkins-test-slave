import sys
from src.math import pow

if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit(1)
    
    num = int(sys.argv[1])
    print(f"The number {num} pow 2 equals {pow(num)}")