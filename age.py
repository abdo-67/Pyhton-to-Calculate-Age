from datetime import date
t = date.today()
t = str(t)
y = t[:4]
m = t[5:7]
d = t[8:]

year0 = int(y)
month0 = int(m)
day0 = int(d)


year1 = int(input("your year "))
month1 =int(input("your month "))
day1 = int(input("your day "))
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
        else:
            print("you have {:d} years".format(year2).strip())
            print("and {:d} months".format(month2).strip())

        if day2 < 0 :
            print("and {:d} days ".format(day2 * -1).strip())
        else:
            print("and {:d} days ".format(day2).strip())
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














