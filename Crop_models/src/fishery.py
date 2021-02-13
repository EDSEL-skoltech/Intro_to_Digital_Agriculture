import numpy as np

N = 1 # Number of realizations of environmental stochasticity

tSteps = 100 # no. of timesteps to run the fish game on

effort = 0.2 # harvesting effort

# Define problem to be solved
def fish_game(a = 0.005, # rate at which the prey is available to the predator
              b = 0.5, # prey growth rate
              c = 0.5, # rate with which consumed prey is converted to predator abundance
              h = 0.1, # handling time (time each predator needs to consume the caught prey)
              K = 2000, # prey carrying capacity given its environmental conditions
              m = 0.7): # predator interference parameter

    
    d = 0.1 # predator death rate   
    sigmaX = 0.004 # variance of stochastic noise in prey population
    sigmaY = 0.004 # variance of stochastic noise of predator population  
      
    x = np.zeros(tSteps+1) # Create prey population array
    y = np.zeros(tSteps+1) # Create predator population array

    # Create array to store prey for all realizations
    prey = np.zeros([N,tSteps+1])
    # Create array to store predator for all realizations
    predator = np.zeros([N,tSteps+1])
    
    # Create array to store metrics per realization
    NPV = np.zeros(N)
    
    # Create array with environmental stochasticity for prey
    epsilon_prey = np.random.normal(0.0, sigmaX, N)
    
    # Create array with environmental stochasticity for predator
    epsilon_predator = np.random.normal(0.0, sigmaY, N)

    # Go through N possible realizations
    for i in range(N):
        # Initialize populations and values
        x[0] = prey[i,0] = K
        y[0] = predator[i,0] = 250
        NPVharvest = effort*x[0]        
        # Go through all timesteps for prey, predator, and harvest
        for t in range(tSteps):
            if x[t] > 0 and y[t] > 0:
                x[t+1] = (x[t] + b*x[t]*(1-x[t]/K) - (a*x[t]*y[t])/(np.power(y[t],m)+a*h*x[t]) - effort*x[t])* np.exp(epsilon_prey[i]) # Prey growth equation
                y[t+1] = (y[t] + c*a*x[t]*y[t]/(np.power(y[t],m)+a*h*x[t]) - d*y[t]) *np.exp(epsilon_predator[i]) # Predator growth equation
            prey[i,t+1] = x[t+1]
            predator[i,t+1] = y[t+1]
            NPVharvest += effort*x[t+1]*(1+0.05)**(-(t+1))
        NPV[i] = NPVharvest
    
    return (np.mean(NPV)) # Mean number of predator extinction days per realization