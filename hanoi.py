A = [1, 2, 3, 4]
B = [0, 0, 0, 0]
C = [0, 0, 0, 0]

invalid = False
holding = 0
lowest = True
n = 1
l = 0
playing = True
def read():
    print(A[0], B[0], C[0])
    print(A[1], B[1], C[1])
    print(A[2], B[2], C[2])
    print(A[3], B[3], C[3])
    print("holding", holding)

read()

while playing:
    if C == [1, 2, 3, 4]:
        print("you won!")
        break
    choice = input("A, B or C? ")
    if holding == 0:
        if choice == "A":
            n = 1
            search = True
            while search:
                if n not in A:
                    n += 1
                    if n > 4:
                        n = 0
                else:
                    break
            holding = n
            A.remove(n)
            A.insert(n-1, 0)
            read()
        elif choice == "B":
            n = 1
            search = True
            while search:
                if n not in B:
                    n += 1
                    if n > 4:
                        n = 0
                else:
                    break
            holding = n
            B.remove(n)
            B.insert(n-1, 0)
            read()
        elif choice == "C":
            n = 1
            search = True
            while search:
                if n not in C:
                    n += 1
                    if n > 4:
                        n = 0
                else:
                    break
            holding = n
            C.remove(n)
            C.insert(n-1, 0)
            read()
    else:
        if choice == "A":
            invalid = False
            l = -1
            for number in A:
                if A[l + 1] != 0:
                    if holding > A[l + 1]:
                        invalid = True
                        break
                    else:
                        invalid == False
                        break
                elif A[l + 1] == 0:
                    l += 1
            if invalid == False:
                A.pop(l)
                A.insert(l, holding)
                read()
                holding = 0
            elif invalid == True:
                print("cant place on a smaller piece")
                holding = holding
                read()
        if choice == "B":
            invalid = False
            l = -1
            for number in B:
                if B[l + 1] != 0:
                    if holding > B[l + 1]:
                        invalid = True
                        break
                    else:
                        invalid == False
                        break
                elif B[l + 1] == 0:
                    l += 1
            if invalid == False:
                B.pop(l)
                B.insert(l, holding)
                read()
                holding = 0
            elif invalid == True:
                print("cant place on a smaller piece")
                holding = holding
                read()
        if choice == "C":
            invalid = False
            l = -1
            for number in C:
                if C[l + 1] != 0:
                    if holding > C[l + 1]:
                        invalid = True
                        break
                    else:
                        invalid == False
                        break
                elif C[l + 1] == 0:
                    l += 1
            if invalid == False:
                C.pop(l)
                C.insert(l, holding)
                read()
                holding = 0
            elif invalid == True:
                print("cant place on a smaller piece")
                holding = holding
                read()