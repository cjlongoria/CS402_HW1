# CS402


### 1 (a) Using trace files, i.e. files that contain addresses issued by some CPU to execute some application(s), draw the histogram of address distribution for each of them (2x20 points). On the Ox axis of the plot you will have the address number (don't start with zero, rather with the smallest address you find in the file and go up to the maximum address in the file). On the Oy axis you will have the number of occurrences for each particular address. 

<img src="images/Hw1_hist1_spice.png">
<img src="images/Hw1_hist1_tex.png">

### Comment based on the histograms (5). 
It is interesting that the histograms look similar even though they are different programs. I believe this is the case because grouping addresses together allows for a speed up in execution. I'm not sure why both programs have a large gap in memory addresses.

### (b) What is the frequency of writes (5)? What is the frequency of reads (5)? Please comment on these results (5). 

<img src="images/Hw1_bar_spice.png">
<img src="images/Hw1_bar_tex.png">

The spice.din file has 150699 reads and 66538 writes. The tex.din file has 130655 reads and 104513 writes. This makes sense as there are numerous read commands to move between the data stored in the program's registers vs actually writing information to memory.

### 2. (a) Write a program, using your favorite programming language, that multiplies two rectangular matrices -- please no square matrices -- whose elements are randomly generated. You will have two versions of the program, one in which matrix elements are integers and another one where they are real numbers (double) (2x15 points). 

<br>

Check out the [python script](scripts/matrix.py). I continued this script to include a new multiplication method to satisfy the requirements for Question 2 of this homework. 

<br>

### Measure the time it takes each program to complete (2x5) and then compare the performance of the two systems (5). Since the matrices are randomly generated, you will have to run the program several times, measure the running time and then take the average. Also the running time has to be significantly large (many seconds) to avoid measuring errors; this means you will have to work with matrices that have at least hundreds of lines and columns.  

<br>

#### **Integer Matrix Table (PC 1)**

| Trial | Runtime (seconds)       
| ----|-------------:
| 1| 44.6271789073944 
| 2| 47.1883685588837     
| 3| 47.3448393344879
| 4| 48.0673696994782
| 5| 47.1904964447022
|**Average**| **46.8836505889893**


<br>

#### **Double Float Matrix Table (PC 1)**

| Trial | Runtime (seconds)       
| ----|-------------:
| 1| 49.2166802883148
| 2| 49.6764869689941 
| 3| 49.6632924079895
| 4| 49.3716456890106
| 5| 49.098571062088
|**Average**| **49.4053352832794**

<br>
<br>

#### **Integer Matrix Table (PC 2)**

| Trial | Runtime (seconds)       
| ----|-------------:
| 1|  41.9794256687164
| 2|  41.5572998523712   
| 3|  41.5685186386108
| 4|  41.9278135299683
| 5|  41.9896602630615
|**Average**| **41.8045435905457**

<br>

#### **Double Float Matrix Table (PC 2)**

| Trial | Runtime (seconds)       
| ----|-------------:
| 1|  38.3396198749542
| 2|  38.3266286849976    
| 3|  38.7765784263611
| 4|  38.2493479251862
| 5|  38.1020042896271
|**Average**| **38.3588358402252**

<br>
<br>

#### **Performance Comparison**

| Matrix Type| Average PC 1 runtime (seconds)| Average PC 2 runtime (seconds)| 
|--------|:--------:|:--------:|
|Integer| 46.88365 | 41.80454 
|Double Float| 49.40534 | 38.35884

Comparing the two machines; PC 2 ran faster in both integer matrix multiplication (1.1215 times faster) and double float matrix multiplication (1.288 times faster). 
<br>
<br>
I found it interesting that double float matrix multiplication was a faster operation on PC 2 compared to integer matrix multiplication. Prior to measuring the results I thought it would be the reverse. Some quick post-experiment research indicates this is a Python quirk that many people have experienced.

<br>

### Is the performance ratio the same as the clock rate ratio of the two systems (5)? Explain. Based on the retail price of the two systems, which one is more cost effective (5)? 
<br>
The performance ratio, briefly mentioned above, is simply the time for one pc to execute a program divided by the time for a second pc to run the same program. Using the data above the performance ratio between PC 2 and PC 1 is 1.1215 for integer matrix multiplication and 1.288 for double float matrix multiplication
<br>
<br>
However, the clock rate ratio is considered static for both programs. This would be the clock rate of PC 1 divided by the clock rate of PC 2. The clock rate for PC 1 is 1.9 Ghz and the clock rate for PC 2 is 1.3 Ghz. Therefore, the clock rate ratio is 1.46 (1.9 Ghz/1.3Ghz).
<br>
<br>
The performance ratio does not match the clock rate ratio because there are more factors to take into consideration when measuring performance. Primarily, the clock cycles per instruction (CPI). This factor is dependent on the CPU's architecture. If this was not the case then, PC 2 (instead of PC 1) should be the faster PC with a performance ratio of 1.46.
<br>
<br>
The price for PC 1 (lenovo thinkpad t490s 20NYS) is $1700.00 and the price for PC 2 (HP Laptop 15-dy1071wm) is $650.00. Since PC 2 had a better performance ratio and a cheaper cost it is a more cost effective option.
<br>
<br>

###  (b) Change your multiplication algorithm and repeat the steps above; for instance, if you used the the naive multiplication algorithm with the column in the inner loop, then just use the same algorithm with the row in the inner loop (same scoring as part a).
<br>
<br>

Check out the [python script](scripts/matrix.py). I continued this script to include a new multiplication method to satisfy the requirements for Question 2 of this homework. The time measurements for all trials are listed here [Measurements](data/Tables.ods)

<br>
<br>

### Make sure your work includes a description of the two systems (manufacturer, CPU type, amount of memory, operating system, etc.) and of the compiler used (5). Attach the source code, the tables with your time measurements for your work, and a link to your repository such that we can check-out the code, build, and execute (5). 

<br>
<br>

| Spec | PC 1 | PC 2 | 
|:--------|:--------|:--------
| OS | Windows | Linux 
| Release | 10 | 5.4.0-45-generic 
| Version | 10.0.18362 | Ubuntu 
| Python Version | 3.8.2.final.0 (64 bit) | 3.8.2.final.0 (64 bit) 
| Architecture | X86_64 | X86_64 
| Brand Name | Intel(R) Core(TM) i7-8665U CPU @ 1.90GHz | Intel(R) Core(TM) i7-1065G7 CPU @ 1.30GHz 
| RAM | 32 GB | 8 GB 

<br>

Since I used Python. The code is compiled by the 'Python Version' listed in the above chart.

<br>
<br>

All my data and scripts are included in this zip. You can check out the repository at https://github.com/cjlongoria/CS402_HW1