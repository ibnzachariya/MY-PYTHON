# SMART OIL FIELD MONITORING & ALERT SYSTEM

# Step 1: Ask how many equipment to monitor
num_equipment = int(input("How many equipment do you want to monitor? "))

# Step 2: Collect data
equipment_list = []
for i in range(num_equipment):
    print(f"\nEnter details for equipment {i+1}:")
    name = input("Name: ")
    temperature = float(input("Temperature: "))
    pressure = float(input("Pressure: "))
    status = input("Status (ok/fault): ").lower()

    equipment = {
        "name": name,
        "temperature": temperature,
        "pressure": pressure,
        "status": status
    }
    equipment_list.append(equipment)

# Step 3: Analyze and generate alerts
faulty_count = 0
high_temp_count = 0

print("\n--- Equipment Alerts ---")
for equip in equipment_list:
    if equip["temperature"] > 100:
        print(f"{equip['name']} → HIGH TEMP ALERT")
        high_temp_count += 1
    elif equip["status"] == "fault":
        print(f"{equip['name']} → FAULT ALERT")
        faulty_count += 1
    else:
        print(f"{equip['name']} → OK")

# Step 4: Final summary
print("\n--- Summary ---")
print(f"Total: {num_equipment}")
print(f"Faulty: {faulty_count}")
print(f"High Temp: {high_temp_count}")
