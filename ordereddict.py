class OrderedDict:
    """
    This aim of this class is to create a sortable dict.
    The object must work like a dictionnary AND like a list.
    """

    def __init__(self, *entree):
        """
        the constructor creates le empty dictolist and, if needed, load the input data
        """
        self.keyslist = []
        self.valueslist = []

        if len(entree) != 0: #if there is parameters
            for data in entree: #for each parameter
                if type(data) is dict: #if the parameter is a dict
                    for keys in data: #for each key in the dict
                        self.keyslist.append(keys) #append data keys to keyslist
                        self.valueslist.append(data[keys]) #append data values to valueslist
                else:
                    pass #if data are set as parameters, like a usual dictionnary creation

    def __getitem__(self, entree):
        """
        OrderedDict[entree]
        """
        try:
            temp = self.keyslist.index(entree) #if the key does not exist, index raise an error
            return self.valueslist[temp]
        except:
            return "Key does not exist" #going back, nothing to get

    def __setitem__(self, entree, valeur):
        """
        OrderedDict[entree] = valeur
        """
        if entree not in self.keyslist:
            self.keyslist.append(entree)
            self.valueslist.append(valeur)
        else:
            temp = self.keyslist.index(entree)
            self.valueslist[temp] = valeur

    def __delitem__ (self, entree):
        """
        del OrderedDict[entree]
        """
        try:
            temp = self.keyslist.index(entree) #if the key does not exist, index raise an error
        except:
            return "Key does not exist" #going back, nothing to delete
        
        del self.keyslist[temp]
        del self.valueslist[temp]

    def __contains__(self, entree):
        """
        entree in OrderedDict
        """
        try:
            temp = self.keyslist.index(entree)
            return True
        except:
            return False
        
    def __len__(self):
        """
        len(OrderedDict)
        """
        longueur = len(self.keyslist)
        return longueur

    def __repr__(self):
        """
        display dictionnary with a direct call from the interpretor
        """
        out = "{"
        for i in range(len(self.keyslist)):
            if type(self.keyslist[i]) is str:
                out += "\'" + self.keyslist[i] + "\'" + ": "
            else:
                out += str(self.keyslist[i]) + ": "
                
            if type(self.valueslist[i]) is str:
                out += "\'" + self.valueslist[i] + "\'"
            else:
                out += str(self.valueslist[i])
                
            if i != len(self.keyslist) - 1:
                out += ", "
        
        out += "}"
        return out

    def __str__(self):
        """
        print(OrderedDict)
        """
        out = "{"
        for i in range(len(self.keyslist)):
            if type(self.keyslist[i]) is str:
                out += "\'" + self.keyslist[i] + "\'" + ": "
            else:
                out += str(self.keyslist[i]) + ": "
                
            if type(self.valueslist[i]) is str:
                out += "\'" + self.valueslist[i] + "\'"
            else:
                out += str(self.valueslist[i])
                
            if i != len(self.keyslist) - 1:
                out += ", "
        
        out += "}"
        return out

    def __iter__(self):
        """
        iter(OrderedDict)
        """
        return ItOrDict(self)

    def __add__(self, entree):
        """
        OrderedDict + OrderedDict
        """
        
        if type(entree) is OrderedDict: #this method works only with 2 OrderedDicts
            for k in entree:
                self.keyslist.append(k)
                self.valueslist.append(entree[k])
        else:
            raise OrDictError('Only works with 2 OrderedDict')

    def sort(self, reverse = False):
        self.keyssorted = []
        self.valuessorted = []
        self.tempkey = None
        self.tempindex = None
        self.tempvalue = None
        
        while len(self.keyslist) != 0:
            self.tempkey = self.keyslist[0]
            self.tempindex = self.keyslist.index(self.tempkey)
            self.tempvalue = self.valueslist[self.tempindex]
            
            for k in self.keyslist:
                if reverse == False:
                    if str(k) < str(self.tempkey):
                        self.tempkey = k
                        self.tempindex = self.keyslist.index(k)
                        self.tempvalue = self.valueslist[self.tempindex]
                else:
                    if str(k) > str(self.tempkey):
                        self.tempkey = k
                        self.tempindex = self.keyslist.index(k)
                        self.tempvalue = self.valueslist[self.tempindex]
            
            self.keyssorted.append(self.tempkey)
            self.valuessorted.append(self.tempvalue)
            
            self.keyslist.pop(self.tempindex)
            self.valueslist.pop(self.tempindex)
        
        self.keyslist = self.keyssorted
        self.valueslist = self.valuessorted
            
        return None
        
class ItOrDict:
    """
    create OrderedDict's iterator
    """
    def __init__(self, entree):
        """
        The constructor create all the usefull variables for __next__
        """
        self.dicolist = entree
        self.posmax = len(entree)
        self.pos = 0
        self.keytemp = ""
        #self.valtemp = ""
        
    def __next__(self):
        """
        method called during the iteration
        """
        if self.pos == self.posmax:
            raise StopIteration
        
        self.keytemp = self.dicolist.keyslist[self.pos]
        #self.valtemp = self.dicolist.valueslist[self.pos]
        self.pos += 1
        #return self.keytemp, self.valtemp
        return self.keytemp

class OrDictError(Exception):
    """
    OrderedDict special error
    """
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)
