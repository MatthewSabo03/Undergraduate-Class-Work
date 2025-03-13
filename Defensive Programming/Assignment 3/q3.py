buffer = []
i=0
z=0

while(i < buffer.length and buffer[i] != 0):
    
    if(buffer[i] >= 'a' and buffer[i] <= 'z'):
        buffer[i] -= 32
    
    if((buffer[i] >= 'A' and buffer[i] <= 'Z') or offline):
        processSymbol(buffer[i])
    else if(buffer[i] >= '0' and buffer[i] <= '9'):
        signalTerminal(buffer[i])
    else:
        displayErrorMessage(buffer[i])
    
    i+=1
        