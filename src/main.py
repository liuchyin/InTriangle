'''
Created on 2013-4-2

@author: Cong
'''

def edge(A, B):
    return  ((A[0] - B[0])**2 + (A[1] - B[1])**2)**(1.0 / 2)
    
def area(A, B, C):
    a = edge(A, B)
    b = edge(B, C)
    c = edge(C, A)
    p = (a + b + c) / 2
    return ((p - a) * (p - b) * (p - c) * p)**(1.0 / 2)

def isInTriangle1(A, B, C, D):
    if area(A, B, D) + area(B, C, D) + area(C, A, D) > area(A, B, C):
        return False
    return True

    

def main():
    A = (1.0, 2.0)
    B = (1.0, 1.0)
    C = (2.0, 1.0)
    D = (1.5, 0.5)
    print isInTriangle1(A, B, C, D)

if __name__ == '__main__':
    main()