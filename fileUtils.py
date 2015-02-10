import os

def readFile(fname):
    """Return a list containing all lines in the file fname"""
    """Returns the lines contained in fname in standard list format"""
    f = open(fname, "r")
    lines = f.readlines()
    f.close()
    return lines

def writeFile(fname, content):
    """Writes the content into a file of path fname"""
    f = open(fname, "w")
    f.write(content)
    f.close()

def getFileType(fname):
    """Extracts the file ending of file name by returning everything after the first point (not including the point)"""
    ending = os.path.splitext(fname)[1]
    if ending == "":
        return None
    return ending.replace(".", "")

def getFilePath(fname):
    """Extracts the file path of path + file name"""
    return os.path.split(fname)[0] + "/"

def getFileName(fname):
    """Extracts the file name of path + file name"""
    return os.path.split(fname)[1]

def mergePaths(relPath1, relPath2):
    """Merge the two paths which point and convert them to a standard absolute path
    (deleting .. links etc)"""
    return os.path.abspath(os.path.join(os.path.dirname(relPath1), relPath2))

def ensureAbsPath(fileName, path):
    """Check if fileName is not yet absolute. If this is true merge the filename with path to make it absolute."""
    if fileName[0] != "/":
        return mergePaths(path, fileName)
    return fileName
