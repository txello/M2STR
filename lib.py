def gcd(x1,x2):
    while x1!=0 and x2 !=0:
        if x1 > x2: x1 = x1 % x2
        else: x2 = x2 % x1
    return x1 + x2
def egcd(a: int, b: int) -> list[int, int, int]:
    if a == 0:
        return (b, 0, 1)
    else:
        b_div_a, b_mod_a = divmod(b, a)
        g, x, y = egcd(b_mod_a, a)
        return (g, y - b_div_a * x, x)
def modinv(a: int, b: int) -> int:
    g, x, _ = egcd(a, b)
    if g != 1:
        raise Exception('gcd(a, b) != 1')
    return x % b
def snum(x):
    a = 2
    while a * a <= x and x % a != 0: a += 1
    return a * a > x
def euclid_nums(x):
    while x >= 2300:
        x //= 2
    x = 3 + (x * 2)
    while snum(x) != True:
        x += 1
    return x
def euclid(i):
    num1 = euclid_nums(euclid_nums(i))
    num2 = euclid_nums(euclid_nums(num1))
    d = ((num1 * num2)) // 2
    if d % 2 == 0: d -= 1
    nums1 = num1 * num2
    num1,num2 = num1-1,num2-1
    while(gcd(d,num1*num2) != 1):
        d = d - 1
    e = modinv(d,num1*num2)
    x = pow(i,e,nums1)
    return x
class Error(Exception):
    def __init__(self, text):
        self.txt = text