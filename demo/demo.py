def calculate_average(numbers):
    if not numbers:
        return 0  # Return 0 if the list is empty, avoids division by zero
    total = sum(numbers)  # Use descriptive variable names and built-in sum function
    return total / len(numbers)  # Simplify calculation
