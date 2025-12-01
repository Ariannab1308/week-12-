# Objective:
# Apply comparison and logical operators to a real-world problem.

# Scenario:
# Write a program that:
# Asks the user for today’s temperature.

# Prints whether it’s cold, warm, or hot using comparison operators.

# If the temperature is out of range (below -10 or above 110), display “Extreme temperature warning!”

# Starter Code:

temp = int(input("What is the temperature today?"))
if temp < -9 or temp > 110:
    print("Extreme temperature warnimg!")
elif -10 <= temp <= 58:
    print("It's cold outside.")
elif 59 <= temp <= 84:
    print("It's warm outside.")
elif 85 <= temp <= 110:
    print("It's hot outside.")

