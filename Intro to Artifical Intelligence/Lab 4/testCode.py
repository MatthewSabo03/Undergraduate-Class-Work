import sys
import pylightxl as xl

'''
    Calculate the probabilites of each of my features given play being yes or no.
    Calculate the probability of just play    
'''
def featProb():
    # opens excel file from specified directory
    file = xl.readxl(fn=r"C:/Users/sabom/Downloads/cisc340_fa20_11_Data.xlsx")
    
    # Variable Declarations
    # Note : I'm so sorry
    yPlay=0
    nPlay=0
    ySun = 0
    nSun =0
    yRain = 0
    nRain = 0
    yOvercast = 0
    nOvercast = 0
    yCold = 0
    nCold = 0
    yMild = 0
    nMild = 0
    yHot = 0
    nHot = 0
    yNormal = 0
    nNormal = 0
    yHigh = 0
    nHigh = 0
    yWindy = 0
    nWindy = 0
    yNotWindy = 0
    nNotWindy = 0
    
    # Puts all data in col E (Play) into a list
    play = file.ws(ws='Sheet').col(col=5)
    
    # Iterates over list to find yes and no totals for probability calculations
    for i in range(0, len(play)):
        if play[i] == 'Yes':
            yPlay +=1
        elif play[i] == 'No':
            nPlay +=1
            
    # Variables for later calculations
    yPlayp = yPlay/(len(play)-1)
    nPlayp = nPlay/(len(play)-1)
                    
    # Overall for loop, will loop through every range to calculate probabilities of each feature
    for num in range(1, 5):
        colData = file.ws(ws='Sheet').col(col=num)
        
        for i in range(0, len(colData)):
            match colData[i]:
                case "Sunny":
                    if play[i] == 'Yes':
                        ySun +=1
                        sunY = ySun/yPlay
                    if play[i] == 'No':
                        nSun +=1
                        sunN = nSun/nPlay
                
                case "Rainy":
                    if play[i] == 'Yes':
                        yRain +=1
                        rainY = yRain/yPlay
                    if play[i] == 'No':
                        nRain +=1
                        rainN = nRain/nPlay
                
                case "Overcast":
                    if play[i] == 'Yes':
                        yOvercast +=1
                        overCastY = yOvercast/yPlay
                    if play[i] == 'No':
                        nOvercast +=1
                        overCastN = nOvercast/nPlay
                
                case "Cold":
                    if play[i] == 'Yes':
                        yCold+=1
                        coldY = yCold/yPlay
                    if play[i] == 'No':
                        nCold+=1
                        coldN = nCold/nPlay
                
                case "Mild":
                    if play[i] == 'Yes':
                        yMild+=1
                        mildY = yMild/yPlay
                    if play[i] == 'No':
                        nMild+=1
                        mildN = nMild/nPlay
                
                case "Hot":
                    if play[i] == 'Yes':
                        yHot+=1
                        hotY = yHot/yPlay
                    if play[i] == 'No':
                        nHot+=1
                        hotN = nHot/nPlay
                
                case "Normal":
                    if play[i] == 'Yes':
                        yNormal+=1
                        normalY = yNormal/yPlay
                    if play[i] == 'No':
                        nNormal+=1
                        normalN = nNormal/nPlay
                
                case "High":
                    if play[i] == 'Yes':
                        yHigh+=1
                        highY = yHigh/yPlay
                    if play[i] == 'No':
                        nHigh+=1
                        highN = nHigh/nPlay
                
                case "Yes":
                    if play[i] == 'Yes':
                        yWindy+=1
                        windyY = yWindy/yPlay
                    if play[i] == 'No':
                        nWindy+=1
                        windyN = nWindy/nPlay
                
                case "No":
                    if play[i] == 'Yes':
                        yNotWindy+=1
                        nWindyY = yNotWindy/yPlay
                    if play[i] == 'No':
                        nNotWindy+=1
                        nWindyN = nNotWindy/nPlay
    
    ################################################################################
    # Calculating Bayes Theorem with previous probabilities for P(X|Class)P(Class) #
    ################################################################################
    
    # P(X|Play=Yes)P(Play=Yes)
    pYes = sunY*rainY*overCastY*coldY*mildY*hotY*normalY*highY*windyY*nWindyY*yPlayp
    
    # P(X|Play=No)P(Play=No)
    pNo = sunN*rainN*overCastN*coldN*mildN*hotN*normalN*highN*windyN*nWindyN*nPlayp
    
    # P(X) = P(X|Play=Yes)P(Play=Yes)+P(X|Play=No)P(Play=No)
    pX = pYes+pNo
    
    # P(Play=Yes|X)
    playYesX = pYes/pX
    
    # P(Play=No|X)
    playNoX = pNo/pX
    
    ##################################################
    ################# Outputs ########################
    ##################################################
    if True:
        # Outlook = Sunny
        print("Outlook is Sunny and Play is Yes: ", str(round(sunY*100,2)), "%")
        print("Outlook is Sunny and Play is No: ", str(round(sunN*100)), "%\n")
        # Outlook = Rainy
        print("Outlook is Rainy and Play is Yes: ", str(round(rainY*100,2)), "%")
        print("Outlook is Rainy and Play is No: ", str(round(rainN*100,2)), "%\n")
        # Outlook = Overcast 
        print("Outlook is Overcast and Play is Yes: ", str(round(overCastY*100,2)), "%")
        print("Outlook is Overcast and Play is No: ", str(round(overCastN*100,2)), "%\n")
        # Temperature = Cold
        print("Temperature is Cold and Play is Yes: ", str(round(coldY*100,2)), "%")
        print("Temperature is Cold and Play is No: ", str(round(coldN*100,2)), "%\n")
        # Temperature = Mild
        print("Temperature is Mild and Play is Yes: ", str(round(mildY*100,2)), "%")
        print("Temperature is Mild and Play is No: ", str(round(mildN*100,2)), "%\n")
        # Temperature = Hot
        print("Temperature is Hot and Play is Yes: ", str(round(hotY*100,2)), "%")
        print("Temperature is Hot and Play is No: ", str(round(hotN*100,2)), "%\n")
        # Humidity = Normal
        print("Humidity is Normal and Play is Yes: ", str(round(normalY*100,2)), "%")
        print("Humidity is Normal and Play is No: ", str(round(normalN*100,2)), "%\n")
        # Humidity = High
        print("Humidity is High and Play is Yes: ", str(round(highY*100,2)), "%")
        print("Humidity is High and Play is No: ", str(round(highN*100,2)), "%\n")
        # Windy = Yes
        print("It is Windy and Play is Yes: ", str(round(windyY*100,2)), "%")
        print("It is Windy and Play is No: ", str(round(windyN*100,2)), "%\n")
        # Windy = No
        print("It is not Windy and Play is Yes: ", str(round(nWindyY*100,2)), "%")
        print("It is not Windy and Play is No: ", str(round(nWindyN*100,2)), "%\n")
        # Probability of Playing
        print("Probability of Playing: ", str(round(playYesX*100,2)), "%")
        print("Probability of Not Playing: ", str(round(playNoX*100,2)), "%")

featProb()