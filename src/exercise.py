def main():
    #write your code below this line
    inheritance = float(input("How much money have you inherited? "))
    years = int(input("How many years since death? "))

    if inheritance > 325000 and years < 3:
        print("The amount of tax is: " + str(inheritance * 1.4 - inheritance))
    elif inheritance > 325000 and years == 3:
        print("The amount of tax is: " + str(inheritance * 1.32 - inheritance))
    elif inheritance > 325000 and years == 4:
        print("The amount of tax is: " + str(inheritance * 1.24 - inheritance))
    elif inheritance > 325000 and years == 5:
        print("The amount of tax is: " + str(inheritance * 1.16 - inheritance))
    elif inheritance > 325000 and years == 6:
        print("The amount of tax is: " + str(inheritance * 1.08 - inheritance))
    else:
        print("There is no tax.")

if __name__ == '__main__':
    main()
