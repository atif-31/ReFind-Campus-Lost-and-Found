# ReFind — Campus Lost & Found Management System

**Lost something? Find your way back.**

ReFind is a campus-based Lost and Found Management System designed to make reporting, tracking, and recovering misplaced belongings easier for students.

The application provides a simple web interface where students can report lost items, register found items, check possible matches, and track the return process.

## Features

- **Report Lost Items:** Submit details about misplaced belongings.
- **Report Found Items:** Register items found around campus.
- **View All Reports:** Browse submitted lost and found reports.
- **Possible Matches:** Identify potential matches using item names and categories.
- **Desk Status Management:** Update whether a found item has been deposited at the physical Lost and Found desk.
- **Mark Items as Returned:** Update matching lost and found reports when an item is returned.
- **Data Persistence:** Store reports using a JSON file.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Application logic |
| Flask | Web framework |
| HTML | Web page structure |
| CSS | User interface styling |
| JSON | Data storage |
| Git & GitHub | Version control and project hosting |

## Project Structure

```text
CampusLostAndFound/
│
├── static/
│   └── style.css
│
├── templates/
│   ├── desk_status.html
│   ├── mark_returned.html
│   ├── matches.html
│   ├── report_found.html
│   ├── report_lost.html
│   ├── reports.html
│   ├── success.html
│   └── tracker.html
│
├── app.py
├── main.py
├── reports.json
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/atif-31/ReFind-Campus-Lost-and-Found.git
```

### 2. Navigate to the project directory

```bash
cd ReFind-Campus-Lost-and-Found
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Run the application

```bash
python app.py
```

### 5. Open ReFind

Visit the following address in your browser:

```text
http://127.0.0.1:5000
```

## Data Storage

ReFind currently uses a JSON file (`reports.json`) to store submitted reports.

The application loads existing reports when it starts and saves changes when users submit or update reports.

## Future Enhancements

The following features can be considered for future development:

- Advanced search and filtering of reports.
- Improved matching logic for similar item descriptions.
- User authentication and authorised staff access.
- Enhanced dashboard analytics.
- Image uploads for lost and found items.
- Database integration for more scalable storage.

## Current Project Status

ReFind is a functional Flask-based prototype with working reporting, matching, desk-status management, and item-return workflows.

## Author

**Atif Ali**

B.Tech — Computer Science and Engineering

GitHub: [atif-31](https://github.com/atif-31)

---

*ReFind — Lost something? Find your way back.*