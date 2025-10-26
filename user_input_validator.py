class UserInputValidator:
    def validate_positive_integers(self, input_list):
        # This class method will check if all elements in the input lists
        # are positive integers. If true, it returns True; otherwise
        # it will return False.
        valid_integers = []
        for item in input_list:
            if item.isdigit() and int(item) > 0:
                valid_integers.append(int(item))
            return valid_integers
