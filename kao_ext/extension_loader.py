from importlib.machinery import PathFinder, SourceFileLoader
import sys

class ExtensionLoader:
    """ Helper to find and load modules that are extension modules """
    
    def __init__(self, parent_module, prefix):
        """ Initialize with the prefix to allow searching for """
        self.parent_module = parent_module + "."
        self.prefix = prefix+'_'
    
    def install(self):
        """ Install this loader into the system metapath so it can try and pre-emptively improt modules """
        sys.meta_path.append(self)
    
    def find_module(self, fullname, path=None):
        """ Method to find the given module name """
        if fullname.startswith(self.parent_module):
            path = self.getPath(fullname)
            return SourceFileLoader(fullname, path)
            
    def getPath(self, fullname):
        """ Return the proper path to the module specified in fullname """
        actualName = self.getActualModuleName(fullname)
        return PathFinder.find_spec(actualName).origin
        
    def getActualModuleName(self, fullname):
        """ Return the actual module name to import """
        return self.prefix + self.getBaseModuleName(fullname)
        
    def getBaseModuleName(self, fullname):
        """ Return the base module name """
        return fullname.replace(self.parent_module, '')