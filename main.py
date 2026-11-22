
import json

def load_reports():

    try:
        with open("reports.json", "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []


def save_reports():

    with open("reports.json", "w") as file:
        json.dump(reports, file, indent=4)


reports = load_reports()


def report_lost():
    print("\n--- Report a Lost Item ---")

    name = input("Enter item name: ").strip()
    category = input("Enter item category: ").strip()
    description = input("Enter item description (optional): ").strip()
    location = input("Where did you last see it? ").strip()

    if not name or not category or not location:
        print("Item Name, Category and Location cannot be blank.")
        return

    report = {
        "id": len(reports) + 1,
        "type": "lost",
        "name": name,
        "category": category,
        "description": description,
        "location": location,
        "status": "open",
        "desk_status": ""
    }

    reports.append(report)
    save_reports()
    print("Lost item report saved successfully!")





def report_found():

    print("\n--- Report a Found Item ---")

    name = input("Enter item name: ").strip()
    category = input("Enter item category: ").strip()
    description = input("Enter item description (optional): ").strip()
    location = input("Where was it found? ").strip()

    if not name or not category or not location:
        print("Item Name, Category and Location cannot be blank.")
        return

    while True:

        print("\nWhere is the item currently?")
        print("1. With me / not deposited at the Lost and Found desk")
        print("2. Deposited at the Lost and Found desk")

        desk_choice = input("Enter your choice: ").strip()

        if desk_choice == "1":
            desk_status = "Not_deposited"
            break

        elif desk_choice == "2":
            desk_status = "Deposited"
            break

        else:
            print("Invalid desk choice. Please enter 1 or 2.")

    report = {
        "id": len(reports) + 1,
        "type": "found",
        "name": name,
        "category": category,
        "description": description,
        "location": location,
        "status": "open",
        "desk_status": desk_status
    }

    reports.append(report)
    save_reports()
    print("Found item report saved successfully!")




def view_reports():
    if len(reports) == 0:
        print("No reports have been added yet.")
        return

    for report in reports:
        print("\nReport ID:", report["id"])
        print("Type:", report["type"])
        print("Name:", report["name"])
        print("Category:", report["category"])
        print("Description:", report["description"])
        print("Location:", report["location"])
        print("Status:", report["status"])

        if report["type"] == "found":
            print("Desk status:", report["desk_status"])


def search_report():
    found_any = False
    keyword = input("Enter a keyword to search for your item: ").strip().lower()

    if keyword == "":
        print("Search keyword cannot be blank.")
        return

    for report in reports:
        if (keyword in report["name"].lower()
            or keyword in report["category"].lower()
            or keyword in report["description"].lower()
            or keyword in report["location"].lower()):

            print("\nMatching report found!")
            print("Name:", report["name"])
            print("Category:", report["category"])
            print("Description:", report["description"])
            print("Location:", report["location"])

            found_any = True

    if found_any == False:
        print("No matching reports found.")



def find_possible_matches():

    match_found = False

    for lost_report in reports:

        if lost_report["type"] == "lost" and lost_report["status"] == "open":

            for found_report in reports:

                if found_report["type"] == "found" and found_report["status"] == "open":

                    if (lost_report["name"].lower() == found_report["name"].lower()
                        and lost_report["category"].lower() == found_report["category"].lower()):

                        print("\n===== POSSIBLE MATCH FOUND =====")

                        print("Lost Report ID:", lost_report["id"])
                        print("Found Report ID:", found_report["id"])

                        print("Item Name:", lost_report["name"])
                        print("Category:", lost_report["category"])

                        print("Lost Location:", lost_report["location"])
                        print("Found Location:", found_report["location"])

                        print("Desk Status:", found_report["desk_status"])

                        match_found = True

    if match_found == False:
        print("No possible matches found.")




def update_desk_status():

    while True:

        try:
            report_id = int(input("Enter the Found Report ID (0 to cancel): "))

        except ValueError:
            print("Please enter a valid numeric Report ID.")
            continue

        if report_id == 0:
            print("Operation cancelled.")
            return

        found_report = None

        for report in reports:

            if report["id"] == report_id and report["type"] == "found":
                found_report = report
                break

        if found_report is None:
            print("Found report not found. Please try again.")
            continue

        if found_report["status"] == "returned":
            print("This item has already been returned.")
            return

        break

    print("\nCurrent Desk Status:", found_report["desk_status"])

    while True:

        print("\n1. Not deposited")
        print("2. Deposited")

        choice = input("Enter your choice (0 to cancel): ").strip()

        if choice == "1":
            found_report["desk_status"] = "Not_deposited"
            save_reports()
            break

        elif choice == "2":
            found_report["desk_status"] = "Deposited"
            save_reports()
            break

        elif choice == "0":
            print("Operation cancelled.")
            return

        else:
            print("Invalid choice. Please enter 1 or 2.")

    print("Desk status updated successfully!")






def mark_item_returned():

    while True:

        try:
            report_id = int(input("Enter the Lost Report ID (0 to cancel): "))

        except ValueError:
            print("Please enter a valid numeric Report ID.")
            continue

        if report_id == 0:
            print("Operation cancelled.")
            return

        lost_report = None
        found_report = None

        for report in reports:

            if report["id"] == report_id and report["type"] == "lost":
                lost_report = report
                break

        if lost_report is None:
            print("Lost report not found. Please try again.")
            continue

        break

    if lost_report["status"] == "returned":
        print("This item has already been returned.")
        return

    for report in reports:

        if (report["type"] == "found"
            and report["status"] == "open"
            and report["name"].lower() == lost_report["name"].lower()
            and report["category"].lower() == lost_report["category"].lower()):

            found_report = report
            break

    if found_report is None:
        print("No corresponding found report was found.")
        print("Lost report has not been updated.")
        return

    lost_report["status"] = "returned"
    found_report["status"] = "returned"

    save_reports()

    print("\nItem successfully marked as returned!")
    print("Lost Report ID:", lost_report["id"])
    print("Found Report ID:", found_report["id"])



            











while True:

    print("\n===== CAMPUS LOST AND FOUND TRACKER =====")
    print("1. Report a Lost Item")
    print("2. Report a Found Item")
    print("3. View All Reports")
    print("4. Search Reports")
    print("5. Find Possible Matches")
    print("6. Update Desk Status")
    print("7. Mark Item as Returned")
    print("8. Exit")

    choice = input("Enter your choice of action: ").strip()

    if choice == "1":
        report_lost()

    elif choice == "2":
        report_found()

    elif choice == "3":
        view_reports()

    elif choice == "4":
        search_report()

    elif choice == "5":
        find_possible_matches()

    elif choice == "6":
        update_desk_status()

    elif choice == "7":
        mark_item_returned()

    elif choice == "8":
        print("Thank you for using our tracker :)")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 8.")


