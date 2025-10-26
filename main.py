from user_input_validator import UserInputValidator

# Used to create two (2) instances of UserInputValidator class
validator1 = UserInputValidator()
validator2 = UserInputValidator()

# Test input lists
input1 = ["10", "20", "-5", "abc", "30"]
input2 = ["0", "kitty", "x", "boop", ""]

# Validate the lists and display results
result1 = validator1.validate_positive_integers(input1)
validator1.display_validation_message()
print("Validated positive integers from input1:", result1)

result2 = validator2.validate_positive_integers(input2)
validator2.display_validation_message()
print("Validated positive integers from input2:", result2)
