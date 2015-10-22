# Chapter 2 - Exercise 8
# alarmClockConverter.py - Converts the time (24 hr) with the number of hours
# inputted and hours to pass.

# Prompt for current time and sets to an integer
timeNowPrompt = input("What time is it now? " )
timeNow = int(timeNowPrompt)

# Prompt for number of hours to pass and sets to an integer
hourAmountPrompt = input("How many hours do you want to set alarm? ")
hourAmount = int(hourAmountPrompt)

# Conversions
initTime = hourAmount + timeNow
days = initTime // 24
setTime = initTime - (days * 24)

# Print what time alarm will go off.
print("The alarm will go off at", str(setTime) + ":00")

