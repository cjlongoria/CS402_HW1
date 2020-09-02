import numpy as np
import time
import cpuinfo
import platform

def create_matrix_int():
    #Matrix of ints
    A = np.random.randint(100, size=(300, 700), dtype=np.intc)
    B = np.random.randint(100, size=(700, 300), dtype=np.intc)
    return (A, B)

def create_matrix_dfloat():
    # Matrix of double floats
    A = np.random.rand(300, 700)
    B = np.random.rand(700, 300)
    return (A, B)

def good_multiply(A, B):
    #Improved multiplication method
    npdot = np.dot(A, B)

def bad_multiply(A, B):
    badmultiply = [[0 for x in range(300)] for y in range(300)] 
    for i in range(len(A)): 
        for j in range(len(B[0])): 
            for k in range(len(B)): 
                badmultiply[i][j] += A[i][k] * B[k][j]  

def printinfo():
    print('OS: ', platform.system())
    print('Release: ', platform.release())
    print('Version: ', platform.version())
    print('Python version: ', cpuinfo.get_cpu_info()['python_version'])
    print('Architecture: ', cpuinfo.get_cpu_info()['arch'])
    print('Brand Name: ', cpuinfo.get_cpu_info()['brand_raw'])
    print('L3 cache: ', cpuinfo.get_cpu_info()['l3_cache_size']) 
    print('L2 cache: ', cpuinfo.get_cpu_info()['l2_cache_size'])
    print('L1 cache: ', cpuinfo.get_cpu_info()['l1_data_cache_size'])

def goodjob(dtypes):
    for i in range(5):
        start_time = time.time()
        A, B = dtypes
        good_multiply(A, B)
        print(f"--- {(time.time() - start_time)} seconds ---")

def badjob(dtypes):
    for i in range(5):
        start_time = time.time()
        A, B = dtypes
        bad_multiply(A, B)
        print(f"--- {(time.time() - start_time)} seconds ---")


print('---------------------------------------------------------------')
print('Using the column by row multiplication method')
print('Integer matrix multiplication')
badjob(create_matrix_int())
print()
print('Double float matrix multiplication')
badjob(create_matrix_dfloat())
print()
print('---------------------------------------------------------------')
print()
print('Using a new and improved multiplication method (numpy dot product)')
print('Integer matrix multiplication')
goodjob(create_matrix_int())
print()
print('Double float matrix multiplication')
goodjob(create_matrix_dfloat())

print('-----------------System Info-----------------')
printinfo()