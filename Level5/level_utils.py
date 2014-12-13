import math
#is a point within a box?
def withinBox(x,y,block):
    return (x>block._x and x<block._x+block._width) and (y>block._y and y<block._y+block._height)

#takes a line segment and returns a point length factor away
#from first point given, in same direction as segment. 
def scale_vector(x1,y1,x2,y2,factor):
    #translate vector to origin
    trans=(x2-x1,y2-y1)
    
    # find length
    length=math.sqrt((x2-x1)**2+(y2-y1)**2)
    
    # normalize
    norm=(trans[0]/length,trans[1]/length)

    #scale by amount
    scale=(norm[0]*factor,norm[1]*factor)
    
    #translate back
    final=(scale[0]+x1,scale[1]+y1)
    return final
#finds how many factor length segments can fit in the given line segment 
def find_mult(x1,y1,x2,y2,factor):
    length=math.sqrt((x2-x1)**2+(y2-y1)**2)
    return int(length/factor)
        
        
