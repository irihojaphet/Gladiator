def main():
    print(solution("abdtacbt"))
    
    list = ["jeff", "john", "jake"]
    uppercase = [w.upper() for w in list]
    dict = {w: len(w) for w in uppercase}
    print(uppercase)
    print(dict)

def solution(word):
    counts = {}
    for w in word:
        if w in counts:
            counts[w] += 1
        else:
            counts[w] = 1
    for k, v in counts.items():
        if v == 1:
            return k
        else:
            continue
main()