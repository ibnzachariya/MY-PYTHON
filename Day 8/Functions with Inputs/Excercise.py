def life_in_weeks(age):
    weeks_in_a_year = 52
    years_left = 90 - age
    weeks_left = years_left * weeks_in_a_year
    print(f"You have {weeks_left} weeks left.")
life_in_weeks(20)