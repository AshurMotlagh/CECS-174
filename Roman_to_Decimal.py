def convertDigit(single_roman_char):
    roman_char = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, "M": 1000}
    return roman_char[single_roman_char]


def romanToDecimal(roman_chars):
    total = 0
    while roman_chars != '':
        if len(roman_chars) == 1 or convertDigit(roman_chars[0]) >= convertDigit(roman_chars[1]):
            total += convertDigit(roman_chars[0])
            roman_chars = roman_chars[1:]
        else:
            total += convertDigit(roman_chars[1]) - convertDigit(roman_chars[0])
            roman_chars = roman_chars[2:]
    return total