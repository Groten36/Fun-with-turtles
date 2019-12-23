xmax=10
xmin=-10
ymax=10
ymin=-10
rangex=xmax-xmin
rangey=ymax-ymin
def setup():
    global xscl,yscl
    size(600,600)
    xscl=width/rangex
    yscl=-height/rangey
    
        
           
def draw():
    global xscl, yscl
    background(255)
    translate(width/2,height/2)
    grid(xscl,yscl)
    graphFunction()

def graphFunction():
    i=xmin
    while i <=xmax:
        stroke(255,0,0)
        line(i*xscl,f(i)*yscl,(i+0.1)*xscl,f(i+0.1)*yscl)
        i+=0.1
    
def f(x):
    return 2*x**2+7*x-15

def grid(xscl,yscl):
    strokeWeight(1)
    stroke(0,0,255)
    for i in range(xmin,xmax+1):
        line(i*xscl,ymin*yscl,i*xscl,ymax*yscl)
    for i in range(ymin,ymax+1):
        line(xmin*xscl,i*yscl,xmax*xscl,i*yscl)
    stroke(0)
    strokeWeight(2)
    line(0,ymin*yscl,0,ymax*yscl)
    line(xmin*xscl,0,xmax*xscl,0)
    
