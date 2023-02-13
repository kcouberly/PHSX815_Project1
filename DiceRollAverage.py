import sys
import numpy as np

sys.path.append(".")
from Random import Random
random = Random()

# main function for dice roll averager
if __name__ == "__main__":
    # if the user includes the flag -h or --help print the options
    if '-h' in sys.argv or '--help' in sys.argv:
        print ("Usage: %s [-seed number] [-Nsides number] [-Nrolls number] [-Ntrials number]" % sys.argv[0])
        print ("Outputs file to 'output.txt' ")
        sys.exit(1)
    # default seed
    seed = 5555
    
    #default number of sides
    n_sides = 6
    #default number of rolls to collect average
    n_rolls = 10
    #default number of trials to create the distribution
    n_trials = 1000
    # read the user-provided seed from the command line (if there)
    if '-seed' in sys.argv:
        p = sys.argv.index('-seed')
        seed = sys.argv[p+1]
    #read the other parameters (if there)
    if '-Nsides' in sys.argv:
        p = sys.argv.index('-Nsides')
        Ns = int(sys.argv[p+1])
        if Ns > 0:
            n_sides = Ns            
    if '-Nrolls' in sys.argv:
        p = sys.argv.index('-Nrolls')
        Nr = int(sys.argv[p+1])
        if Nr > 0:
            n_rolls = Nr
    if '-Ntrials' in sys.argv:
        p = sys.argv.index('-Ntrials')
        Nt = int(sys.argv[p+1])
        if Nt > 0:
            n_trials = Nt
   
    #loop that writes results to output file
    output = open('output.txt','w')
    for x in range(n_trials):
        #empty array to collect averages
        rolls = []
        for i in range(n_rolls):
            rolls.append(random.categorical(n_sides))
        avg = np.mean(np.asarray(rolls))
        output.write(str(avg)+" \n")