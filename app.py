# Study Time Tracker Program
# This program estimates weekly study hours based on daily input

print("Welcome to my Python program!")

# Ask user for input
hours = input("How many hours did you study today? ")


# Error handling + conversion
try:
    hours = float(hours)
except ValueError:
    print("Please enter a valid number.")
    exit()

# Calculation
weekly_hours = hours * 7


# Output result
print(f"You are on track to study {weekly_hours} hours this week.")
