from menu.owner import *
from menu.customer import *
from entity.User import *
if __name__ == "__main__":
    while (True):
        choice = getIntegerInRange(
            "Choose User Type:\n1.Owner\n2.Customer\n3.Exit", 1, 3)
        if choice == 1:
            ownerMainMenu()
        elif choice == 2:
            customerMainMenu()
        else:
            break
