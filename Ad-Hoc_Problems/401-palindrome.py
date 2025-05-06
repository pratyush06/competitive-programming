list_of_mirrored_word = {
    'A': 'A', 'B': '', 'C': '', 'D': '', 'E': '3', 'F': '', 'G': '', 'H': 'H', 'I': 'I',
    'J': 'L', 'K': '', 'L': 'J', 'M': 'M', 'N': '', 'O': 'O', 'P': '', 'Q': '', 'R': '',
    'S': '2', 'T': 'T', 'U': 'U', 'V': 'V', 'W': 'W', 'X': 'X', 'Y': 'Y', 'Z': '5',
    '1': '1', '2': 'S', '3': 'E', '4': '', '5': 'Z', '6': '', '7': '', '8': '8', '9': ''
}

while True:
    try:
        word = input().strip()
    except EOFError:
        break

    palindrome = True
    mirrored_word = ''

    # Check if it's a regular palindrome
    for i in range(len(word) // 2):
        if word[i] != word[-(i + 1)]:
            palindrome = False
            break

    # Build the mirrored word
    for j in range(len(word)):
        # Use get with a default value (e.g., '') to avoid None
        mirrored_word += list_of_mirrored_word.get(word[j], '')

    # Check if it's a mirrored string
    is_mirrored = mirrored_word == word[::-1]

    # Output based on conditions
    if palindrome and is_mirrored:
        print(f'{word} -- is a mirrored palindrome.')
    elif is_mirrored:
        print(f'{word} -- is a mirrored string.')
    elif palindrome:
        print(f'{word} -- is a regular palindrome.')
    else:
        print(f'{word} -- is not a palindrome.')
    
    print()  # Empty line after each test case