

while True:
    print("\n1.Save \n2.Show \n3.Delete \n4.Search \n-1.Exit\n")
    a1 =(input("Enter any number: "))


    if (a1 =='') or (a1 ==' '):
        continue

    elif(a1 == '1'):
        while True:
            a = input('\nEnter name: ')
            if (a == '-1'):
                print("Saved succecfully")
                break

            elif (a == "") or (a == " "):
                break

            x = a.isnumeric()

            if x is True:
                break

            else:
                a0=input("Enter number: ")
                x = a0.isnumeric()

                if x is True:
                    f = open("shopno.txt", "a")
                    f.write((a) + "           ")
                    f.write((a0) + "\n")
                    # f.write(input("Enter number: ") + "\n")
                    f.close()

                else:
                    print("Invalid")



    elif (a1 == '2'):
        print("\n*******************************************\n  Name:           Number:\n*******************************************")
        f = open("shopno.txt", "a")
        f.close()
        f = open("shopno.txt", "r")
        p = f.readlines( )

        c=0
        for i in p:
            c=c+1
            print(c,".",i .replace("\n"," "))
        f.close()

    elif (a1=='3'):
        f=open("shopno.txt","r")
        s=f.read()
        # s.replace("\n","")

        d=s.split()


        DN=input("Enter The name for Delete: ")

        x = DN.isnumeric()

        if x is True:
            continue

        elif DN in d:
            p=d.index(DN)
            d.pop(p)
            d.pop(p)
            f=open("shopno.txt","w")

            for i in range(0,len(d),2):
                str=d[i]+" "+d[i+1]+"\n"
                f.write(str)
            f.close()


            print("*******************************************\nDeleting Successful\n*******************************************\nUpdating List\n")
            f = open("shopno.txt", "a")
            f.close()
            f = open("shopno.txt", "r")
            p = f.readlines()

            c = 0
            for i in p:
                c = c + 1
                print(c, ".", i.replace("\n", " "))
            f.close()




        else:
            print("Invalid")


    elif (a1=='4'):

        f = open("shopno.txt", "a")
        f.close()
        f = open("shopno.txt", "r")
        p = f.readlines()

        c = 0
        for i in p:
            c = c + 1
            print(c, ".", i.replace("\n", " "))
        f.close()

        f = open("shopno.txt", "r")
        s = f.read()
        s.replace("\n", "")
        d = s.split()
        DN = input("\nEnter The name for Search: ")
        if DN in d:
            p = d.index(DN)
            print("\nSearching result:\n",d[p],d[p+1])
        else:
            print("Your Name is Not Found")
    else:
        print("invalied")
