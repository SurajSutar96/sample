print("this is an alternate module with same package")

from mainmodule import square
print("you are in alternate module by accessing ",__name__)
if __name__=="__main__":
    print("we are in alternate function")
print("*"*55)
square(6)
print("you are in alternate module by accessing ",__name__)
if __name__=="__main__":
    print("we are in alternate function")
