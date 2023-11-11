def romantoint():
    string = str(input('enter the right roman number:'))
    memory = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    integer = 0
    i = 0
    while i < len(string):
        if i + 1 < len(string) and memory[string[i]] < memory[string[i + 1]]:
            integer += memory[string[i + 1]] - memory[string[i]]
            i += 2
        else:
            integer += memory[string[i]]
            i += 1
    return integer

result = romantoint()
print(f"The integer value of the Roman numeral is: {result}")