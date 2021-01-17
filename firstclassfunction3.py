# Use gitlab history to check the explaination 

def logger(msg): # outside function

    def log_message():  # inside function
        print ('Log:', msg)

    return log_message  # without ()

log_hi = logger("Hi!")
log_hi()   # This is called closure