"""
 This file is test template.
 package :'',
 user: 'bxcode'
 date: '1/17/2025'
"""
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

if __name__ == '__main__':
    n= 10
    print(f"Fibonacci de {n} es {fibonacci(n)}")
