class Applicant:
    def __init__(self, name, age, street, city, state, zip_code, program_status):
        self.name = name
        self.age = age
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.program_status = program_status

    def is_eligible_applicant(self):
        return self.age > 18

    def is_active_applicant(self):
        return self.program_status == "Active"


class ApplicantTracker:
    def __init__(self, applicants):
        self.applicants = applicants

    def filter_applicants_by_eligibility(self):
        result = []
        for applicant in self.applicants:
            if applicant.is_eligible_applicant():
                result.append(applicant)
        return result

    def filter_active_applicants(self):
        result = []
        for applicant in self.applicants:
            if applicant.is_active_applicant():
                result.append(applicant)
        return result

    def report_completed_applicants(self):
        count = 0
        for applicant in self.applicants:
            if applicant.program_status == "Completed":
                count += 1
        return count
    
applicant1 = Applicant("John Smith", 20, "123 Main St", "Chicago", "IL", "60601", "Applied")
applicant2 = Applicant("Sarah Johnson", 17, "45 Oak St", "Chicago", "IL", "60602", "Rejected")
applicant3 = Applicant("Michael Brown", 25, "78 Pine St", "Chicago", "IL", "60603", "Active")
applicant4 = Applicant("Emily Davis", 30, "12 Lake St", "Chicago", "IL", "60604", "Completed")
applicant5 = Applicant("David Wilson", 19, "99 Elm St", "Chicago", "IL", "60605", "Accepted")
applicant6 = Applicant("Jessica Garcia", 22, "55 Maple St", "Chicago", "IL", "60606", "Dismissed")
applicant7 = Applicant("Daniel Martinez", 18, "88 Cedar St", "Chicago", "IL", "60607", "Applied")
applicant8 = Applicant("Laura Rodriguez", 28, "14 Birch St", "Chicago", "IL", "60608", "Completed")
applicant9 = Applicant("James Lee", 21, "33 Walnut St", "Chicago", "IL", "60609", "Active")
applicant10 = Applicant("Olivia Taylor", 16, "77 Ash St", "Chicago", "IL", "60610", "Rejected")


applicant_fleet = [
    applicant1, applicant2, applicant3, applicant4, applicant5,
    applicant6, applicant7, applicant8, applicant9, applicant10
]


tracker = ApplicantTracker(applicant_fleet)

eligible = tracker.filter_applicants_by_eligibility()
active = tracker.filter_active_applicants()
completed_count = tracker.report_completed_applicants()

print("Eligible applicants:", len(eligible))
print("Active applicants:", len(active))
print("Completed applicants:", completed_count)