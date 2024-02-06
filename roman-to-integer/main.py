from collections import defaultdict
#Mainly using to ignore key-value errors for lookups

def romanToInt(s):
    roman_map = defaultdict(int)
    roman_map['M'] = 1000
    roman_map['CM'] = 900
    roman_map['D'] = 500
    roman_map['CD'] = 400
    roman_map['C'] = 100
    roman_map['XC'] = 90
    roman_map['L'] = 50
    roman_map['XL'] = 40
    roman_map['X'] = 10
    roman_map['IX'] = 9
    roman_map['V'] = 5
    roman_map['IV'] = 4
    roman_map['I'] = 1

    idx = 0
    roman_number = 0

    while idx < len(s):
        if roman_map[s[idx:idx+2]]:
            roman_number += roman_map[s[idx:idx+2]]
            idx += 2
        else:
            roman_number += roman_map[s[idx]]
            idx += 1
    return roman_number

