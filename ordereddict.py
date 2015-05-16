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

    def __getitem__(self, entree):
        """
        OrderedDict[entree]
        """
        try:
            temp = self.keyslist.index(entree)
            return self.valueslist[temp]
        except:
            return "Cette clé n\'existe pas"

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
