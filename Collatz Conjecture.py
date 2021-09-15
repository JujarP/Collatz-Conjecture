# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 17:40:06 2021

Collatz Conjecture Solver
Enter a random positive integer
If the integer is odd then multiply by 3 and add 1
If the integer is even then divide by 2
Repeat the pattern with the results
All solutions for positive integer seeds should converge to 1->4->2->1 pattern
This is the so-called 3n+1 problem

@author: Jujar Panesar
https://github.com/JujarP
"""

##################
#IMPORT LIBRARIES#
##################


import matplotlib.pyplot as plt 


########################
#ENTER USER INPUTS HERE#
########################


initial_int = 123456                #Enter any positive integer
iter_limit = 10000000               #Max number of iterations
verbose = 0                         #verbose = 0 yields no output
                                    #verbose = 1 yields output

######################
#MAIN COMPUTE PROGRAM#                                    
######################


pos_int = initial_int               #Required to not overwrite initial_int
my_iter = 0                         #Initialise iteration number
iter_list = [0]                     #Initialise iteration list
pos_int_list = [pos_int]            #Initialise positive integer list

if (verbose == 1):
    print('Iter','Integer value'
          ,sep='\t')                #Headers for verbose output
    print(my_iter,pos_int,sep='\t') #Print initial seed integer at iteration 0
        
while (pos_int > 0) and \
    (pos_int_list.count(1.0)<1):
    if pos_int%2 == 0:              #If even integer divide by 2
        pos_int=pos_int/2           #Update integer for next iteration
    else:
        pos_int=(3*pos_int)+1       #If odd integer multiply 3 add 1
    
    my_iter = my_iter + 1           #Update iteration
    iter_list.append(my_iter)       #Append iterations in list for plotting
    pos_int_list.append(pos_int)    #Append integers in list for plotting
    
    if (verbose == 1):
        print(my_iter,pos_int,
              sep='\t')             #Output iteration and integers if verbose
    

##################
#PLOTTING ROUTINE#                                    
##################


fig, (ax1, ax2) = plt.subplots\
    (2, 1, figsize=(8,8))           #Subplots, 2 by 1 
last_element = iter_list[-1]        #Last element in the iteration list
print(last_element)
fig.suptitle('Collatz conjecture,' 
             ' initial integer is {}.'
             '\nSolution takes {} iterations'
             'to reach finality.'
             .format(initial_int,last_element),
             fontsize=15, y=1.05)
fig.tight_layout()                  #Keep subplots close together

ax1.plot(iter_list,
         pos_int_list,'.-')         #Plot top chart
ax1.set_ylabel('Integer value'
               ,fontsize=15)

ax2.plot(iter_list,
         pos_int_list,'.-')         #Plot bottom chart
ax2.set_xlabel('Iteration',
               fontsize=15)
ax2.set_ylabel('Integer value'
               ' ($\log_{10}$)',
               fontsize=15)
ax2.set_yscale("log")               #Log10 scale for bottom chart

ax1.grid(which='both', 
         axis='both', linestyle='-')
ax2.grid(which='both', 
         axis='both', linestyle='-')

ax1.set_xlim(xmin=0)                #Set minimum x-axis for top chart 
ax2.set_xlim(xmin=0)                #Set minimum x-axis for bottom chart 
ax1.set_ylim(ymin=0)                #Set minimum y-axis for top chart 

plt.savefig('Initial integer'
            'seed %s.png' % 
            (str(initial_int)),
            bbox_inches = 'tight')  #Save the figure
plt.show()