def check_password_strength(password):
    
    
    # Initialize criteria checks
    length_ok = len(password) >= 8
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_number = any(char.isdigit() for char in password)
    has_special = any(char in "!@#$%^&*()_+-=[]{}|;:,.<>?" for char in password)
    
    # Count criteria met
    criteria_met = sum([length_ok, has_upper, has_lower, has_number, has_special])
    
    # Determine strength
    if criteria_met < 2:
        return "Weak"
    elif criteria_met < 4:
        return "Medium"
    else:
        return "Strong"


# Main program
if __name__ == "__main__":
    password = input("Enter a password to check: ")
    strength = check_password_strength(password)
    print(f"Password Strength: {strength} ")