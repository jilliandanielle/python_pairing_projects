scores = [10, 30, 90, 30, 100, 20, 10, 0, 30, 40, 40, 70, 70]

# latest(scores)=
print(scores.pop())

# personal_best(scores)= 
print(max(scores))

# personal_top_three(scores)=
top_3 = sorted(scores)
print(top_3[-3:])