from block import *
from waypoint import *
from navigator import *
from level_utils import *
import random
class Level (object):
    def scale(self,factor):
        for block in self._map:
            block.scale(factor)
        self._navigator.scale(factor)
    def level_one(self,paintLine):
        col=(.1,.5,.25)
        
        _map=[]
        _map.append(Block(100,0,750,30,col))      #A
        _map.append(Block(700,0,600,30,col))      #B
        _map.append(Block(450,0,30,200,col))      #C
        _map.append(Block(950,0,30,170,col))      #D
        _map.append(Block(1300,0,30,300,col))     #E 1200
        _map.append(Block(1300,400,30,200,col))   #E2
        _map.append(Block(1300,700,30,200,col))   #E3
        _map.append(Block(1300,1000,30,200,col))  #E4
        _map.append(Block(100,1200,1230,30,col))  #F
        _map.append(Block(1200,400,100,30,col))   #0
        _map.append(Block(950,400,100,30,col))    #N
        _map.append(Block(950,300,30,300,col))    #M
        _map.append(Block(950,700,30,300,col))    #P
        _map.append(Block(950,1100,30,120,col))   #R
        _map.append(Block(870,900,100,30,col))    #Q
        _map.append(Block(-150,900,770,30,col))   #H
        _map.append(Block(450,1100,30,120,col))   #S
        _map.append(Block(1300,1000,200,30,col))  #U
        _map.append(Block(1500,300,30,730,col))   #V
        _map.append(Block(1300,300,200,30,col))   #W
        _map.append(Block(450,700,30,300,col))    #T
        _map.append(Block(450,300,30,300,col))    #L
        _map.append(Block(-150,400,600,30,col))   #J
        _map.append(Block(100,800,30,400,col))    #G
        _map.append(Block(-150,400,30,500,col))   #I
        _map.append(Block(100,0,30,700,col))      #K

        brown=(.5,.3,.1)
        _map.append(Block(670,400,170,350,brown)) #stairs
        _map.append(Block(590,1000,250,110,brown)) #dining table
        _map.append(Block(1200,1100,30,30,brown)) #hall table
        _map.append(Block(1200,800,30,30,brown)) #hall table
        _map.append(Block(1200,150,30,30,brown)) #sitting room table
        _map.append(Block(200,500,150,60,brown)) #kitchenette table
        self._map=_map

        waypoints=[]
        a=Waypoint(300,250,"a")
        b=Waypoint(550,250,"b")
        b1=Waypoint(730,250,"b1")
        c=Waypoint(900,250,"c")
        d=Waypoint(1100,250,"d")
        e=Waypoint(1100,350,"e")
        f=Waypoint(1260,370,"f")
        g=Waypoint(1100,100,"g")
        g1=Waypoint(1260,100,"g1")
        h=Waypoint(1400,370,"h")
        i=Waypoint(1400,650,"i")
        j=Waypoint(1400,950,"j")
        k=Waypoint(1260,650,"k")
        l=Waypoint(1100,450,"l")
        m=Waypoint(1260,950,"m")
        n=Waypoint(1260,1160,"n")
        o=Waypoint(1050,650,"o")
        p=Waypoint(1050,1060,"p")
        q=Waypoint(1100,1160,"q")
        r=Waypoint(1100,950,"r")
        s=Waypoint(900,650,"s")
        t=Waypoint(900,850,"t")
        u=Waypoint(550,650,"u")
        v=Waypoint(730,850,"v")
        w=Waypoint(730,650,"w")
        x=Waypoint(550,850,"x")
        y=Waypoint(730,960,"y")
        z=Waypoint(900,960,"z")
        aa=Waypoint(900,1060,"aa")
        ab=Waypoint(900,1160,"ab")
        ac=Waypoint(550,1160,"ac")
        ad=Waypoint(550,1060,"ad")
        ae=Waypoint(550,960,"ae")  
        af=Waypoint(300,1060,"af")

        ag=Waypoint(400,650,"ag")
        ah=Waypoint(400,450,"ah")
        ai=Waypoint(170,450,"ai")
        aj=Waypoint(170,650,"aj")
        ak=Waypoint(170,750,"ak")
        al=Waypoint(0,750,"al")
        

        #make code smaller
        Nav=Navigator 

        Nav.dconn(a,b)

        Nav.dconn(b,b1)
        Nav.dconn(b,u)

        Nav.dconn(b1,c)
        Nav.dconn(b1,w)

        Nav.dconn(c,d)
        Nav.dconn(c,s)
        
        Nav.dconn(d,e)
        Nav.dconn(d,f)
        Nav.dconn(d,g)

        Nav.dconn(e,l)

        Nav.dconn(f,e)
        Nav.dconn(f,h)
        Nav.dconn(f,g1)

        Nav.dconn(g,g1)
        
        Nav.dconn(h,i)
        
        Nav.dconn(i,j)
        Nav.dconn(i,k)

        Nav.dconn(j,m)

        Nav.dconn(k,l)
        Nav.dconn(k,m)
        Nav.dconn(k,o)

        Nav.dconn(l,o)
        Nav.dconn(l,r)

        Nav.dconn(m,n)
        Nav.dconn(m,r)

        Nav.dconn(n,q)

        Nav.dconn(o,p)
        Nav.dconn(o,r)
        Nav.dconn(o,s)

        Nav.dconn(p,r)
        Nav.dconn(p,q)
        Nav.dconn(p,aa)
        
        Nav.dconn(q,r)

        Nav.dconn(s,t)

        Nav.dconn(t,v)

        Nav.dconn(u,x)
        Nav.dconn(u,ag)

        Nav.dconn(v,x)
        Nav.dconn(v,y)

        Nav.dconn(y,z)
        Nav.dconn(y,ae)

        Nav.dconn(z,aa)

        Nav.dconn(aa,ab)

        Nav.dconn(ab,ac)

        Nav.dconn(ac,ad)

        Nav.dconn(ad,ae)
        Nav.dconn(ad,af)

        Nav.dconn(ag,ah)
        Nav.dconn(ag,aj)
        Nav.dconn(ag,ak)

        Nav.dconn(ah,ai)

        Nav.dconn(ai,aj)

        Nav.dconn(aj,ak)

        Nav.dconn(ak,al)

        waypoints+=[a,b,b1,c,d,e,f,g,g1,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x]
        waypoints+=[y,z,aa,ab,ac,ad,ae,af,ag,ah,ai,aj,ak,al]

        self._navigator=Navigator(waypoints)        
        
    def __init__ (self,paintLine):
        self._width=50
        self._height=50
        size = self._width * self._height
        
        
        self.level_one(paintLine)
##        self.scale(.25)

        paintLine.append(self)

        #print self.raycast(0,0,2000,2000)

    def _pos (self,x,y):
        return x + (y*self._width);
    
##    def inv_pos(self,index):
##        return (index%self._width,index/self._width)
    # return the tile at a given tile position in the level
    def tile (self,x,y):
        return self._map[self._pos(x,y)]
    
    # Does a point with graphics coordinates x and y collide with the level?
    def collide(self,graph_x,graph_y):
        for block in self._map:
            if withinBox(graph_x,graph_y,block):
                return True
        return False

    #preforms a fake raycast against stationary level objects
    #from point x1,y1 to point x2,y2
    def raycast(self,x1,y1,x2,y2):
        DIS=15
        mult=find_mult(x1,y1,x2,y2,DIS)
        for i in range(mult):
            point=scale_vector(x1,y1,x2,y2,DIS*(i+1))
            if self.collide(point[0],point[1]):
                return (point[0],point[1])
        if self.collide(x2,y2):
                return (x2,y2)
        return None

    #reutrns the closest waypoint to a point
    #making sure a straight line exists between the two
    def closest_waypoint(self,x,y,precision=True):
        Q=self._navigator.waypoint_distances(x,y,precision)

        while not(Q.empty()):
            dis,obj=Q.get()
            test=self.raycast(x,y,obj._x,obj._y)
            # if straight line
            if test==None:
                return obj
            
        #This will make things expload
        return None
                
    

    def on_draw(self):
        for block in self._map:
                block.on_draw()
        self._navigator.on_draw()
