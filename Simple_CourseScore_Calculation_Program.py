print("welcome to grade calculator:".upper().center(150))
lesson1 = str(input("lesson1: ".upper()))
lesson2 = str(input("lesson2: ".upper()))
lesson3 = str(input("lesson3: ".upper()))
 

lesson1midterm = int(input(f"{lesson1} midterm exam: ".upper()))
print(f"{lesson1} midterm exam result: ".upper(),lesson1midterm*0.4)
lesson1final = int(input(f"{lesson1} final exam: ".upper()))
print(f"{lesson1} final exam result: ".upper(),lesson1final*0.6)
print(f"{lesson1} total result: ".upper(),lesson1midterm*0.4+lesson1final*0.6)

lesson1totalresult = lesson1midterm*0.4+lesson1final*0.6
if (lesson1totalresult >=90):
    print(f"you successded {lesson1} with aa".upper())
elif (lesson1totalresult >= 85):
    print(f"you successded {lesson1} with ba".upper())
elif (lesson1totalresult >= 80):
    print(f"you successded {lesson1} with bb".upper())
elif (lesson1totalresult >= 70):
    print(f"you successded {lesson1} with cb".upper())
elif (lesson1totalresult >= 60):
    print(f"you successded {lesson1} with cc".upper())
elif (lesson1totalresult >= 55):
    print(f"you successded {lesson1} with dc".upper())
elif (lesson1totalresult >= 50):
    print(f"you successded {lesson1} with dd".upper())
else:
    print(f"unsuccessfull {lesson1}".upper())

lesson2midterm = int(input(f"{lesson2} midterm exam: ".upper()))
print(f"{lesson2} midterm exam result: ".upper(),lesson2midterm*0.4)
lesson2final = int(input(f"{lesson2} final exam: ".upper()))
print(f"{lesson2} final exam result: ".upper(),lesson2final*0.6)
print(f"{lesson2} total result:".upper(),lesson2midterm*0.4+lesson2final*0.6)

lesson2totalresult = lesson2midterm*0.4+lesson2final*0.6
if (lesson2totalresult >= 90):
    print(f"you successded {lesson2} with aa".upper())
elif (lesson2totalresult >= 85):
    print(f"you successded {lesson2} with ba".upper())
elif (lesson2totalresult >= 80):
    print(f"you successded {lesson2} with bb".upper())
elif (lesson2totalresult >= 70):
    print(f"you successded {lesson2} with cb".upper())
elif (lesson2totalresult >= 60):
    print(f"you successded {lesson2} with cc".upper())
elif (lesson2totalresult >= 55):
    print(f"you successded {lesson2} with dc".upper())
elif (lesson2totalresult >= 50):
    print(f"you successded {lesson2} with dd".upper())
else:
    print(f"unsuccessfull {lesson2}".upper())

lesson3midterm = int(input(f"{lesson3} midterm exam: ".upper()))
print(f"{lesson3} midterm exam result: ".upper(),lesson3midterm*0.4)
lesson3final = int(input(f"{lesson3} final exam: ".upper()))
print(f"{lesson3} final exam result: ".upper(),lesson3final*0.6)
print(f"{lesson3} total result: ".upper(),lesson3midterm*0.4+lesson3final*0.6)

lesson3totalresult = lesson3midterm*0.4+lesson3final*0.6
if (lesson3totalresult >= 90):
    print(f"you successded {lesson3} with aa".upper())
elif (lesson3totalresult >= 85):
    print(f"you successded {lesson3} with ba".upper())
elif (lesson3totalresult >= 80):
    print(f"you successded {lesson3} with bb".upper())
elif (lesson3totalresult >= 70):
    print(f"you successded {lesson3} with cb".upper())
elif (lesson3totalresult >= 60):
    print(f"you successded {lesson3} with cc".upper())
elif (lesson3totalresult >= 55):
    print(f"you successded {lesson3} with dc".upper())
elif (lesson3totalresult >= 50):
    print(f"you successded {lesson3} with dd".upper())
else:
    print(f"unsuccessfull {lesson3}".upper())


answer = str(input("would you like to calculate more lesson grades? (yes/no): ".upper()).upper())
if (answer == "no".upper()):
    print(f"all your lessons: ".upper(), 
              f"\n{lesson1} successded with {lesson1totalresult}".upper() if lesson1totalresult >= 50 or f"{lesson1} {lesson1totalresult}".upper() else lesson1totalresult < 50,
              f"\n{lesson2} successded with {lesson2totalresult}".upper() if lesson2totalresult >= 50 or f"{lesson2} {lesson2totalresult}".upper() else lesson2totalresult < 50,
              f"\n{lesson3} successded with {lesson3totalresult}".upper() if lesson3totalresult >= 50 or f"{lesson3} {lesson3totalresult}".upper() else lesson3totalresult < 50
            )

if (answer == "yes".upper()):
    extralesson = int(input("enter the number of lessons: ".upper()))
    if (extralesson == 1):

        lesson4 = str(input("lesson4: ".upper()))
        lesson4midterm = int(input(f"{lesson4} midterm exam: ".upper()))
        print(f"{lesson4} midterm exam result: ".upper(), lesson4midterm * 0.4)
        lesson4final = int(input(f"{lesson4} final exam: ".upper()))
        print(f"{lesson4} final exam result: ".upper(),lesson4final*0.6)
        print(f"{lesson4} total result: ".upper(),lesson4midterm*0.4+lesson4final*0.6)

        lesson4totalresult = lesson4midterm*0.4+lesson4final*0.6
        if (lesson4totalresult >= 90):
            print(f"you successded {lesson4} with aa".upper())
        elif (lesson4totalresult >= 85):
            print(f"you successded {lesson4} with ba".upper())
        elif (lesson4totalresult >= 80):
            print(f"you successded {lesson4} with bb".upper())
        elif (lesson4totalresult >= 70):
            print(f"you successded {lesson4} with cb".upper())
        elif (lesson4totalresult >= 60):
            print(f"you successded {lesson4} with cc".upper())
        elif (lesson4totalresult >= 55):
            print(f"you successded {lesson4} with dc".upper())
        elif (lesson4totalresult >= 50):
            print(f"you successded {lesson4} with dd".upper())
        else:
            print(f"unsuccessfull {lesson4}".upper())
            totalscore = [lesson1, lesson2, lesson3, lesson4]
        print(f"all your lessons: " 
              f"\n{lesson1} successded with {lesson1totalresult}".upper() if lesson1totalresult >= 50 or f"{lesson1} {lesson1totalresult}".upper() else lesson1totalresult < 50,
              f"\n{lesson2} successded with {lesson2totalresult}".upper() if lesson2totalresult >= 50 or f"{lesson2} {lesson2totalresult}".upper() else lesson2totalresult < 50,
              f"\n{lesson3} successded with {lesson3totalresult}".upper() if lesson3totalresult >= 50 or f"{lesson3} {lesson3totalresult}".upper() else lesson3totalresult < 50,
              f"\n{lesson4} successded with {lesson4totalresult}".upper() if lesson4totalresult >= 50 or f"{lesson4} {lesson4totalresult}".upper() else lesson4totalresult < 50
            )

    elif (extralesson == 2):
        
        lesson4 = str(input("lesson4: ".upper()))
        lesson4midterm = int(input(f"{lesson4} midterm exam: ".upper()))
        print(f"{lesson4} midterm exam result: ".upper(), lesson4midterm * 0.4)
        lesson4final = int(input(f"{lesson4} final exam: ".upper()))
        print(f"{lesson4} final exam result: ".upper(),lesson4final*0.6)
        print(f"{lesson4} total result: ".upper(),lesson4midterm*0.4+lesson4final*0.6)


        lesson4totalresult = lesson4midterm*0.4+lesson4final*0.6
        if (lesson4totalresult >= 90):
            print(f"you successded {lesson4} with aa".upper())
        elif (lesson4totalresult >= 85):
            print(f"you successded {lesson4} with ba".upper())
        elif (lesson4totalresult >= 80):
            print(f"you successded {lesson4} with bb".upper())
        elif (lesson4totalresult >= 70):
            print(f"you successded {lesson4} with cb".upper())
        elif (lesson4totalresult >= 60):
            print(f"you successded {lesson4} with cc".upper())
        elif (lesson4totalresult >= 55):
            print(f"you successded {lesson4} with dc".upper())
        elif (lesson4totalresult >= 50):
            print(f"you successded {lesson4} with dd".upper())
        else:
            print(f"unsuccessfull {lesson4}".upper())

        lesson5 = str(input("lesson5: ".upper()))
        lesson5midterm = int(input(f"{lesson5} midterm exam: ".upper()))
        print(f"{lesson5} midterm exam result: ".upper(), lesson5midterm * 0.4)
        lesson5final = int(input(f"{lesson5} final exam: ".upper()))
        print(f"{lesson5} final exam result: ".upper(),lesson5final*0.6)
        print(f"{lesson5} total result: ".upper(),lesson5midterm*0.4+lesson5final*0.6)

        lesson5totalresult = lesson5midterm*0.4+lesson5final*0.6
        if (lesson5totalresult >= 90):
            print(f"you successded {lesson5} with aa".upper())
        elif (lesson5totalresult >= 85):
            print(f"you successded {lesson5} with ba".upper())
        elif (lesson5totalresult >= 80):
            print(f"you successded {lesson5} with bb".upper())
        elif (lesson5totalresult >= 70):
            print(f"you successded {lesson5} with cb".upper())
        elif (lesson5totalresult >= 60):
            print(f"you successded {lesson5} with cc".upper())
        elif (lesson5totalresult >= 55):
            print(f"you successded {lesson5} with dc".upper())
        elif (lesson5totalresult >= 50):
            print(f"you successded {lesson5} with dd".upper())
        else:
            print(f"unsuccessfull {lesson5}".upper())
        print(f"all your lessons: ".upper(), 
             f"\n{lesson1} successded with {lesson1totalresult}".upper() if lesson1totalresult >= 50 or f"{lesson1} {lesson1totalresult}".upper() else lesson1totalresult < 50,
             f"\n{lesson2} successded with {lesson2totalresult}".upper() if lesson2totalresult >= 50 or f"{lesson2} {lesson2totalresult}".upper() else lesson2totalresult < 50,
             f"\n{lesson3} successded with {lesson3totalresult}".upper() if lesson3totalresult >= 50 or f"{lesson3} {lesson3totalresult}".upper() else lesson3totalresult < 50,
             f"\n{lesson4} successded with {lesson4totalresult}".upper() if lesson4totalresult >= 50 or f"{lesson4} {lesson4totalresult}".upper() else lesson4totalresult < 50,
             f"\n{lesson5} successded with {lesson5totalresult}".upper() if lesson5totalresult >= 50 or f"{lesson5} {lesson5totalresult}".upper() else lesson5totalresult < 50
            )
              
    elif (extralesson == 3):

        lesson4 = str(input("lesson4: ".upper()))
        lesson4midterm = int(input(f"{lesson4} midterm exam: ".upper()))
        print(f"{lesson4} midterm exam result: ".upper(), lesson4midterm * 0.4)
        lesson4final = int(input(f"{lesson4} final exam :".upper()))
        print(f"{lesson4} final exam result: ".upper(),lesson4final*0.6)
        print(f"{lesson4} total result: ".upper(),lesson4midterm*0.4+lesson4final*0.6)


        lesson4totalresult = lesson4midterm*0.4+lesson4final*0.6
        if (lesson4totalresult >= 90):
            print(f"you successded {lesson4} with aa".upper())
        elif (lesson4totalresult >= 85):
            print(f"you successded {lesson4} with ba".upper())
        elif (lesson4totalresult >= 80):
            print(f"you successded {lesson4} with bb".upper())
        elif (lesson4totalresult >= 70):
            print(f"you successded {lesson4} with cb".upper())
        elif (lesson4totalresult >= 60):
            print(f"you successded {lesson4} with cc".upper())
        elif (lesson4totalresult >= 55):
            print(f"you successded {lesson4} with dc".upper())
        elif (lesson4totalresult >= 50):
            print(f"you successded {lesson4} with dd".upper())
        else:
            print(f"unsuccessfull {lesson4}".upper())

        lesson5 = str(input("lesson5: ".upper()))
        lesson5midterm = int(input(f"{lesson5} midterm exam: ".upper()))
        print(f"{lesson5} midterm exam result: ".upper(), lesson5midterm * 0.4)
        lesson5final = int(input(f"{lesson5} final exam: ".upper()))
        print(f"{lesson5} final exam result: ".upper(),lesson5final*0.6)
        print(f"{lesson5} total result: ".upper(),lesson5midterm*0.4+lesson5final*0.6)

        lesson5totalresult = lesson5midterm*0.4+lesson5final*0.6
        if (lesson5totalresult >= 90):
            print(f"you successded {lesson5} with aa".upper())
        elif (lesson5totalresult >= 85):
            print(f"you successded {lesson5} with ba".upper())
        elif (lesson5totalresult >= 80):
            print(f"you successded {lesson5} with bb".upper())
        elif (lesson5totalresult >= 70):
            print(f"you successded {lesson5} with cb".upper())
        elif (lesson5totalresult >= 60):
            print(f"you successded {lesson5} with cc".upper())
        elif (lesson5totalresult >= 55):
            print(f"you successded {lesson5} with dc".upper())
        elif (lesson5totalresult >= 50):
            print(f"you successded {lesson5} with dd".upper())
        else:
            print(f"unsuccessfull {lesson5}".upper())

        lesson6 = str(input("lesson6: ".upper()))
        lesson6midterm = int(input(f"{lesson6} midterm exam: ".upper()))
        print(f"{lesson6} midterm exam result: ".upper(), lesson6midterm * 0.4)
        lesson6final = int(input(f"{lesson6} final exam: ".upper()))
        print(f"{lesson6} final exam result: ".upper(),lesson6final*0.6)
        print(f"{lesson6} total result: ".upper(),lesson6midterm*0.4+lesson6final*0.6)

        lesson6totalresult = lesson6midterm*0.4+lesson6final*0.6
        if (lesson6totalresult >= 90):
            print(f"you successded {lesson6} with aa".upper())
        elif (lesson6totalresult >= 85):
            print(f"you successded {lesson6} with ba".upper())
        elif (lesson6totalresult >= 80):
            print(f"you successded {lesson6} with bb".upper())
        elif (lesson6totalresult >= 70):
            print(f"you successded {lesson6} with cb".upper())
        elif (lesson6totalresult >= 60):
            print(f"you successded {lesson6} with cc".upper())
        elif (lesson6totalresult >= 55):
            print(f"you successded {lesson6} with dc".upper())
        elif (lesson6totalresult >= 50):
            print(f"you successded {lesson6} with dd".upper())
        else:
            print(f"unsuccessfull {lesson6}".upper())
        print(f"all your lessons: ".upper(),
              f"\n{lesson1} successded with {lesson1totalresult}".upper() if lesson1totalresult >= 50 or f"{lesson1} {lesson1totalresult}".upper() else lesson1totalresult < 50 ,
              f"\n{lesson2} successded with {lesson2totalresult}".upper() if lesson2totalresult >= 50 or f"{lesson2} {lesson2totalresult}".upper() else lesson2totalresult < 50 ,
              f"\n{lesson3} successded with {lesson3totalresult}".upper() if lesson3totalresult >= 50 or f"{lesson3} {lesson3totalresult}".upper() else lesson3totalresult < 50 ,
              f"\n{lesson4} successded with {lesson4totalresult}".upper() if lesson4totalresult >= 50 or f"{lesson4} {lesson4totalresult}".upper() else lesson4totalresult < 50 ,
              f"\n{lesson5} successded with {lesson5totalresult}".upper() if lesson5totalresult >= 50 or f"{lesson5} {lesson5totalresult}".upper() else lesson5totalresult < 50 ,
              f"\n{lesson6} successded with {lesson6totalresult}".upper() if lesson6totalresult >= 50 or f"{lesson6} {lesson6totalresult}".upper() else lesson6totalresult < 50
            )


    elif (extralesson == 4):
        lesson4 = str(input("lesson4: ".upper()))
        lesson4midterm = int(input(f"{lesson4} midterm exam: ".upper()))
        print(f"{lesson4} midterm exam result: ".upper(), lesson4midterm * 0.4)
        lesson4final = int(input(f"{lesson4} final exam: ".upper()))
        print(f"{lesson4} final exam result: ".upper(),lesson4final*0.6)
        print(f"{lesson4} total result: ".upper(),lesson4midterm*0.4+lesson4final*0.6)


        lesson4totalresult = lesson4midterm*0.4+lesson4final*0.6
        if (lesson4totalresult >= 90):
            print(f"you successded {lesson4} with aa".upper())
        elif (lesson4totalresult >= 85):
            print(f"you successded {lesson4} with ba".upper())
        elif (lesson4totalresult >= 80):
            print(f"you successded {lesson4} with bb".upper())
        elif (lesson4totalresult >= 70):
            print(f"you successded {lesson4} with cb".upper())
        elif (lesson4totalresult >= 60):
            print(f"you successded {lesson4} with cc".upper())
        elif (lesson4totalresult >= 55):
            print(f"you successded {lesson4} with dc".upper())
        elif (lesson4totalresult >= 50):
            print(f"you successded {lesson4} with dd".upper())
        else:
            print(f"unsuccessfull {lesson4}".upper())

        lesson5 = str(input("lesson5: ".upper()))
        lesson5midterm = int(input(f"{lesson5} midterm exam: ".upper()))
        print(f"{lesson5} midterm exam result: ".upper(), lesson5midterm * 0.4)
        lesson5final = int(input(f"{lesson5} final exam: ".upper()))
        print(f"{lesson5} final exam result: ".upper(),lesson5final*0.6)
        print(f"{lesson5} total result: ".upper(),lesson5midterm*0.4+lesson5final*0.6)

        lesson5totalresult = lesson5midterm*0.4+lesson5final*0.6
        if (lesson5totalresult >= 90):
            print(f"you successded {lesson5} with aa".upper())
        elif (lesson5totalresult >= 85):
            print(f"you successded {lesson5} with ba".upper())
        elif (lesson5totalresult >= 80):
            print(f"you successded {lesson5} with bb".upper())
        elif (lesson5totalresult >= 70):
            print(f"you successded {lesson5} with cb".upper())
        elif (lesson5totalresult >= 60):
            print(f"you successded {lesson5} with cc".upper())
        elif (lesson5totalresult >= 55):
            print(f"you successded {lesson5} with dc".upper())
        elif (lesson5totalresult >= 50):
            print(f"you successded {lesson5} with dd".upper())
        else:
            print(f"unsuccessfull {lesson5}".upper())

        lesson6 = str(input("lesson6: ".upper()))
        lesson6midterm = int(input(f"{lesson6} midterm exam: ".upper()))
        print(f"{lesson6} midterm exam result: ".upper(), lesson6midterm * 0.4)
        lesson6final = int(input(f"{lesson6} final exam: ".upper()))
        print(f"{lesson6} final exam result: ".upper(),lesson6final*0.6)
        print(f"{lesson6} total result: ".upper(),lesson6midterm*0.4+lesson6final*0.6)

        lesson6totalresult = lesson6midterm*0.4+lesson6final*0.6
        if (lesson6totalresult >= 90):
            print(f"you successded {lesson6} with aa".upper())
        elif (lesson6totalresult >= 85):
            print(f"you successded {lesson6} with ba".upper())
        elif (lesson6totalresult >= 80):
            print(f"you successded {lesson6} with bb".upper())
        elif (lesson6totalresult >= 70):
            print(f"you successded {lesson6} with cb".upper())
        elif (lesson6totalresult >= 60):
            print(f"you successded {lesson6} with cc".upper())
        elif (lesson6totalresult >= 55):
            print(f"you successded {lesson6} with dc".upper())
        elif (lesson6totalresult >= 50):
            print(f"you successded {lesson6} with dd".upper())
        else:
            print(f"unsuccessfull {lesson6}".upper())


        lesson7 = str(input("lesson7: ".upper()))
        lesson7midterm = int(input(f"{lesson7} midterm exam: ".upper()))
        print(f"{lesson7} midterm exam result: ".upper(), lesson7midterm * 0.4)
        lesson7final = int(input(f"{lesson7} final exam: ".upper()))
        print(f"{lesson7} final exam result: ".upper(),lesson7final*0.6)
        print(f"{lesson7} total result: ".upper(),lesson7midterm*0.4+lesson7final*0.6)

        lesson7totalresult = lesson7midterm*0.4+lesson7final*0.6
        if (lesson7totalresult >= 90):
            print(f"you successded {lesson7} with aa".upper())
        elif (lesson7totalresult >= 85):
            print(f"you successded {lesson7} with ba".upper())
        elif (lesson7totalresult >= 80):
            print(f"you successded {lesson7} with bb".upper())
        elif (lesson7totalresult >= 70):
            print(f"you successded {lesson7} with cb".upper())
        elif (lesson7totalresult >= 60):
            print(f"you successded {lesson7} with cc".upper())
        elif (lesson7totalresult >= 55):
            print(f"you successded {lesson7} with dc".upper())
        elif (lesson7totalresult >= 50):
            print(f"you successded {lesson7} with dd".upper())
        else:
            print(f"unsuccessfull {lesson7}".upper())
        
        print(f"all your lessons: ".upper(), 
              f"\n{lesson1} successded with {lesson1totalresult}".upper() if lesson1totalresult >= 50 or f"{lesson1} {lesson1totalresult}".upper() else lesson1totalresult < 50,
              f"\n{lesson2} successded with {lesson2totalresult}".upper() if lesson2totalresult >= 50 or f"{lesson2} {lesson2totalresult}".upper() else lesson2totalresult < 50,
              f"\n{lesson3} successded with {lesson3totalresult}".upper() if lesson3totalresult >= 50 or f"{lesson3} {lesson3totalresult}".upper() else lesson3totalresult < 50,
              f"\n{lesson4} successded with {lesson4totalresult}".upper() if lesson4totalresult >= 50 or f"{lesson4} {lesson4totalresult}".upper() else lesson4totalresult < 50,
              f"\n{lesson5} successded with {lesson5totalresult}".upper() if lesson5totalresult >= 50 or f"{lesson5} {lesson5totalresult}".upper() else lesson5totalresult < 50,
              f"\n{lesson6} successded with {lesson6totalresult}".upper() if lesson6totalresult >= 50 or f"{lesson6} {lesson6totalresult}".upper() else lesson6totalresult < 50,
              f"\n{lesson7} successded with {lesson7totalresult}".upper() if lesson7totalresult >= 50 or f"{lesson7} {lesson7totalresult}".upper() else lesson7totalresult < 50
            )


        
        
        

