class Overage(Exception):
    pass
def oops():
    raise Overage()
try:
    num=int(input("enter your age: "))
    if num>20:
        oops()
    elif num==1:
        print("num is >10")
    else:
        print("congrats u have been selected! ")
except Overage:
    print("sorry! ur age is above 20!")
except ValueError:
    print("please enter in integer!!")
except:
    print("something is wrong!")
finally:
    print("finally!")


