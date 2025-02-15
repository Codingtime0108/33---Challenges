#Number into roman number using object oriented programming

class RomanConverter:
    def __init__(self, number):
        self.number = number

    def to_roman(self):
        num = self.number
        result = ""

        while num >= 1000:
            result += "M"
            num -= 1000
        while num >= 900:
            result += "CM"
            num -= 900
        while num >= 500:
            result += "D"
            num -= 500
        while num >= 400:
            result += "CD"
            num -= 400
        while num >= 100:
            result += "C"
            num -= 100
        while num >= 1:
            result += "I"
            num -= 1
        return result
    
number = int(input("Enter a number: "))
converter = RomanConverter(number)
print(f"Roman numeral: {converter.to_roman()}")
