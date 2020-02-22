class Interval(object):
    def __init__(self,a,b):
         """
         :a: integer
         :b: integer
         """
         assert a<b
         assert isinstance(a,int)
         assert isinstance(b,int)
         self._a = a
         self._b = b
    def __repr__(self):
        return 'Interval(' + str(self._a) + ',' + str(self._b) + ')'
    def __eq__(self,other):
        assert isinstance(self,Interval)
        assert isinstance(self,Interval)
        return self._a == other._a and self._b == other._b
    def __lt__(self,other):
        # a < b
        pass
    def __gt__(self,other):
        # a > b
        pass
    def __ge__(self,other):
        # a >= b
        pass
    def __le__(self,other):
        # a <= b
        pass
    def __add__(self,other):
        assert isinstance(self,Interval)
        assert isinstance(other,Interval)
        min_a = min(self._a, other._a)
        max_a = max(self._a, other._a)
        min_b = min(self._b, other._b)
        max_b = max(self._b, other._b)
        if max_a < min_b:
            return Interval(min_a, max_b)
        else:
            return [self, other]
