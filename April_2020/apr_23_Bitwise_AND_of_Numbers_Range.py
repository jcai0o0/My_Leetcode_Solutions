class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        if m == n:
            return m
        a = '{0:b}'.format(m)
        b = '{0:b}'.format(n)
        if len(a) != len(b):
            return 0
        res = ''
        i = 0
        while i < len(a):
            if a[i] == '1' and b[i]=='1':
                res += '1'
                i += 1
            elif a[i] == '0' and b[i] == '0':
                res += '0'
                i += 1
            else:
                res += '0' * (len(a)-i)
                break

        return int(res, 2)