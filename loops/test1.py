def main():
    print(solution("abdtacbt"))

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