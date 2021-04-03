# THIS FUNCTION RETRIEVE THE DATA

def retrieve():
    client_name = int(input("Enetr:\n1: harry food.txt\n2: rohan food.txt\n3: rishi food.txt"
                            "\n4: harry exercise.txt\n5: rohan exercise.txt\n6: rishi exercise.txt\n"))
    if client_name == 1:
        f = open("harry food.txt","r")
        print(f.read())
        f.close()
    elif client_name == 2:
        f = open("rohan food.txt", "r")
        print(f.read())
        f.close()
    elif client_name == 3:
        f = open("rishi food.txt", "r")
        print(f.read())
        f.close()
    elif client_name == 4:
        f = open("harry exercise.txt", "r")
        print(f.read())
        f.close()
    elif client_name == 5:
        f = open("rohan exercise.txt", "r")
        print(f.read())
        f.close()
    elif client_name == 6:
        f = open("rishi exercise.txt", "r")
        print(f.read())
        f.close()
    else:
        print("Wrong choice")

# THIS FUNCTION WRITES DATA

def writing():
    #  this function get time
    def getdate():
        import datetime
        return str(datetime.datetime.now())

    client_name = int(input("Enetr:\n1: harry food.txt\n2: rohan food.txt\n3: rishi food.txt"
                            "\n4: harry exercise.txt\n5: rohan exercise.txt\n6: rishi exercise.txt\n"))
    activity = input("Enter your activity: ")
    if client_name == 1:
        f = open("harry food.txt" , "a")
        f.write(getdate())
        f.write("\t")
        f.write(activity)
        f.close()
    elif client_name == 2:
        f = open("rohan food.txt", "a")
        f.write(getdate())
        f.write("\t")
        f.write(activity)
        f.close()
    elif client_name == 3:
        f = open("rishi food.txt", "a")
        f.write(getdate())
        f.write("\t")
        f.write(activity)
        f.close()
    elif client_name == 4:
        f = open("harry exercise.txt", "a")
        f.write(getdate())
        f.write("\t")
        f.write(activity)
        f.close()
    elif client_name == 5:
        f = open("rohan exercise.txt", "a")
        f.write(getdate())
        f.write("\t")
        f.write(activity)
        f.close()
    elif client_name == 6:
        f = open("rishi exercise.txt", "a")
        f.write(getdate())
        f.write("\t")
        f.write(activity)
        f.close()
    else:
        print("wrong input")


action = int(input("Enter\n1: writing\n2: retrieve\n  "))
if action == 2:
    retrieve()
elif action == 1:
    writing()
