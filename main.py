from datetime import datetime


def calculate_bmi(weight, height, units="metric"):
    """
    Calculate BMI based on weight, height, and units.

    :param weight: Weight in kilograms (metric) or pounds (imperial)
    :param height: Height in meters (metric) or inches (imperial)
    :param units: "metric" (default) or "imperial"
    :return: BMI value rounded to 2 decimals
    """
    return round((weight / (height ** 2)) if units == "metric" else (weight / (height ** 2)) * 703, 2)


def calculate_age(dob):
    """
    Calculate age from the given date of birth.

    :param dob: Date of birth as a string in 'YYYY-MM-DD' format.
    :return: Age in years.
    """
    birth_date = datetime.strptime(dob, "%Y-%m-%d")
    today = datetime.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age


def bmi_category(bmi, age, ethnicity=None):
    """
    Determine BMI category based on age, BMI, and ethnicity.

    :param bmi: BMI value
    :param age: Age in years
    :param ethnicity: Ethnicity or background as a string (for adults only).
    :return: BMI category as a string.
    """
    if age < 2 or age > 120:
        return "Age out of range. Please consult a healthcare professional."

    # Thresholds based on ethnicity (for adults)
    thresholds = {
        "asian": (18.5, 23, 27.5),
        "black": (18.5, 25, 30),
        "hispanic": (18.5, 25, 30),
        "pacific islander": (18.5, 26, 32),
        "indigenous": (18.5, 24.9, 29.9),
        "middle eastern": (18.5, 24.9, 29.9),
        "caucasian": (18.5, 24.9, 29.9),
        "default": (18.5, 24.9, 29.9),
    }

    # Children and Adolescents (Percentiles)
    if age < 18:
        if bmi < 5:
            return "Severely underweight (percentile < 5th)"
        elif 5 <= bmi < 85:
            return "Healthy weight (percentile 5th - 85th)"
        elif 85 <= bmi < 95:
            return "Overweight (percentile 85th - 95th)"
        else:
            return "Obese (percentile ≥ 95th)"

    # Adults (Ethnicity-Specific Thresholds)
    low, high, obese = thresholds.get(ethnicity.lower(), thresholds["default"])
    if bmi < low:
        return "Underweight"
    elif low <= bmi < high:
        return "Healthy weight"
    elif high <= bmi < obese:
        return "Overweight"
    else:
        return "Obese"


def main():
    print("Welcome to the Advanced BMI Calculator with Age and Ethnicity Adjustment!\n")
    try:
        dob = input("Enter your Date of Birth (YYYY-MM-DD): ").strip()
        age = calculate_age(dob)

        gender = input("Enter your gender (Male/Female/Other): ").strip().capitalize()
        if gender not in ["Male", "Female", "Other"]:
            print("Invalid gender. Please enter Male, Female, or Other.")
            return

        if age >= 18:
            # Adults
            ethnicity = input(
                "Enter your ethnicity (e.g., Asian, Black, Caucasian, etc.): ").strip().lower()
            units = input("Enter units ('metric' or 'imperial'): ").strip().lower()
            if units not in ["metric", "imperial"]:
                print("Invalid units. Please choose 'metric' or 'imperial'.")
                return
        else:
            # Children
            print("For children, ethnicity is not required.")
            units = "metric"

        weight = float(input("Enter your weight (kg for metric, lbs for imperial): "))
        height = float(input("Enter your height (meters for metric, inches for imperial): "))

        if min(weight, height) <= 0:
            print("Weight and height must be positive values.")
            return

        bmi = calculate_bmi(weight, height, units)
        category = bmi_category(bmi, age, ethnicity if age >= 18 else None)

        print(f"\nYour BMI is: {bmi}")
        print(f"Category: {category}")
    except ValueError:
        print("Invalid input. Please enter numeric values for weight, height, and a valid date for DOB.")


if __name__ == "__main__":
    main()
