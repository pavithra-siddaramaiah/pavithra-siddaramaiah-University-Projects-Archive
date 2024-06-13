def getInteger(label):
    while (True):
        try:
            n = int(input(label+"\n>>> "))
            return n
        except:
            print("Please enter the integer value.")


def getIntegerInRange(label, min, max):
    while (True):
        try:
            n = int(input(label+"\n>>> "))
            if (n <= max and n >= min):
                return n
            else:
                print(
                    f"Please provide value in range between ${min} and ${max}.")
        except:
            print("Please enter the integer value.")

def getString(label):
    return input(label+"\n>>> ")


def showMessage(message):
    print(message)