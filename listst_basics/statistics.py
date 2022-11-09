n_lines = int(input())
pos_numbers = []
neg_numbers = []

for _ in range(n_lines):
    command = int(input())
    if command >= 0:
        pos_numbers.append(command)
    else:
        neg_numbers.append(command)
print(pos_numbers)
print(neg_numbers)
print(f"Count of positives: {len(pos_numbers)}")
print(f"Sum of negatives: {sum(neg_numbers)}")