# Ant Colony Optimization

R1 = 30
R2 = 70

total = R1 + R2

P1 = R1 / total
P2 = R2 / total

percentage1 = P1 * 100
percentage2 = P2 * 100

print("Path 1 Probability:", percentage1, "%")
print("Path 2 Probability:", percentage2, "%")

if percentage1 > percentage2:
    print("Most ants follow Path 1.")
    print("Path 1 has the higher chance:", percentage1, "%")
else:
    print("Most ants follow Path 2.")
    print("Path 2 has the higher chance:", percentage2, "%")

#OUTPUT****
Path 1 Probability: 30.0 %
Path 2 Probability: 70.0 %

Most ants follow Path 2.
Path 2 has the higher chance: 70.0 %
