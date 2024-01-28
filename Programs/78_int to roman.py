class Int_Roman:
    def int_to_roman(self , num:int) -> str:
        hashing = {
            1 : "I",
            4 : "IV",
            5 : "V",
            9 : "IX",
            10 : "X",
            40 : "XL",
            50 : "L",
            90 : "XC",
            100 : "C",
            400 : "CD",
            500 : "D",
            900 : "CM",
            1000 : "M"
        }
        ans = ""
        lst = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        for i in range(len(lst)):
            if num >= lst[i]:
                q = num // lst[i]
                num %= lst[i]
                for j in range(q):
                    ans += hashing.get(lst[i])
        return ans
a = Int_Roman()
n = int(input("Enter the number to find the Roman Number :"))
print(a.int_to_roman(n))