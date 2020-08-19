def add():
    return 5+6;

if __name__ == "__main__":
    # print(add())
    # print("the nature of this python file is ", __name__)

    #file handling

    f = open("kaviya.txt", "w")
    for i in range(10):
        f.write("Hi this is Ali \n")
    f.close()

    f= open("kaviya.txt", "r")
    print(f.read())
    f.close()

    f = open("kaviya.txt","a")
    f.write("This is append function")
    f.close()

    f= open("kaviya.txt", "r")
    print(f.read())
    f.close()