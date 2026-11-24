import math

def softmax(scores: list[float]) -> list[float]:
    # Your code here
    max_num = max(scores)
    total = 0
    for i in range(len(scores)):
        total += math.exp(scores[i] - max_num)
    ans = []
    for i in range(len(scores)):
        ans.append(math.exp(scores[i] - max_num) / total)
    
    return ans