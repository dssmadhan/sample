from scipy import sparse as s
import numpy as np

arr = np.array([
  [0, 1, 2],
  [1, 0, 0],
  [2, 0, 0]
])

n = s.csr_matrix(arr)
print(s.csgraph.dijkstra(n,return_predecessors=True,indices=1))