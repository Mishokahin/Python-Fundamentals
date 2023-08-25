n = int(input())
inputs = [int(input()) for i in range(n)]
positives = [i for i in inputs if i >= 0]
negatives = [i for i in inputs if i < 0]
print(positives)
print(negatives)
print(f"Count of positives: {len(positives)} \nSum of negatives: {sum(negatives)}")