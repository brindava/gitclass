good_credit = input("Do you have good credit status: ")
value = 1000000
if good_credit:
    good_value = (value - value * 0.1)
    print("You get 10 percent down which is " + str(good_value))
else:
    bad_value = (value - value * 0.2)
    print("You get 20 percent down which is " + str(bad_value)) 