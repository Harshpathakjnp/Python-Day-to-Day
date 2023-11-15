class Solution:
    def part(self, n, forward):
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        if forward:
            return alphabets[:n]
        else:
            return alphabets[26 - n:]

    def digitsum(self, n):
        total = 0
        n = str(n)
        for i in n:
            total += int(i)
        return total

    def BalancedString(self, n):
        output = ""
        if n % 2 == 0:
            while n > 26:
                output += self.part(13, True)
                output += self.part(13, False)
                n = n - 26

            if n > 0:
                output += self.part(n // 2, True)
                output += self.part(n // 2, False)
        elif n % 2 != 0:
            s = self.digitsum(n)
            while n > 26:
                output += self.part(13, True)
                output += self.part(13, False)
                n = n - 26

            if n > 0:
                if s % 2 == 0:
                    output += self.part((n + 1) // 2, True)
                    output += self.part((n - 1) // 2, False)
                else:
                    output += self.part((n - 1) // 2, True)
                    output += self.part((n + 1) // 2, False)

        return output
