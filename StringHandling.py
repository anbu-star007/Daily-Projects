def analyze_string(s):
    s = s.lower().replace(" ", "")
    
    # Reverse string
    reversed_str = s[::-1]
    
    # Count vowels and consonants
    vowels = sum(1 for c in s if c.isalpha() and c in "aeiou")
    consonants = sum(1 for c in s if c.isalpha() and c not in "aeiou")
    
    # Check palindrome
    is_palindrome = s == reversed_str
    
    return {
        "original": s,
        "reversed": reversed_str,
        "vowels": vowels,
        "consonants": consonants,
        "is_palindrome": is_palindrome
    }

# Main
user_input = input("Enter a string: ")
result = analyze_string(user_input)

print(f"\nOriginal String: {result['original']}")
print(f"Reversed String: {result['reversed']}")
print(f"Vowels: {result['vowels']}")
print(f"Consonants: {result['consonants']}")
print(f"Is Palindrome: {result['is_palindrome']}")