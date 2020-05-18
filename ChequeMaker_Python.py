##################################
#       Created by DINORADO      #
#                                #
#         Basila, Eadrian        #
# Pineda, Stephano Denniel M.    #
#         Ugay, Jay Mark         #
##################################

import re

global suffixes
suffixes = ["", " Thousand", " Million", " Billion", " Trillion"]

global cents
cents = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]

global ones
ones = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]

global after_ten
after_ten = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]

global tens
tens = ["Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety", "Hundred"]


def getNum_Words(number, index):
    length = len(number)

    if length > 3:
        return False

    number = number.zfill(3)
    string = ""
    hundreds_digit = ord(number[0]) - 48
    tens_digit = ord(number[1]) - 48
    ones_digit = ord(number[2]) - 48
    string += "" if number[0] == '0' else ones[hundreds_digit]
    string += " Hundred " if not string == "" else ""

    if tens_digit > 1:
        string += tens[tens_digit - 2]
        string += " "
        string += ones[ones_digit]
    elif tens_digit == 1:
        string += after_ten[(int(tens_digit + ones_digit) % 10) - 1]
    elif tens_digit == 0:
        string += ones[ones_digit]

    if string.endswith("Zero"):
        string = string[:-len("Zero")]
    else:
        string += ""

    if not len(string) == 0:
        string += suffixes[index]

    return string


def initiateProcess(number):
    while True:
        length = len(str(number))

        counter = int(length / 3) if length % 3 == 0 else int(length / 3) + 1
        counter_copy = counter
        word_representation = []

        for i in range(length - 1, -1, -3):
            word_representation.append(
                getNum_Words(str(number)[0 if i - 2 < 0 else i - 2: i + 1], counter_copy - counter))
            counter -= 1

        print("Number in Words: ", end="", flush=True)
        for s in reversed(word_representation):
            if not len(s.strip()) == 0:
                print(s + " ", end="", flush=True)

        return ""


print("*=" * 50)
print("Input should be in this format to continue: [PHP/VND/USD] [123,456,789.90]")
print("Final input should be in this format: eg. [PHP 123,456,789.90]")
print("*=" * 50)
print()
while True:

    numValue = str(input("Enter your desired Value: "))
    if "-" in numValue: 
        print("Value out of Range. Please Try again.")
        print("[Value should not be greater than 1,000,000,000,000.99 and not less than 0.01]")
        break
    
    else:

        numValue = str(numValue.replace(',', ''))
        numValue = numValue  + ".00"
        res1 = "".join(re.split("[^a-zA-Z]*", numValue))
        temp = re.findall("\d+\.\d+", numValue)
        res = list(map(float, temp)) 
        

        number = []
        moneyCurrency = ["PHP","VND","USD"]
        currencyMoney = str(res1)
        currencyValue = float(''.join(map(str, res))) 
        
        integerPart = int(currencyValue)
        decimalPart = (float(currencyValue) - int(currencyValue))
        number.append(integerPart)
        decimalPart = (round(decimalPart, 2)) * 100
        
        print()
        if (currencyMoney in moneyCurrency) and (currencyValue <= 1000000000000.99):
            
            if ((integerPart >= 1) and (decimalPart >= 0.01)) == True: 
                
                if 1 <= decimalPart < 10:
                
                    print("*=" * 50)
                    print(initiateProcess(integerPart) + currencyMoney, "and", ones[int(decimalPart)] + " Cents")
                    print("*=" * 50)
                
                elif 10 <= decimalPart < 20:
                
                    print("*=" * 50)
                    print(initiateProcess(integerPart) + currencyMoney, "and", after_ten[int(decimalPart) - 10] + " Cents")
                    print("*=" * 50)
                
                elif 20 <= decimalPart < 100:
                
                    centsA = (int(decimalPart) // 10)
                    centsB = (int(decimalPart) % 10)
                    print("*=" * 50)
                    print(initiateProcess(integerPart) + currencyMoney, "and", tens[centsA - 2], cents[centsB] + " Cents")
                    print("*=" * 50)
                
                else:
                    
                    print("*=" * 50)
                    print(initiateProcess(integerPart) + currencyMoney, "and", "Zero Cents")
                    print("*=" * 50)
                    
            elif ((integerPart >= 1) and (decimalPart == 0)) == True:
                
                print("*=" * 50)
                print(initiateProcess(integerPart) + currencyMoney, "and", "Zero Cents")
                print("*=" * 50)
                
            elif ((integerPart == 0) and (decimalPart >= 0.01)) == True: 
                
                if 1 <= decimalPart < 10:
                    
                    print("*=" * 50)
                    print("Number in Words: ", currencyMoney, ones[int(decimalPart)] + " Cents")
                    print("*=" * 50)
                    
                elif 10 <= decimalPart < 20:
                    
                    print("*=" * 50)
                    print("Number in Words: ", currencyMoney, after_ten[int(decimalPart) - 10] + " Cents")
                    print("*=" * 50)
                    
                elif 20 <= decimalPart < 100:
                    
                    centsA = (int(decimalPart) // 10)
                    centsB = (int(decimalPart) % 10)
                    print("*=" * 50)
                    print("Number in Words: ", currencyMoney, tens[centsA - 2], cents[centsB] + " Cents")
                    print("*=" * 50)
                    
                else:
                    
                    print("*=" * 50)
                    print("Value out of Range. Please Try again.")
                    print("[Value should not be greater than 1,000,000,000,000.99 and not less than 0.01]")
                    print("*=" * 50)
            
            else:
                
                print("*=" * 50)
                print("Value out of Range. Please Try again.")
                print("[Value should not be greater than 1,000,000,000,000.99 and not less than 0.01]")
                print("*=" * 50)
                
        else: 
            print("*=" * 50)
            print("Invalid Currency or Value Exceeded Maximum Threshold. Please Try again.")
            print("*=" * 50)
    break



