

"""
This is the correct way to declare decorate
"""

code = None
money = 1000

# my decorator function
def decorator(func):
    def check():
        if type(code) is not None and code == "123":
            func()
        else:
            print("You don't have access, first you must log")
    
    return check


@decorator
def show():
    global money
    print(f"You have {money} of dolars")

    
@decorator
def more():
    global money
    money += 10

    
def log():
    global code
    code = input("Put your code: ")

    
def main():
    while True:
        print("[1] show")
        print("[2] more")
        print("[3] log")
        print("[4] exit")

        res = int(input('\n>>> '))

        if res == 1:
            show()
        
        elif res == 2:
            more()
        
        elif res == 3:
            log()
        
        else:
            break

if __name__ == "__main__":
    main()

    
