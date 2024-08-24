
def calc_tax():
    pass

def calc_shipping():
    pass

# if we put the following code at the bottom of a package it will work as a stand-alone script
if __name__ == "__main__":
    print("Sales initialized")
    calc_tax()
    # or any initialization code can be put here
    # any code here will run if this module is executed as a stand-alone module but not when imported