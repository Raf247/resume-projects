#program to calculate dad's money from work
salary = 17
days = int(input("Enter the number of days he worked: "))

if days == 6:
    day1In = float(input("Day 1 - Enter the time of entry: "))
    day1Out = float(input("Day 1 - Enter the time of leave: "))
    day1Out += 12

    day2In = float(input("Day 2 - Enter the time of entry: "))
    day2Out = float(input("Day 2 - Enter the time of leave: "))
    day2Out += 12

    day3In = float(input("Day 3 - Enter the time of entry: "))
    day3Out = float(input("Day 3 - Enter the time of leave: "))
    day3Out += 12

    day4In = float(input("Day 4 - Enter the time of entry: "))
    day4Out = float(input("Day 4 - Enter the time of leave: "))
    day4Out += 12
    
    day5In = float(input("Day 5 - Enter the time of entry: "))
    day5Out = float(input("Day 5 - Enter the time of leave: "))
    day5Out += 12

    day6In = float(input("Day 6 - Enter the time of entry: "))
    day6Out = float(input("Day 6 - Enter the time of leave: "))
    day6Out += 12

    didNotHaveBreak = int(input('How many days did he not have a lunch?: '))

    totalMoney = 0

    # money for day 1
    day1Hours = int(day1Out - day1In)
    day1Minutes = 0
    if round(day1In * 100 % 100) == 0:
        day1InMinutes = abs(round(day1In * 100 % 100))
    else:
        day1InMinutes = abs(round(day1In * 100 % 100) - 60)
    
    day1OutMinutes = round(day1Out * 100 % 100)
    
    if (day1InMinutes + day1OutMinutes) >= 60:
        day1Minutes = (day1InMinutes + day1OutMinutes) % 60
    else:
        day1Minutes = day1InMinutes + day1OutMinutes
    
    day1Money = ((day1Hours *salary) + ((salary / 60) * day1Minutes))
    totalMoney += day1Money

    # money for day 2
    day2Hours = int(day2Out - day2In)
    day2Minutes = 0
    if round(day2In * 100 % 100) == 0:
        day2InMinutes = abs(round(day2In * 100 % 100))
    else:
        day2InMinutes = abs(round(day2In * 100 % 100) - 60)
    
    day2OutMinutes = round(day2Out * 100 % 100)
    
    if (day2InMinutes + day2OutMinutes) >= 60:
        day2Minutes = (day2InMinutes + day2OutMinutes) % 60
    else:
        day2Minutes = day2InMinutes + day2OutMinutes
    
    day2Money = ((day2Hours *salary) + ((salary / 60) * day2Minutes))
    totalMoney += day2Money

    #money for day 3
    day3Hours = int(day3Out - day3In)
    day3Minutes = 0
    if round(day3In * 100 % 100) == 0:
        day3InMinutes = abs(round(day3In * 100 % 100))
    else:
        day3InMinutes = abs(round(day3In * 100 % 100) - 60)
    
    day3OutMinutes = round(day3Out * 100 % 100)
    
    if (day3InMinutes + day3OutMinutes) >= 60:
        day3Minutes = (day3InMinutes + day3OutMinutes) % 60
    else:
        day3Minutes = day3InMinutes + day3OutMinutes
    day3Money = ((day3Hours *salary) + ((salary / 60) * day3Minutes))
    totalMoney += day3Money

    #money for day 4
    day4Hours = int(day4Out - day4In)
    day4Minutes = 0
    if round(day4In * 100 % 100) == 0:
        day4InMinutes = abs(round(day4In * 100 % 100))
    else:
        day4InMinutes = abs(round(day4In * 100 % 100) - 60)
    
    day4OutMinutes = round(day4Out * 100 % 100)
    
    if (day4InMinutes + day4OutMinutes) >= 60:
        day4Minutes = (day4InMinutes + day4OutMinutes) % 60
    else:
        day4Minutes = day4InMinutes + day4OutMinutes
    day4Money = ((day4Hours *salary) + ((salary / 60) * day4Minutes))
    totalMoney += day4Money

    #money for day 5
    day5Hours = int(day5Out - day5In)
    day5Minutes = 0
    if round(day5In * 100 % 100) == 0:
        day5InMinutes = abs(round(day5In * 100 % 100))
    else:
        day5InMinutes = abs(round(day5In * 100 % 100) - 60)
    
    day5OutMinutes = round(day5Out * 100 % 100)
    
    if (day5InMinutes + day5OutMinutes) >= 60:
        day5Minutes = (day5InMinutes + day5OutMinutes) % 60
    else:
        day5Minutes = day5InMinutes + day5OutMinutes
    day5Money = ((day5Hours *salary) + ((salary / 60) * day5Minutes))
    totalMoney += day5Money

    #money for day 6
    day6Hours = int(day6Out - day6In)
    day6Minutes = 0
    if round(day6In * 100 % 100) == 0:
        day6InMinutes = abs(round(day6In * 100 % 100))
    else:
        day6InMinutes = abs(round(day6In * 100 % 100) - 60)
    
    day6OutMinutes = round(day6Out * 100 % 100)
    
    if (day6InMinutes + day6OutMinutes) >= 60:
        day6Minutes = (day6InMinutes + day5OutMinutes) % 60
    else:
        day6Minutes = day6InMinutes + day6OutMinutes
    day6Money = ((day6Hours *salary) + ((salary / 60) * day6Minutes))
    totalMoney += day6Money

    #total amount
    totalMoney = totalMoney - (8.5 * (days - didNotHaveBreak))
    totalMoney += 0

    print("day 1 = $" + str(day1Money))
    print("day 2 = $" + str(day2Money))
    print("day 3 = $" + str(day3Money))
    print("day 4 = $" + str(day4Money))
    print("day 5 = $" + str(day5Money))
    print("day 6 = $" + str(day6Money))
    
    totalMoney = round(totalMoney, 2)
    print("Your total amount is $" + str(totalMoney))



elif days == 5:
    day1In = float(input("Day 1 - Enter the time of entry: "))
    day1Out = float(input("Day 1 - Enter the time of leave: "))
    day1Out += 12

    day2In = float(input("Day 2 - Enter the time of entry: "))
    day2Out = float(input("Day 2 - Enter the time of leave: "))
    day2Out += 12

    day3In = float(input("Day 3 - Enter the time of entry: "))
    day3Out = float(input("Day 3 - Enter the time of leave: "))
    day3Out += 12

    day4In = float(input("Day 4 - Enter the time of entry: "))
    day4Out = float(input("Day 4 - Enter the time of leave: "))
    day4Out += 12
    
    day5In = float(input("Day 5 - Enter the time of entry: "))
    day5Out = float(input("Day 5 - Enter the time of leave: "))
    day5Out += 12

    didNotHaveBreak = int(input('How many days did he not have a lunch?: '))

    totalMoney = 0

    # money for day 1
    day1Hours = int(day1Out - day1In)
    day1Minutes = 0
    if round(day1In * 100 % 100) == 0:
        day1InMinutes = abs(round(day1In * 100 % 100))
    else:
        day1InMinutes = abs(round(day1In * 100 % 100) - 60)
    
    day1OutMinutes = round(day1Out * 100 % 100)
    
    if (day1InMinutes + day1OutMinutes) >= 60:
        day1Minutes = (day1InMinutes + day1OutMinutes) % 60
    else:
        day1Minutes = day1InMinutes + day1OutMinutes
    
    day1Money = ((day1Hours *salary) + ((salary / 60) * day1Minutes))
    totalMoney += day1Money

    # money for day 2
    day2Hours = int(day2Out - day2In)
    day2Minutes = 0
    if round(day2In * 100 % 100) == 0:
        day2InMinutes = abs(round(day2In * 100 % 100))
    else:
        day2InMinutes = abs(round(day2In * 100 % 100) - 60)
    
    day2OutMinutes = round(day2Out * 100 % 100)
    
    if (day2InMinutes + day2OutMinutes) >= 60:
        day2Minutes = (day2InMinutes + day2OutMinutes) % 60
    else:
        day2Minutes = day2InMinutes + day2OutMinutes
    
    day2Money = ((day2Hours *salary) + ((salary / 60) * day2Minutes))
    totalMoney += day2Money

    #money for day 3
    day3Hours = int(day3Out - day3In)
    day3Minutes = 0
    if round(day3In * 100 % 100) == 0:
        day3InMinutes = abs(round(day3In * 100 % 100))
    else:
        day3InMinutes = abs(round(day3In * 100 % 100) - 60)
    
    day3OutMinutes = round(day3Out * 100 % 100)
    
    if (day3InMinutes + day3OutMinutes) >= 60:
        day3Minutes = (day3InMinutes + day3OutMinutes) % 60
    else:
        day3Minutes = day3InMinutes + day3OutMinutes
    day3Money = ((day3Hours *salary) + ((salary / 60) * day3Minutes))
    totalMoney += day3Money

    #money for day 4
    day4Hours = int(day4Out - day4In)
    day4Minutes = 0
    if round(day4In * 100 % 100) == 0:
        day4InMinutes = abs(round(day4In * 100 % 100))
    else:
        day4InMinutes = abs(round(day4In * 100 % 100) - 60)
    
    day4OutMinutes = round(day4Out * 100 % 100)
    
    if (day4InMinutes + day4OutMinutes) >= 60:
        day4Minutes = (day4InMinutes + day4OutMinutes) % 60
    else:
        day4Minutes = day4InMinutes + day4OutMinutes
    day4Money = ((day4Hours *salary) + ((salary / 60) * day4Minutes))
    totalMoney += day4Money

    #money for day 5
    day5Hours = int(day5Out - day5In)
    day5Minutes = 0
    if round(day5In * 100 % 100) == 0:
        day5InMinutes = abs(round(day5In * 100 % 100))
    else:
        day5InMinutes = abs(round(day5In * 100 % 100) - 60)
    
    day5OutMinutes = round(day5Out * 100 % 100)
    
    if (day5InMinutes + day5OutMinutes) >= 60:
        day5Minutes = (day5InMinutes + day5OutMinutes) % 60
    else:
        day5Minutes = day5InMinutes + day5OutMinutes
    day5Money = ((day5Hours *salary) + ((salary / 60) * day5Minutes))
    totalMoney += day5Money

    #total amount
    totalMoney = totalMoney - (8.5 * (days - didNotHaveBreak))
    totalMoney += 0

    print("day 1 = $" + str(day1Money))
    print("day 2 = $" + str(day2Money))
    print("day 3 = $" + str(day3Money))
    print("day 4 = $" + str(day4Money))
    print("day 5 = $" + str(day5Money))
    
    totalMoney = round(totalMoney, 2)
    print("Your total amount is $" + str(totalMoney))




elif days == 4:
    day1In = float(input("Day 1 - Enter the time of entry: "))
    day1Out = float(input("Day 1 - Enter the time of leave: "))
    day1Out += 12

    day2In = float(input("Day 2 - Enter the time of entry: "))
    day2Out = float(input("Day 2 - Enter the time of leave: "))
    day2Out += 12

    day3In = float(input("Day 3 - Enter the time of entry: "))
    day3Out = float(input("Day 3 - Enter the time of leave: "))
    day3Out += 12

    day4In = float(input("Day 4 - Enter the time of entry: "))
    day4Out = float(input("Day 4 - Enter the time of leave: "))
    day4Out += 12

    didNotHaveBreak = int(input('How many days did he not have a lunch?: '))

    totalMoney = 0

    # money for day 1
    day1Hours = int(day1Out - day1In)
    day1Minutes = 0
    if round(day1In * 100 % 100) == 0:
        day1InMinutes = abs(round(day1In * 100 % 100))
    else:
        day1InMinutes = abs(round(day1In * 100 % 100) - 60)
    
    day1OutMinutes = round(day1Out * 100 % 100)
    
    if (day1InMinutes + day1OutMinutes) >= 60:
        day1Minutes = (day1InMinutes + day1OutMinutes) % 60
    else:
        day1Minutes = day1InMinutes + day1OutMinutes
    
    day1Money = ((day1Hours *salary) + ((salary / 60) * day1Minutes))
    totalMoney += day1Money

    # money for day 2
    day2Hours = int(day2Out - day2In)
    day2Minutes = 0
    if round(day2In * 100 % 100) == 0:
        day2InMinutes = abs(round(day2In * 100 % 100))
    else:
        day2InMinutes = abs(round(day2In * 100 % 100) - 60)
    
    day2OutMinutes = round(day2Out * 100 % 100)
    
    if (day2InMinutes + day2OutMinutes) >= 60:
        day2Minutes = (day2InMinutes + day2OutMinutes) % 60
    else:
        day2Minutes = day2InMinutes + day2OutMinutes
    
    day2Money = ((day2Hours *salary) + ((salary / 60) * day2Minutes))
    totalMoney += day2Money

    #money for day 3
    day3Hours = int(day3Out - day3In)
    day3Minutes = 0
    if round(day3In * 100 % 100) == 0:
        day3InMinutes = abs(round(day3In * 100 % 100))
    else:
        day3InMinutes = abs(round(day3In * 100 % 100) - 60)
    
    day3OutMinutes = round(day3Out * 100 % 100)
    
    if (day3InMinutes + day3OutMinutes) >= 60:
        day3Minutes = (day3InMinutes + day3OutMinutes) % 60
    else:
        day3Minutes = day3InMinutes + day3OutMinutes
    day3Money = ((day3Hours *salary) + ((salary / 60) * day3Minutes))
    totalMoney += day3Money

    #money for day 4
    day4Hours = int(day4Out - day4In)
    day4Minutes = 0
    if round(day4In * 100 % 100) == 0:
        day4InMinutes = abs(round(day4In * 100 % 100))
    else:
        day4InMinutes = abs(round(day4In * 100 % 100) - 60)
    
    day4OutMinutes = round(day4Out * 100 % 100)
    
    if (day4InMinutes + day4OutMinutes) >= 60:
        day4Minutes = (day4InMinutes + day4OutMinutes) % 60
    else:
        day4Minutes = day4InMinutes + day4OutMinutes
    day4Money = ((day4Hours *salary) + ((salary / 60) * day4Minutes))
    totalMoney += day4Money

    #total amount
    totalMoney = totalMoney - (8.5 * (days - didNotHaveBreak))
    totalMoney += 0

    print("day 1 = $" + str(day1Money))
    print("day 2 = $" + str(day2Money))
    print("day 3 = $" + str(day3Money))
    print("day 4 = $" + str(day4Money))
    
    totalMoney = round(totalMoney, 2)
    print("Your total amount is $" + str(totalMoney))

    


elif days == 3:
    day1In = float(input("Day 1 - Enter the time of entry: "))
    day1Out = float(input("Day 1 - Enter the time of leave: "))
    day1Out += 12

    day2In = float(input("Day 2 - Enter the time of entry: "))
    day2Out = float(input("Day 2 - Enter the time of leave: "))
    day2Out += 12

    day3In = float(input("Day 3 - Enter the time of entry: "))
    day3Out = float(input("Day 3 - Enter the time of leave: "))
    day3Out += 12

    didNotHaveBreak = int(input('How many days did he not have a lunch?: '))

    totalMoney = 0

    # money for day 1
    day1Hours = int(day1Out - day1In)
    day1Minutes = 0
    if round(day1In * 100 % 100) == 0:
        day1InMinutes = abs(round(day1In * 100 % 100))
    else:
        day1InMinutes = abs(round(day1In * 100 % 100) - 60)
    
    day1OutMinutes = round(day1Out * 100 % 100)
    
    if (day1InMinutes + day1OutMinutes) >= 60:
        day1Minutes = (day1InMinutes + day1OutMinutes) % 60
    else:
        day1Minutes = day1InMinutes + day1OutMinutes
    
    day1Money = ((day1Hours *salary) + ((salary / 60) * day1Minutes))
    totalMoney += day1Money

    # money for day 2
    day2Hours = int(day2Out - day2In)
    day2Minutes = 0
    if round(day2In * 100 % 100) == 0:
        day2InMinutes = abs(round(day2In * 100 % 100))
    else:
        day2InMinutes = abs(round(day2In * 100 % 100) - 60)
    
    day2OutMinutes = round(day2Out * 100 % 100)
    
    if (day2InMinutes + day2OutMinutes) >= 60:
        day2Minutes = (day2InMinutes + day2OutMinutes) % 60
    else:
        day2Minutes = day2InMinutes + day2OutMinutes
    
    day2Money = ((day2Hours *salary) + ((salary / 60) * day2Minutes))
    totalMoney += day2Money

    #money for day 3
    day3Hours = int(day3Out - day3In)
    day3Minutes = 0
    if round(day3In * 100 % 100) == 0:
        day3InMinutes = abs(round(day3In * 100 % 100))
    else:
        day3InMinutes = abs(round(day3In * 100 % 100) - 60)
    
    day3OutMinutes = round(day3Out * 100 % 100)
    
    if (day3InMinutes + day3OutMinutes) >= 60:
        day3Minutes = (day3InMinutes + day3OutMinutes) % 60
    else:
        day3Minutes = day3InMinutes + day3OutMinutes
    day3Money = ((day3Hours *salary) + ((salary / 60) * day3Minutes))
    totalMoney += day3Money

    #total amount
    totalMoney = totalMoney - (8.5 * (days - didNotHaveBreak))
    totalMoney += 0

    print("day 1 = $" + str(day1Money))
    print("day 2 = $" + str(day2Money))
    print("day 3 = $" + str(day3Money))
    
    totalMoney = round(totalMoney, 2)
    print("Your total amount is $" + str(totalMoney))




elif days == 2:
    day1In = float(input("Day 1 - Enter the time of entry: "))
    day1Out = float(input("Day 1 - Enter the time of leave: "))
    day1Out += 12

    day2In = float(input("Day 2 - Enter the time of entry: "))
    day2Out = float(input("Day 2 - Enter the time of leave: "))
    day2Out += 12

    didNotHaveBreak = int(input('How many days did he not have a lunch?: '))

    totalMoney = 0

    # money for day 1
    day1Hours = int(day1Out - day1In)
    day1Minutes = 0
    if round(day1In * 100 % 100) == 0:
        day1InMinutes = abs(round(day1In * 100 % 100))
    else:
        day1InMinutes = abs(round(day1In * 100 % 100) - 60)
    
    day1OutMinutes = round(day1Out * 100 % 100)
    
    if (day1InMinutes + day1OutMinutes) >= 60:
        day1Minutes = (day1InMinutes + day1OutMinutes) % 60
    else:
        day1Minutes = day1InMinutes + day1OutMinutes
    
    day1Money = ((day1Hours *salary) + ((salary / 60) * day1Minutes))
    totalMoney += day1Money

    # money for day 2
    day2Hours = int(day2Out - day2In)
    day2Minutes = 0
    if round(day2In * 100 % 100) == 0:
        day2InMinutes = abs(round(day2In * 100 % 100))
    else:
        day2InMinutes = abs(round(day2In * 100 % 100) - 60)
    
    day2OutMinutes = round(day2Out * 100 % 100)
    
    if (day2InMinutes + day2OutMinutes) >= 60:
        day2Minutes = (day2InMinutes + day2OutMinutes) % 60
    else:
        day2Minutes = day2InMinutes + day2OutMinutes
    
    day2Money = ((day2Hours *salary) + ((salary / 60) * day2Minutes))
    totalMoney += day2Money

    #total amount
    totalMoney = totalMoney - (8.5 * (days - didNotHaveBreak))
    totalMoney += 0

    print("day 1 = $" + str(day1Money))
    print("day 2 = $" + str(day2Money))
    
    totalMoney = round(totalMoney, 2)
    print("Your total amount is $" + str(totalMoney))



elif days == 1:
    day1In = float(input("Day 1 - Enter the time of entry: "))
    day1Out = float(input("Day 1 - Enter the time of leave: "))
    day1Out += 12

    didNotHaveBreak = int(input('How many days did he not have a lunch?: '))

    totalMoney = 0

    # money for day 1
    day1Hours = int(day1Out - day1In)
    day1Minutes = 0
    if round(day1In * 100 % 100) == 0:
        day1InMinutes = abs(round(day1In * 100 % 100))
    else:
        day1InMinutes = abs(round(day1In * 100 % 100) - 60)
    
    day1OutMinutes = round(day1Out * 100 % 100)
    
    if (day1InMinutes + day1OutMinutes) >= 60:
        day1Minutes = (day1InMinutes + day1OutMinutes) % 60
    else:
        day1Minutes = day1InMinutes + day1OutMinutes
    
    day1Money = ((day1Hours *salary) + ((salary / 60) * day1Minutes))
    totalMoney += day1Money

    #total amount
    totalMoney = totalMoney - (8.5 * (days - didNotHaveBreak))
    totalMoney += 0

    print("day 1 = $" + str(day1Money))
    
    totalMoney = round(totalMoney, 2)
    print("Your total amount is $" + str(totalMoney))


    #test
    print("day1Hours:" , str(day1Hours))
    print("day1Minutes:", str(day1Minutes))
    print("day1InMinutes:", str(day1InMinutes))
    print("day1OutMinutes:", str(day1OutMinutes))
    
    

else:
    print("enter a valid number of working days")
