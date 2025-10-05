def calculate_emi(principal, rate, tenure_years):
    """ EMI calculation using formula """
    rate = rate / (12 * 100)  # Convert annual % to monthly decimal
    tenure_months = tenure_years * 12
    if rate == 0:  # handle zero interest
        return principal / tenure_months
    emi = (principal * rate * (1 + rate) ** tenure_months) / ((1 + rate) ** tenure_months - 1)
    return emi


def loan_eligibility(age, income, credit_score, existing_emi, loan_amount, tenure_years, loan_type):
    # Default values
    min_income = 0
    interest_rate = 0.0
    max_tenure = 0

    # Loan type rules using if-elif
    loan_type = loan_type.lower()
    if loan_type == "personal":
        min_income = 20000
        interest_rate = 12.0
        max_tenure = 5
    elif loan_type == "home":
        min_income = 25000
        interest_rate = 8.5
        max_tenure = 30
    elif loan_type == "car":
        min_income = 18000
        interest_rate = 9.5
        max_tenure = 7
    elif loan_type == "education":
        min_income = 15000
        interest_rate = 10.0
        max_tenure = 10
    else:
        return "Invalid loan type! Choose from Personal, Home, Car, Education."

    # Basic checks
    if age < 21 or age > 60:
        return "Not eligible (Age must be between 21 and 60)."
    if credit_score < 650:
        return " Not eligible (Credit Score too low)."
    if income < min_income:
        return f" Not eligible (Minimum income required: ₹{min_income})."
    if tenure_years > max_tenure:
        return f"Not eligible (Max tenure allowed for {loan_type} loan is {max_tenure} years)."

    # EMI and FOIR
    emi = calculate_emi(loan_amount, interest_rate, tenure_years)
    foir = ((existing_emi + emi) / income) * 100

    if foir > 50:
        return f" Not eligible (FOIR too high: {foir:.2f}%)."
    else:
        return (f" Eligible for {loan_type.capitalize()} Loan!\n"
                f" Estimated EMI: ₹{emi:.2f}\n"
                f" FOIR: {foir:.2f}%\n"
                f" Interest Rate: {interest_rate}% per annum")


#  Example Run 
print("Available Loan Types: Personal, Home, Car, Education")
loan_type = input("Enter loan type: ")

age = int(input("Enter your age: "))
income = float(input("Enter your monthly income (₹): "))
credit_score = int(input("Enter your credit score: "))
existing_emi = float(input("Enter your total existing EMI (₹): "))
loan_amount = float(input("Enter desired loan amount (₹): "))
tenure_years = int(input("Enter tenure (years): "))

result = loan_eligibility(age, income, credit_score, existing_emi, loan_amount, tenure_years, loan_type)
print("\nResult:\n", result)
