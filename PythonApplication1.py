call = ""
total = 0    
items = ""
inputformat = ""

def adding_report(num):
        

        numStr = num
        
        if numStr.isdigit():
            numInt = int(num)
            
            if numInt < 0:
                print("invalid input, number must be positive")
            else:
                items = num + " "
               
                total = total + numInt

        elif inputformat == "A":
            print("Items: ", items)

        elif inputformat == "T":
            print(total)
            return total

        else:
            print("Invalid Input")


while inputformat != "Q":
        
        call = input("Input an integer to add to the total or 'Q' to quit: ")
        
        inputformat = call.upper()
        
        total = adding_report(inputformat)

