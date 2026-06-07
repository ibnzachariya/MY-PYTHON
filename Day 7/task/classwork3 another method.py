# SMART OIL FIELD MONITORING (Beginner Version)

# Step 1: Ask how many equipment to monitor
num_equipment = int(input("How many equipment do you want to monitor? "))

# Step 2: Create empty lists to store data
names = []
temperatures = []
pressures = []
statuses = []

# Step 3: Collect data for each equipment
for i in range(num_equipment):
    print(f"\nEnter details for equipment {i+1}:")
    name = input("Name: ")
    temp = float(input("Temperature: "))
    pres = float(input("Pressure: "))
    status = input("Status (ok/fault): ").lower()

    names.append(name)
    temperatures.append(temp)
    pressures.append(pres)
    statuses.append(status)

# Step 4: Analyze and generate alerts
faulty_count = 0
high_temp_count = 0

print("\n--- Equipment Alerts ---")
for i in range(num_equipment):
    if temperatures[i] > 100:
        print(f"{names[i]} → HIGH TEMP ALERT")
        high_temp_count += 1
    elif statuses[i] == "fault":
        print(f"{names[i]} → FAULT ALERT")
        faulty_count += 1
    else:
        print(f"{names[i]} → OK")

# Step 5: Final summary
print("\n    Summary    ")
print(f"Total: {num_equipment}")
print(f"Faulty: {faulty_count}")
print(f"High Temp: {high_temp_count}")
