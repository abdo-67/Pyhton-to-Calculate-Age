print("." * 30)
print("Welcome you".upper().center(30 ,"."))
print("this is ages calalculator ".capitalize().center(30 ,"."))
print("." * 30)
print("\n")
from datetime import date
t = date.today()
t = str(t)
y = t[:4]                            # this for take the today's date
m = t[5:7]
d = t[8:]

year0 = int(y)            # year0 is 2022 and this....
month0 = int(m)
day0 = int(d)


year1 = int(input("please enter your year ".capitalize()))
month1 =int(input("and your month ".capitalize()))
day1 = int(input("finally your day ".capitalize()))
print("\n")

year2 = year0 - year1
month2 = month0 - month1
day2 = day0 - day1

if year1 <= 2022  and month1 <= 12 and day1 <= 31:
    if month2 == 0 and day2 == 0 :
        print("#" * 50)
        print("#" * 50)
        print(" Happy Birthday To You ".center(50,"#"))
        print("#" * 50)
        print("#" * 50)
        print("You become have {:d} years completely ".format(year2))
        print(" you are so bigger now")
        print("congratulations".upper())
    else:
        if month2 < 0 :
            print("you have {:d} years".format(year2).strip())
            print("and {:d} months".format(month2 * -1).strip())
        elif month2 > 0:
            print("you have {:d} years".format(year2).strip())
            print("and {:d} months".format(month2).strip())
        else:
            print("you have {:d} years".format(year2).strip())

        if day2 < 0 :
            print("and {:d} days ".format(day2 * -1).strip())
        elif day2 >0:
            print("and {:d} days ".format(day2).strip())
        else:
            print("")
        print("\n")
        if month0 == 4 or month0 ==6 or month0 == 8 or month0 ==11 :
            print("next your birthday after {:d} months".format(12 - month2 - 1))
            print("and {:d} days".format(30 - day2))
        elif month0 == 2:
            print("next your birthday after {:d} months".format(12 - month2 - 1))
            print("and {:d} days".format(28 - day2))
        else:
            print("next your birthday after {:d} months".format(12 - month2 - 1))
            print("and {:d} days".format(31 - day2))

else:
    print("your inputs is  not valid")