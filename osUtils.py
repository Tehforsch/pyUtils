import os, subprocess

def executeExactCommand(workFolder, command):
    """Run a command system command and return the output. Change to the workfolder afterwards. """
    out, err = runCommand(command)
    # Change back for safety
    os.chdir(workFolder)
    return out + err

def executeStandardCommand(workFolder, fname, command):
    """Execute the command on the file fname by switching into the path of fname, running the command
    and switching back to workFolder afterwards."""
    # cd into the directory 
    folder, filename = os.path.split(fname)
    os.chdir(folder)
    out, err = runCommand(command + " " + filename)
    # And then change back
    os.chdir(workFolder)
    return out + err

def runCommand(command):
    """Runs the system command and returns output and errors"""
    p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, errors = p.communicate()
    return output, errors
