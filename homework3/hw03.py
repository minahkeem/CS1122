#Minah Kim

#Q2
def decToBinary(dec):
    return bin(dec)

#Q3
def hexToASCII(listOfHexa):
    asc = ""
    for hexa in listOfHexa:
        asc += chr(hexa)
    return asc

#Q4
def binToHex(bina):
    return hex(bina)

#Q5
def octToDec(octa):
    exp = 1
    digit = 0
    summed = 0
    for i in range(len(octa)-1, -1, -1):
        digit = int(octa[i])
        digit *= exp
        exp *= 8
        summed += digit
    return summed

def main():
    q2 = int(input("Decimal to Binary: "))
    binary = decToBinary(q2)
    print(binary)

    q3 = []
    element = input("Hexadecimal to ASCII: ")
    while(element != "done"):
        q3.append(int(element,16))
        element = input("Hexadecimal to ASCII: ")
    asc = hexToASCII(q3)
    print(asc)

    q4 = int(input("Binary to Hexadecimal: "),2)
    hexa = binToHex(q4)
    print (hexa)

    q5 = input("Octal to Decimal: ")
    octa = octToDec(q5)
    print(octa)
