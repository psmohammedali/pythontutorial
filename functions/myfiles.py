# print("This is first line")
# print("This is first line")

def main():
    print("Main Method is called from the funciton")

    #entering into file
    f= open("bavana.txt","+w")
    f.write("this is Ali")
    f.close()

    #presenting in the console

    g = open("bavana.txt","r")
    print(g.read())


if __name__ == "__main__":
    main()
