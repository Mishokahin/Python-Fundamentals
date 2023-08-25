inputs = [input() for i in range(3)]
meerkat = [inputs[i] for i in range(len(inputs)-1, -1, -1 )]
print(meerkat)