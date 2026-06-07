# MODULE 4: ANALYSIS ENGINE

def check_equipment_risk(equipment):
    """Check risk level of equipment based on temp, pressure, status."""
    if equipment["temperature"] > 80:
        return "HIGH RISK (Temperature critical)"
    elif equipment["pressure"] > 150:
        return "HIGH RISK (Pressure critical)"
    elif equipment["status"] == "faulty":
        return "INCIDENT REQUIRED"
    else:
        return "OK"

def assign_priority(incident):
    """Assign response team based on severity."""
    if incident["severity"] == "high":
        return "Emergency Team Assigned"
    elif incident["severity"] == "medium":
        return "Maintenance Team Assigned"
    else:
        return "Monitor Team Assigned"

# MODULE 5: CONTROL DASHBOARD

def view_all_equipment(equipment_list):
    print("\n--- Equipment Status ---")
    for eq in equipment_list:
        risk = check_equipment_risk(eq)
        print(f"{eq['name']} → {risk}")

def report_incident(incidents, equipment_list):
    print("\n--- Report Incident ---")
    equipment_name = input("Equipment name: ")
    issue = input("Issue: ")
    severity = input("Severity (high/medium/low): ").lower()
    reported_by = input("Reported by: ")

    incident = {
        "equipment": equipment_name,
        "issue": issue,
        "severity": severity,
        "reported_by": reported_by
    }
    incidents.append(incident)
    print("Incident reported successfully!")

def view_incidents(incidents):
    print("\n--- Active Incidents ---")
    for inc in incidents:
        team = assign_priority(inc)
        print(f"{inc['equipment']} - {inc['issue']} - {inc['severity'].upper()} - {team}")

def run_system_analysis(equipment_list, incidents):
    print("\n--- System Analysis ---")
    critical_alerts = 0
    for eq in equipment_list:
        risk = check_equipment_risk(eq)
        print(f"{eq['name']} → {risk}")
        if "HIGH RISK" in risk:
            critical_alerts += 1

    print("\n--- Summary ---")
    print(f"Total Equipment: {len(equipment_list)}")
    print(f"Active Incidents: {len(incidents)}")
    print(f"Critical Alerts: {critical_alerts}")

# MAIN LOOP SYSTEM

def main():
    equipment_list = []
    incidents = []

    # STEP 1: Add operators and equipment
    num_equipment = int(input("How many equipment to add? "))
    for i in range(num_equipment):
        print(f"\nEnter details for equipment {i+1}:")
        name = input("Name: ")
        temp = float(input("Temperature: "))
        pres = float(input("Pressure: "))
        status = input("Status (ok/faulty): ").lower()
        equipment_list.append({"name": name, "temperature": temp, "pressure": pres, "status": status})

    # Dashboard Menu
    while True:
        print("\n--- CONTROL DASHBOARD ---")
        print("1. View all equipment")
        print("2. Report incident")
        print("3. View incidents")
        print("4. Run system analysis")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            view_all_equipment(equipment_list)
        elif choice == "2":
            report_incident(incidents, equipment_list)
        elif choice == "3":
            view_incidents(incidents)
        elif choice == "4":
            run_system_analysis(equipment_list, incidents)
        elif choice == "5":
            print("Exiting system... Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

# Run program
main()
