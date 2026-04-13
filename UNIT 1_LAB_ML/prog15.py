import numpy as np
data = b'hello'
arr = np.frombuffer(data, dtype=np.uint8)
print(arr) 
