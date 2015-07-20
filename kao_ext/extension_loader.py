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
            return self
    
    def load_module(self, fullname):
        """ Load the given module """
        actualName = self.getActualModuleName(fullname)
        __import__(actualName)
        sys.modules[fullname] = sys.modules[actualName]
        return sys.modules[actualName]
        
    def getActualModuleName(self, fullname):
        """ Return the actual module name to import """
        return self.prefix + self.getBaseModuleName(fullname)
        
    def getBaseModuleName(self, fullname):
        """ Return the base module name """
        return fullname.replace(self.parent_module, '')