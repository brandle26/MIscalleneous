## This module will have methods for computing various parameters
## in space mechanics

import math

class space_mechanics(object):
    
    def __init__(self,name):
        self.name=name
        self.G=66.73e-12  #universal constant of gravitation in m^3/(kg*s^2)
        self.M_e=5.972e+24  #mass of earth in kilogram
        print("%s is ready for launch"%name)

    def launch(self):
        for i in range(5,0,-1):
            print(i)
        print("Blas off")
        
    def circular_path(self,perigee):
        #perigee is the minimum distance from a satellite's orbit to
        #the centre of the earth ( one of the foci of the orbit)
        self.perigee=perigee
        v_c=math.sqrt((self.G*self.M_e)/perigee)
        print("cicular path velocity is %.2f m/s"%v_c)
        #print("The velocity required to launch %s into cicular orbit \
        #     is %.2f m/s"%(name,v_c))

    def escape_vel():
        print("construction")
        


if __name__=="__main__":
    print("You are running the module directly")
