import sys
import math
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    # if the user includes the flag -h or --help print the options
    if '-h' in sys.argv or '--help' in sys.argv:
        print ("Usage: %s" % sys.argv[0])
        print ("   -input [filename]  name of file for data")
        print("    -Nsides [N] for number of sided dice used")
        print
        sys.exit(1)
        
    haveInput = False
        
    if '-input' in sys.argv:
        p = sys.argv.index('-input')
        InputFile = sys.argv[p+1]
        haveInput = True
        
    if '-Nsides' in sys.argv:
        p = sys.argv.index('-Nsides')
        N = int(sys.argv[p+1])
    else:
       #default number of sides
        N = 6
    #loading in file
    #defaults to load 'output.txt'
    if haveInput == False:
        data = np.loadtxt('output.txt')
    else:
        data = np.loadtxt(InputFile)
    #range of possible dice rolls for histogram
    roll_bins = []
    for x in range(1,N+1):
        roll_bins.append(x)
    
    #histogram of the averages
    n, bins, patches = plt.hist(data, bins=roll_bins, alpha=0.7 ,rwidth=0.95, density = True, facecolor = "blue")
    plt.xlabel('Roll Average')
    plt.ylabel('Probability')
    plt.title(str(N) + ' sided die - ' + str(len(data)) + ' trials')
    plt.grid(axis='y', alpha=0.75)
    
    #number of times average >=5 or <=2
    #loop that counts these times
    count = 0
    for x in data:
        if x>=5:
            count += 1
    print('number of times above 5:',count)
    prob = count/len(data)
    print('probability',prob)
              