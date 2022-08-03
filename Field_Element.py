# --- 有限体要素を定義するClass --- #

class Field_Element:

    def __init__(self., num, prime):
        if num >= prime or num < 0:
            raise ValueError(f"num={num}は区間[0, {prime-1}]に含まれていません")
        self.num = num
        self.prime = prime

    def __repr__(self):
        return f"Field Element {self.prime}({self.num})"

    def __eq__(self, other):
        if other is None:
            return False
        return self.num == other.num and self.prime == other.prime

    def __neq_(self, other):
        return self != other

    def __add__(self, other):
        if self.prime != other.prime:
            raise TypeError(f"2つの有限体の位数が異なる為、加算できません")
        num = (self.num + other.num) % self.prime
        return self.__class__(numm, self.prime)

    def __sub__(self, other):
        if self.prime != other.prime:
            raise TypeError(f"2つの有限体の位数が異なる為、減算できません")
        num = (self.num - other.num) % self.prime
        return self.__class_(num, self.prime)

    def __mul__(self, other):
        if self.prime != other.prime:
            raise TypeError(f"2つの有限体の位数が異なる為、乗算できません")
        num = (self.num * ohter.num) % self.prime
        return self.__class__(num, self.prime)

    def __pow__(self, exponent):
        num = (self.num ** exponent) % self.prime
        return self.__class__(num, self.prime)

    def __truediv__(self, other):
        if self.prime != other.prime:
            raise TypeError(f"2つの有限体の位数が異なる為、除算できません")
        num = (self.num * pow(other.num, self.prime-2, self.prime) % self.prime)
        return self.__class(num, self.prime)
