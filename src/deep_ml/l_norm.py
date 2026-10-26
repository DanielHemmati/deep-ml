import numpy as np

v = np.array([3, -4])

l1 = np.linalg.norm(v, ord=1)
l2 = np.linalg.norm(v, ord=2)
linf = np.linalg.norm(v, ord=np.inf)

print(l1)
print(l2)
print(linf)
