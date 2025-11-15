text = "HELLO"
print(text[0:3])  # What prints?
print(text[1:4])  # What prints?
print(text[0:5])  # What prints?

print("==========================")

print(text[:3])   # What happens when you skip the start?
print(text[2:])   # What happens when you skip the end?
print(text[:])    # What happens when you skip both?

print("==========================")

#text = "HELLO"
#      01234  (positive indices)
#     -5-4-3-2-1  (negative indices)

print(text[-1])   # What character?
print(text[-3])   # What character?
print(text[-4:])  # What do you get?

print("==========================")

text = "HELLO"
print(text[0:5:1])   # Every 1st character (default)
print(text[0:5:2])   # Every 2nd character
print(text[::2])     # What pattern?

print("==========================")

print(text[::-1])
print(text[-4:])      # What pattern?