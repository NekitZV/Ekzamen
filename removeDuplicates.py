def remove_brackets(text):
    result = []
    depth = 0

    for char in text:
        if char == '(':
            depth += 1
        elif char == ')':
            if depth > 0:
                depth -= 1
        elif depth == 0:
            result.append(char)

    return ''.join(result)
