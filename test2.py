def main():
    print(isAnagram("", "tehpaj"))

def isAnagram(s, t):
    t_ = list(t)
    for ch in list(s):
        try:
            t_.remove(ch)
        except ValueError as e:
            return False
        
    if t_:
        return False
    return True

main()