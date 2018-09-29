def missingWords(s, t):
    # Write your code here
    s_ = s.split()
    t_ = t.split()
    i = 0
    j = 0
    ans = []
    while j < len(t_):
        while t_[j] != s_[i]:
            ans.append(s_[i])
            i += 1
        j += 1
        i += 1
    if i < len(s_):
        for x in s_[i:]:
            ans.append(x)
    return ans

s = "I am using hackerrank to improve programming"
t = "am hackerrank to improve"

print missingWords(s, t)