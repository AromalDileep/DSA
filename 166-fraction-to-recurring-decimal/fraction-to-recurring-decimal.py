class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0: return "0"
        sign = "-" if numerator * denominator < 0 else ""
        numerator, denominator = abs(numerator), abs(denominator)
        res = [sign + str(numerator // denominator)]
        remainder = numerator % denominator
        if remainder == 0: return "".join(res)
        res.append(".")
        m = {}
        while remainder:
            if remainder in m:
                res.insert(m[remainder], "(")
                res.append(")")
                break
            m[remainder] = len(res)
            remainder *= 10
            res.append(str(remainder // denominator))
            remainder %= denominator
        return "".join(res)
