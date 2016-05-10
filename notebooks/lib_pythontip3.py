import numpy as np

def measure_nmad(a):
    """ """
    return np.median( np.abs(a-np.median(a)) ) *1.4

class MyFirstClass( object ):
    
    CLASSNAME = "the class name"
    
    def __init__(self, filename):
        self.filename = filename
        self.load_data()
        
    def load_data(self):
        """ """
        
        self.data = open(self.filename).read().splitlines()
        self.header = self.data[0].split(",")
        self.year,self.marriages,self.divorces,self.population, self.marriages_per_1000, self.divorces_per_1000 = \
        np.asarray( [ d.split(",") for d in self.data[1:] ], dtype="float").T 
        
    def get_mean_divorce(self):
        """ """
        return np.nanmean(self.divorces)
    
    def print_me_divorce_stat(self):
        """"""
        print "mean: ",np.nanmean(self.divorces)
        print "std: ",np.std(self.divorces[self.divorces==self.divorces])
        print "nmad:", measure_nmad(self.divorces[self.divorces==self.divorces])
        
        
        
        
class MySecondClass( object ):
    
    def __init__(self):
        print "hello"
     
    def print_it(self,a):
        """ it prints a """
        print a