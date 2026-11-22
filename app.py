
from flask import Flask, render_template, request
import json

app = Flask(__name__)


# Load existing reports from JSON
def load_reports():
    try:
        with open("reports.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


# Save reports to JSON
def save_reports():
    with open("reports.json", "w") as file:
        json.dump(reports, file, indent=4)


reports = load_reports()


# Homepage
@app.route("/")
def home():

    total_lost = 0
    total_found = 0
    total_returned = 0

    for report in reports:

        if report["type"] == "lost":
            total_lost += 1

        if report["type"] == "found":
            total_found += 1

        if report["status"] == "returned":
            total_returned += 1

    return render_template(
        "tracker.html",
        total_lost=total_lost,
        total_found=total_found,
        total_returned=total_returned
    )


# Report Lost Item
@app.route("/report-lost", methods=["GET", "POST"])
def report_lost_page():

    if request.method == "POST":

        name = request.form["name"]
        category = request.form["category"]
        description = request.form["description"]
        location = request.form["location"]

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

        return render_template("success.html")

    return render_template("report_lost.html")


# Report Found Item
@app.route("/report-found", methods=["GET", "POST"])
def report_found_page():

    if request.method == "POST":

        name = request.form["name"]
        category = request.form["category"]
        description = request.form["description"]
        location = request.form["location"]
        desk_status = request.form["desk_status"]

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

        return render_template("success.html")

    return render_template("report_found.html")


# View All Reports
@app.route("/reports")
def view_reports_page():
    return render_template("reports.html", reports=reports)


# Find Possible Matches
@app.route("/matches")
def possible_matches_page():

    matches = []

    for lost_report in reports:

        if lost_report["type"] == "lost" and lost_report["status"] == "open":

            for found_report in reports:

                if found_report["type"] == "found" and found_report["status"] == "open":

                    if (lost_report["name"].lower() == found_report["name"].lower()
                        and lost_report["category"].lower() == found_report["category"].lower()):

                        match = {
                            "lost": lost_report,
                            "found": found_report
                        }

                        matches.append(match)

    return render_template("matches.html", matches=matches)


# Update Desk Status
@app.route("/update-desk-status", methods=["GET", "POST"])
def update_desk_status_page():

    found_reports = []

    for report in reports:
        if report["type"] == "found" and report["status"] == "open":
            found_reports.append(report)

    message = ""

    if request.method == "POST":

        report_id = int(request.form["report_id"])
        new_status = request.form["desk_status"]

        for report in reports:

            if report["id"] == report_id and report["type"] == "found":

                if report["status"] == "returned":
                    message = "This item has already been returned."
                else:
                    report["desk_status"] = new_status
                    save_reports()
                    message = "Desk status updated successfully!"

                break

        return render_template(
            "desk_status.html",
            found_reports=found_reports,
            message=message
        )

    return render_template(
        "desk_status.html",
        found_reports=found_reports,
        message=message
    )

@app.route("/mark-returned", methods=["GET", "POST"])
def mark_returned_page():

    lost_reports = []

    for report in reports:
        if report["type"] == "lost" and report["status"] == "open":
            lost_reports.append(report)

    message = ""

    if request.method == "POST":

        report_id = int(request.form["report_id"])

        lost_report = None
        found_report = None

        for report in reports:
            if report["id"] == report_id and report["type"] == "lost":
                lost_report = report
                break

        if lost_report is not None:

            for report in reports:
                if (report["type"] == "found"
                    and report["status"] == "open"
                    and report["name"].lower() == lost_report["name"].lower()
                    and report["category"].lower() == lost_report["category"].lower()):

                    found_report = report
                    break

            if found_report is None:
                message = "No corresponding found report was found."

            else:
                lost_report["status"] = "returned"
                found_report["status"] = "returned"

                save_reports()

                message = "Item successfully marked as returned!"

    return render_template(
        "mark_returned.html",
        lost_reports=lost_reports,
        message=message
    )

if __name__ == "__main__":
    app.run(debug=True)
