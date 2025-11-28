text = "HELLO"

# Attempt 1: At the end
result1 = text + "!"
print(result1)
print(text)  # Did the original change?

# Attempt 2: At the beginning  
result2 = "Mr. " + text
print(result2)

# Attempt 3: In the middle (think about slicing!)
result3 = text[:3] + "X" + text[3:]
print(result3)