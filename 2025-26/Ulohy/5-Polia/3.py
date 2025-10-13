import random

team_a = [random.randint(0, 10) for x in range(20)]
team_b = [random.randint(0, 10) for x in range(20)]

avg_a = sum(team_a) / len(team_a)
avg_b = sum(team_b) / len(team_b)

print(f"tim A: {", ".join(str(x) for x in team_a)}; priemer: {avg_a}")
print(f"tim B: {", ".join(str(x) for x in team_b)}; priemer: {avg_b}")

if sum(team_a) > sum(team_b):
    print("vyhral tim A")
else:
    print("vyhral tim B")