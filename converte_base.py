def convert_base(number, from_base, to_base):
    decimal_value = 0
    length = len(number)

    for i in range(length):
        digit = number[length - 1 - i] 
        if digit.isdigit(): 
            value = int(digit)
        else:  
            value = ord(digit.upper()) - ord('A') + 10
        
        decimal_value += value * (from_base ** i)

    if to_base == 10:
        return str(decimal_value)

    digits = []
    while decimal_value > 0:
        remainder = decimal_value % to_base
        if remainder >= 10:
            digits.append(chr(remainder - 10 + ord('A')))  
        else:
            digits.append(str(remainder))
        decimal_value //= to_base

    return ''.join(reversed(digits)) or '0'

def main():
    number = input("Digite o número a ser convertido: ")
    from_base = int(input("Digite a base original (2-36): "))
    to_base = int(input("Digite a base de destino (2-36): "))

    if 2 <= from_base <= 36 and 2 <= to_base <= 36:
        result = convert_base(number, from_base, to_base)
        print(f"O número {number} na base {from_base} é {result} na base {to_base}.")
    else:
        print("As bases devem estar entre 2 e 36.")

if __name__ == "__main__":
    main()
