# -----------------------------
# Applicant Data (10 applicants)
# -----------------------------

applicant1 = {
    "name": "John Smith",
    "age": 20,
    "address": {
        "street": "123 Main St",
        "city": "Chicago",
        "state": "IL",
        "zip_code": "60601"
    },
    "program_status": "Applied"
}

applicant2 = {
    "name": "Sarah Johnson",
    "age": 17,
    "address": {
        "street": "45 Lake St",
        "city": "Chicago",
        "state": "IL",
        "zip_code": "60602"
    },
    "program_status": "Accepted"
}

applicant3 = {
    "name": "Michael Brown",
    "age": 25,
    "address": {
        "street": "88 Oak Ave",
        "city": "Chicago",
        "state": "IL",
        "zip_code": "60603"
    },
    "program_status": "Active"
}

applicant4 = {
    "name": "Emily Davis",
    "age": 30,
    "address": {
        "street": "10 Pine Rd",
        "city": "Chicago",
        "state": "IL",
        "zip_code": "60604"
    },
    "program_status": "Completed"
}

applicant5 = {
    "name": "David Wilson",
    "age": 19,
    "address": {
        "street": "77 West St",
        "city": "Chicago",
        "state": "IL",
        "zip_code": "60605"
    },
    "program_status": "Active"
}

applicant6 = {
    "name": "Olivia Martinez",
    "age": 22,
    "address": {
        "street": "300 North Ave",
        "city": "Chicago",
        "state": "IL",
        "zip_code": "60606"
    },
    "program_status": "Rejected"
}

applicant7 = {
    "name": "James Anderson",
    "age": 18,
    "address": {
        "street": "55 South Blvd",
        "city": "Chicago",
        "state": "IL",
        "zip_code": "60607"
    },
    "program_status": "Active"
}

applicant8 = {
    "name": "Sophia Thomas",
    "age": 16,
    "address": {
        "street": "9 Elm St",
        "city": "Chicago",
        "state": "IL",
        "zip_code": "60608"
    },
    "program_status": "Applied"
}

applicant9 = {
    "name": "Daniel Taylor",
    "age": 28,
    "address": {
        "street": "400 Cedar Ln",
        "city": "Chicago",
        "state": "IL",
        "zip_code": "60609"
    },
    "program_status": "Completed"
}

applicant10 = {
    "name": "Isabella Moore",
    "age": 21,
    "address": {
        "street": "12 Birch Way",
        "city": "Chicago",
        "state": "IL",
        "zip_code": "60610"
    },
    "program_status": "Active"
}

# -----------------------------
# List of applicants
# -----------------------------

applicants = [
    applicant1, applicant2, applicant3, applicant4, applicant5,
    applicant6, applicant7, applicant8, applicant9, applicant10
]

# -----------------------------
# Functions
# -----------------------------

def is_eligible_applicant(applicant):
    """
    Returns True if applicant is over 18 years old.
    """
    if applicant["age"] > 18:
        return True
    else:
        return False


def is_active_applicant(applicant):
    """
    Returns True if applicant program status is Active.
    """
    if applicant["program_status"] == "Active":
        return True
    else:
        return False


def filter_applicants_by_eligibility(applicants_list):
    """
    Returns a list of applicants who are eligible (age > 18).
    """
    eligible_list = []

    for applicant in applicants_list:
        if is_eligible_applicant(applicant):
            eligible_list.append(applicant)

    return eligible_list


def filter_active_applicants(applicants_list):
    """
    Returns a list of applicants whose status is Active.
    """
    active_list = []

    for applicant in applicants_list:
        if is_active_applicant(applicant):
            active_list.append(applicant)

    return active_list


def report_completed_applicants(applicants_list):
    """
    Returns the number of applicants with Completed status.
    """
    count = 0

    for applicant in applicants_list:
        if applicant["program_status"] == "Completed":
            count += 1

    return count


# -----------------------------
# Simple testing (optional output)
# -----------------------------

print("Eligible Applicants:", len(filter_applicants_by_eligibility(applicants)))
print("Active Applicants:", len(filter_active_applicants(applicants)))
print("Completed Applicants:", report_completed_applicants(applicants))