def is_leap_year(year: int) -> bool:
    # Leap year if divisible by 4
    # But not divisible by 100 unless also divisible by 400
    if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False

# Example usage:
print(is_leap_year(2024))  # True
print(is_leap_year(1900))  # False
print(is_leap_year(2000))  # True
print(is_leap_year(2023))  # False
