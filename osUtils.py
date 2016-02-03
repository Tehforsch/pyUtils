import os, subprocess

def executeCommand(workFolder, fname, command):
    """Switch to the path of the file fname. Execute the command and then switch back to workFolder"""
    # cd into the directory 
    folder, filename = os.path.split(fname)
    os.chdir(folder)
    out, err = runCommand(command)
    # And then change back
    os.chdir(workFolder)
    return out + err

def runCommand(command):
    """Runs the system command and returns output and errors"""
    p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, errors = p.communicate()
    return output, errors
