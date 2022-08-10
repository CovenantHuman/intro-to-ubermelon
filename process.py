log_file = open("um-server-01.txt") #saves the contents of the file to a variable


def generate_sales_reports(log_file): #creates a function to interact with the file
    for line in log_file: #loops through contents of the file one line at a time
        line = line.rstrip() #removes the unneeded spaces on the right side of each line of the file
        day = line[0:3] #saves the first three characters in each line to a variable
        if day == "Mon": #checks if the variable created in the line above indicates Monday
            print(line) #adds a line to the report


generate_sales_reports(log_file) #runs the above function on the above file
