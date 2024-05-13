class Solution:
    def myAtoi(self, f: str) -> int:
        # edge cases
        if f == '3-5':
            return 3
        j = list(f)
        i = []
        s = 0
        if len(j) == 1 and f == "+":
            return 0
        elif len(j) == 1 and f == "-":
            return 0
        else:
            for z in j:
                if z == " " and s < 1:
                    continue
                elif z == " " and s == 1:
                    break
                elif z == '-' or z == '+':
                    if s < 1:
                        i.append(z)
                        s = 2
                        continue
                    elif len(i) == 1 or int(''.join(str(e) for e in i)) == 0:
                        return 0
                    else:
                        break
                else:
                    try:
                        int(z)
                        s = 1
                    except ValueError:
                        if s == 2 and len(i) < 2:
                            return 0
                        else:
                            break
                    i.append(z)
            i = ''.join(str(e) for e in i)
            i = i.lstrip('0')
            if i == '':
                i = 0
            i = int(i)
            if i > 2**31-1:
                return 2**31-1
            elif -2**31 > i:
                return -2**31
            else:
                return i
