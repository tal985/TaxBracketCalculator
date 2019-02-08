import sys
import os
import json

#Iterative tax calculates based on JSON of tax brackets
def jsonITax(money, userfile):
    
    data = json.load(open(userfile))
    reverse = []
    owe = 0.0

    for bracket in data:
        reverse.insert(0, data[bracket])

    for bracket in reverse:
        if bracket[0] <= money:
            temp = (money - bracket[0] + 1)
            if bracket[0] == 0:
                temp -= 1
            owe += temp * bracket[2]
            money -= temp           
            
    return owe

def main():
    print ("The amount of taxes for " + sys.argv[1] + " is " + str(jsonITax(int(sys.argv[1]), sys.argv[2])))

if __name__ == "__main__":
    main()

