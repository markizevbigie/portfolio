#This is a function that will calculate whether one can buy a new car at a certain price, assuming they sell their old car.
#The function takes into account savings and a percentage change in value of the new and old cars
def nbMonths(startPriceOld, startPriceNew, savingperMonth, percentLossByMonth):
    monthCounter = 2          #The price of both vehicles goes down every month, this increases by .05 every 2 months
    savings = 0               #The amount we have saved increases by 1000 per month
    monthsPassed = 0
    while True:
        if startPriceOld >= startPriceNew:                              #If the price of our old car is greater than or equal to our new car, we're done
            print([monthsPassed, int(startPriceOld - startPriceNew)])
            return [monthsPassed, int(startPriceOld - startPriceNew)]
        if startPriceOld + savings >= startPriceNew:                    #If the price of our old car plus our savings is greater than or equal to our new car, we're done
            print([monthsPassed, round((startPriceOld + savings) - startPriceNew,0)])
            return [monthsPassed, round((startPriceOld + savings) - startPriceNew,0)]
        startPriceOld = startPriceOld * (100 - percentLossByMonth)/100             #If neither of the above scenarios is True the cars decrease in value, and our savings increase in value
        startPriceNew = startPriceNew * (100 - percentLossByMonth)/100
        savings = savings + savingperMonth
        if monthCounter == 2:                                                       #If we are on month 2, the percentLossByMonth increases by 0.5
            percentLossByMonth = percentLossByMonth + 0.5
            monthCounter = 0
        monthCounter = monthCounter + 1
        monthsPassed = monthsPassed + 1
#How get to go back to top? Answer: while loop with returns to stop code

nbMonths(2000, 8000, 1000, 1.5)
