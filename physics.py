print("Welcome to COS 101")
print("Name: Adeonigbagbe Oyindolapo Charles ")
print("Matric number: BHU/24/04/09/003 ")

def a():
    velocity = float(input("enter your value for velocity: "))
    time = float(input("enter your value for time: "))
 #   acceleration= velocity * time
    output = str(velocity * time)
    print("Acceleration= :" +output+"m/s^2" )

def b():
    distance = float(input("enter your value for distance: "))
    time = float(input("enter your value for time: "))
 #   speed= distance / time
    output = str(distance / time)
    print("Speed= :" + output+"m/s")

def c():
    force = float(input("enter your value for force: "))
    distance = float(input("enter your value for distance: "))
 #   work= force * distance
    output = str(force * distance)
    print("Work= " + output+"J")

def d():
    charge = float(input("enter your value for charge: "))
    time = float(input("enter your value for time: "))
 #   current= charge * time
    output = str(charge / time)
    print("Current= " + output+"A")

def e():
    work = float(input("Enter your value for work: "))
    time = float(input("enter your value for time: "))
 #   energy= work / time
    output = str(work / time)
    print("Energy= " + output+"J")

def main():
    user_choice = input("Enter operation a(acceleration),b(speed),c(work),d(current),e(energy): " )

    if user_choice == "a":
        a()
    elif user_choice == "b":
        b()
    elif user_choice == "c":
        c()
    elif user_choice == "d":
        d()
    elif user_choice == "e":
        e()
if __name__ == '__main__':
    main()