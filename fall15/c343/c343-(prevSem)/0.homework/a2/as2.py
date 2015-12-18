if __name__ == "__main__":
    
    from math import *

    ##  log(log*n)

    def f0(n):
        return log(f13(n),2)

    ## 2**(log*n)

    def f1(n):
        return (2**(f13(n)))*1.0

    ## (sqrt(2))**(log n)

    def f2(n):
        return sqrt(2)**(log(n,2))

    ## n**2 

    def f3(n):
        return (n**2)*1.0

    ## n!

    def f4(n):
        if n<=1:
            return 1
        else:
            return (n * f4(n-1))

    ## (log(n))!

    def f5(n):
        if n<=1:
            return 1
        else:
            return int(floor(log(n,2))*f5(floor(log(n,2))-1))

    ## (3/2.0)**n

    def f6(n):
        return (3/2.0)**n

    ## n**3

    def f7(n):
        return 1.0*(n**3)


    ## log(n)**2  

    def f8(n):
        return log(n,2)**2

    ## log(n!) 

    def f9(n):
        return log(f4(n),2)

    ## 2**(2**n)

    def f10(n):
        return 2.0**(2**n)

    ## n**(1/log(n))

    def f11(n):
        return n**(1/log(n,2))

    ## ln(ln n)

    def f12(n):
        return log(log(n))


    ## log*n

    def f13(n):
        if n<=1:
            return 0
        else:
            return 1+(f13(log(n,2)))

    ## n(2**n)

    def f14(n):
        return (n*(2**n))*1.0

    ## n**(log(log(n))

    def f15(n):
        return n**(log(log(n,2),2))

    ## ln(n)

    def f16(n):
        return log(n,e)

    ## 1

    def f17(n):
        return 1

    ## 2**(log(n))

    def f18(n):
        return 2**(log(n,2))

    ## (log(n)**(log(n))

    def f19(n):
        return log(n,2)**(log(n,2))

    ## e**n

    def f20(n):
        return e**n


    ## 4**(log(n))

    def f21(n):
        return 4**(log(n,2))

    ## (n+1)!

    def f22(n):
        return f4((n+1))

    ## sqrt(log(n))

    def f23(n):
        return sqrt(log(n,2))

    ## log*(log(n))

    def f24(n):
        return f13(log(n,2))

    ## 2**(sqrt(2(log(n)))

    def f25(n):
        return 2**(sqrt(2*(log(n,2))))

    ## n

    def f26(n):
        return n

    ## 2**n

    def f27(n):
        return 2.0**n

    ## n(log(n))

    def f28(n):
        return n*log(n,2)

    ## 2**(2**(n+1))

    def f29(n):
        return 2**(2**(n+1))

    ## list of all functions on input 5
    funs = [f0(5),f1(5),f2(5),f3(5),f4(5),f5(5),
            f6(5),f7(5),f8(5),f9(5),f10(5),f11(5),
            f12(5),f13(5),f14(5),f15(5),f16(5),f17(5),
            f18(5),f19(5),f20(5),f21(5),f22(5),f23(5),
            f24(5),f25(5),f26(5),f27(5),f28(5),f29(5)]
