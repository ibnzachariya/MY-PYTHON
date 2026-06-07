# SMART OIL FIELD MONITORING using Functions

# Function to collect data for one equipment
def collect_equipment_data():
    name = input("Name: ")
    temp = float(input("Temperature: "))
    pres = float(input("Pressure: "))
    status = input("Status (ok/fault): ").lower()
    return name, temp, pres, status

# Function to analyze one equipment
def analyze_equipment(name, temp, status):
    if temp > 100:
        print(f"{name} → HIGH TEMP ALERT")
        return "high_temp"
    elif status == "fault":
        print(f"{name} → FAULT ALERT")
        return "fault"
    else:
        print(f"{name} → OK")
        return "ok"

# Function to print summary
def print_summary(total, faulty, high_temp):
    print("\n--- Summary ---")
    print(f"Total: {total}")
    print(f"Faulty: {faulty}")
    print(f"High Temp: {high_temp}")

# Main program
def main():
    num_equipment = int(input("How many equipment do you want to monitor? "))
    faulty_count = 0
    high_temp_count = 0

    print("\n--- Equipment Alerts ---")
    for i in range(num_equipment):
        print(f"\nEnter details for equipment {i+1}:")
        name, temp, pres, status = collect_equipment_data()
        result = analyze_equipment(name, temp, status)

        if result == "fault":
            faulty_count += 1
        elif result == "high_temp":
            high_temp_count += 1

    print_summary(num_equipment, faulty_count, high_temp_count)

# Run the program
main()
