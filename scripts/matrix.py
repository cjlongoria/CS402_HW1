import numpy as np
import time

for i in range(5):
    start_time = time.time()

    #Matrix of ints
    A = np.random.randint(100, size=(300, 700), dtype=np.intc)
    # B = np.random.randint(100, size=(700, 300), dtype=np.intc)

    # Matrix of double floats
    # A = np.random.rand(300, 700)
    B = np.random.rand(700, 300)

    print(type(A[0][0]))
    print(type(B[0][0]))
    
    #Improved multiplication method
    # npdot = np.dot(A, B)

    # badmultiply = [[0 for x in range(300)] for y in range(700)] 
    # for i in range(len(A)): 
    #     for j in range(len(B[0])): 
    #         for k in range(len(B)): 
    #             badmultiply[i][j] += A[i][k] * B[k][j]  

    # print(f"--- {(time.time() - start_time)} seconds ---")