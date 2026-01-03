from PythonBasicsLectures.Constructors import Calculator


class inherit(Calculator):
    c=100
    def __init__(self):
        Calculator.__init__(self,2,10) ## Here we are calling the parent's or super class constructors to intialize the object instances.

    def overallcalculation(self):
        return (self.summation() + self.c)

object1=inherit()
print ("The Total is ", object1.overallcalculation())