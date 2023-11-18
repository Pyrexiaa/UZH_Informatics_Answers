# perform a ROTn encoding
def rot_n(plain_text, shift_by):
    result = ""
    for char in plain_text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            shifted_char = chr(((ord(char) - ord('a') + shift_by) % 26) + ord('a'))
            if is_upper:
                shifted_char = shifted_char.upper()
        else:
            shifted_char = char
        result += shifted_char
    return result

print(rot_n("abc", 1))