def main():
    print("Calling from main function")

    passMark = 450
    student1Mark = 300
    student2Mark = 550

    msg = "You Did it" if student1Mark > passMark else "Try again"
    msg2 = "You Did it" if student2Mark > passMark else "Try again"

    print(msg, msg2)
    print(type(msg))
    print(id(msg))

        


# def subMain():
#     print("Calling from sub main")


if __name__ == '__main__':
    main()
