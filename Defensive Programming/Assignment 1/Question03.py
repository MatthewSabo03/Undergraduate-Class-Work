# Question 03
#
# Code takes configuration input from a file, user input through the UI, and
# live sensor data through a network socket connection. This input is then
# combined via a forumla noted within the in-line comments and then written
# to a persistent database.
#
# You may assume that any variables used are appropriately scoped and
# initialized.

def process_datapoint():

    try:
        connectString = ""

        # I) Open, read the database connect string from, and close setup.cfg
        configFile = open("setup.cfg", "r")
        if configFile.mode == 'r':
            lineNo = 0
            contents = configFile.readlines()
            while lineNo < len(contents):
                if contents[lineNo][0:len("connectstring=")].lower() == "connectstring=":
                    connectString = contents[lineNo][len("connectstring="):] 
                if contents[lineNo][0:len("sensoraddress=")].lower() == "sensoraddress=":
                    sensorAddress = contents[lineNo][len("sensoraddress="):]
                if contents[lineNo][0:len("sensorport=")].lower() == "sensorport=":
                    port = contents[lineNo][len("sensorport="):]
        configFile.close()

        # II) Read from the three sensor reading count textboxes
        sensor1Count = int(sensor1CountBox.getText())
        sensor2Count = int(sensor2CountBox.getText())
        sensor3Count = int(sensor3CountBox.getText())

        # III) Grab the next datapoint from the sensor socket representing
        #       the sum of sensor readings since the last readings
        s = socket.socket()          
        s.connect((sensorAddress, port))
        sumOfSensorReadings = int(s.recv(1024))
        s.close()        

        # IV) Calculate average of sensor sum over the three sensor reading
        #       counts
        average = sumOfSensorReadings/(sensor1Count + sensor2Count + sensor3Count)

        # V) Connect to the database specified from the connect string
        conn = pyodbc.connect(connectString)

        # VI) Run the sensor data update stored procedure with all data
        cursor = conn.cursor()
        cursor.callproc('spUpdateSensorData',
                        (sensor1Count, sensor2Count, sensor3Count,
                         sumOfSensorReadings, average))

        # VII) Close the database connection
        cursor.close()
        connection.close()
        
    except:
        print("There has been an exception")

