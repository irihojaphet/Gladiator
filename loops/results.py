results = ["Mario", "Luigi"]

results.append("Princess")
results.append(["Ypshi", "Toad"]) # add at the end new element
results.remove(["Ypshi", "Toad"]) # remove element regardless of position
results.extend(["Ypshi", "Toad"]) # add multiple elements at the end
results.insert[0, "Bowser"] # add at specific position

results.sort() # sort alphabetically
results.reverse() # reverse order
results.clear() # remove all elements
results.count("Mario") # count occurrences of an element


print(results)