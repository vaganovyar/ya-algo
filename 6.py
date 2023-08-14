def correct_bracket_sequence(data):
    stack = []
    close_bracket_data = {
        ")": "(",
        "]": "[",
        "}": "{",
    }

    for letter in data:
        try:
            close_bracket = close_bracket_data[letter]
            if stack[-1] != close_bracket:
                return False
            else:
                stack.pop(len(stack) - 1)
        except KeyError:
            stack.append(letter)

    return True


print(correct_bracket_sequence(input()))
