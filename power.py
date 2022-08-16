#I want to create a script that would allow me to either restart, shutdown or logoff a system

#Useful libraries that I would be working with -->
import os
import sys
import traceback

#Declaring the various variables
class Control:
    def __init__(self):
        pass

    #This function restarts the system
    def restart(self):
        func = os.system("shutdown /r /t 1")
        return func

    #This function shutsdown the system
    def shutdown(self):
        func = os.system("shutdown /s /t 1")
        return func

    #This function log's off the system
    def logoff(self):
        func = os.system("shutdown -l")
        return func

    #This function performs the power switching depending on the specified mode
    def switch(self, mode = None):
        try:
            if mode == "restart":
                func = self.restart()
                pow = f"System {mode} successfully" 
            elif mode == "shutdown":
                func = self.shutdown()
                pow = f"System {mode} successfully" 
            elif mode == "logoff":
                func = self.logoff()
                pow = f"System {mode} successfully" 
            else:
                raise ValueError("Invalid mode input")
        except:
            pow = traceback.format_exc()
        
        return pow


if __name__ == "__main__":
    print("POWER CONTROLLER \n")

    mode = "shutdown"
    switch = Control().switch(mode)
    print(switch)

    print("\nExecuted successfully")