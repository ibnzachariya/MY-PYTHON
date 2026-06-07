# Simple Oil Field Monitoring System

def check_equipment_risk(eq):
    if eq["temperature"] > 80:
        return "HIGH RISK (Temperature critical)"
    elif eq["pressure"] > 150:
        return "HIGH RISK (Pressure critical)"
    elif eq["status"] == "faulty":
        return "INCIDENT REQUIRED"
    else:
        return "OK"

def assign_priority(severity):
    if severity == "high":
        return "Emergency Team Assigned"
    elif severity == "medium":
        return "Maintenance Team Assigned"
    else:
        return "Monitor Team Assigned"

# MAIN PROGRAM
equipment_list = []
incidents = []

num_equipment = int(input("How many equipment to add? "))
for i in range(num_equipment):
    name = input("Name: ")
    temp = float(input("Temperature: "))
    pres = float(input("Pressure: "))
    status = input("Status (ok/faulty): ").lower()
    equipment_list.append({"name": name, "temperature": temp, "pressure": pres, "status": status})

while True:
    print("\n--- MENU ---")
    print("1. View equipment")
    print("2. Report incident")
    print("3. View incidents")
    print("4. Run analysis")
    print("5. Exit")

    choice = input("Choose: ")

    if choice == "1":
        for eq in equipment_list:
            print(f"{eq['name']} → {check_equipment_risk(eq)}")

    elif choice == "2":
        eq_name = input("Equipment name: ")
        issue = input("Issue: ")
        severity = input("Severity (high/medium/low): ").lower()
        reporter = input("Reported by: ")
        incidents.append({"equipment": eq_name, "issue": issue, "severity": severity, "reported_by": reporter})

    elif choice == "3":
        for inc in incidents:
            team = assign_priority(inc["severity"])
            print(f"{inc['equipment']} - {inc['issue']} - {inc['severity'].upper()} - {team}")

    elif choice == "4":
        critical = 0
        for eq in equipment_list:
            risk = check_equipment_risk(eq)
            print(f"{eq['name']} → {risk}")
            if "HIGH RISK" in risk:
                critical += 1
        print(f"\nSummary: Total={len(equipment_list)}, Incidents={len(incidents)}, Critical Alerts={critical}")

    elif choice == "5":
        print("Exiting.... Goodbye!")
        break
