def adj(x):
    Argentina = ["Bolivia", "Brasil", "Chile", "Paraguay", "Uruguay"]
    Brasil = [Argentina, Bolivia, Colombia, Guyana, "Guyane", "Paraguay", "Peru", "Suriname", "Venezuela"]
    Bolivia = [Argentina, Brasil, Chile, Paraguay, Peru]
    Colombia = [Brasil, Ecuador, Peru, Venezuela]
    Chile = [Argentina, Bolivia, Peru]
    Ecuador = [Colombia, Peru]
    Guyana = [Brasil, Suriname, Venezuela]
    Guyane = [Brasil, Venezuela]
    Paraguay = [Argentina, Brasil, Bolivia]
    Peru = [Brasil, Bolivia, Chile, Ecuador]
    Uruguay = [Argentina, Brasil]
    Suriname = [Brasil, Guyana, Guyane]
    Venezuela = [Brasil, Colombia, Guyana]

def countryColor(x):
    Argentina = None
    Brasil = None
    Bolivia = None
    Colombia = None
    Chile = None
    Ecuador = None
    Guyana = None
    Guyane = None
    Paraguay = None
    Peru = None
    Uruguay = None
    Suriname = None
    Venezuela = None
    
    
def colorMap(map):
    colorIndex= []
    output = []
    colors = ["red", "green", "yellow", "blue"]
    country = ["Argentina", "Brasil", "Bolivia", "Colombia", "Chile", "Ecuador", "Guyana", 
               "Guyane", "Paraguay", "Peru", "Uruguay", "Suriname", "Venezuela"]
    i=0
    
    # Loops through every element in country
    while len(country)>i:
        current = country[i]
        currColor = 0
        # Loop through every color until one is assigned
        for x in colors:
            # Sets country color to red if there is no color assigned
            if countryColor[current] == None:
                countryColor[current] = colors[currColor]
                # Adds name and country color for later refrencing
                colorIndex.append((current, countryColor(current)))
            
            # Adjacency check and current country color
            colorAdj = False
            
            # Loops through adjacent countries of current country
            for a in adj[current]:
                #Checks if colors are touching
                colorAdj = colorCheck(current, a, countryColor)
                #breaks the loop if there is an adjacent color
                if colorAdj == True:
                    break
                
            # If there is not an adjacent color
            if colorAdj == False:
                # Adds tuple to the final output as defined in colorIndex
                output.append(colorIndex[0])
                # clears colorIndex
                colorIndex.pop()
                break
            
            # If there is an adjacent color
            if colorAdj == True:
                # Wipe current color
                countryColor[current] = None
                # adds to the current color and then starts the loop over again
                currColor += 1
            
        i+=1
        
    return output

def colorCheck(current, adj, countryColor):
    colorAdj = False
    if countryColor[current] == countryColor[adj]:
        colorAdj = True
        
    return colorAdj
