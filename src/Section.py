# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:47:50 2017

@author: lfoul
"""
import OpenGL.GL as gl

class Section:
    # Constructor
    def __init__(self, parameters = {}) :  
        # Parameters
        # position: position of the wall 
        # width: width of the wall - mandatory
        # height: height of the wall - mandatory
        # thickness: thickness of the wall
        # color: color of the wall        

        # Sets the parameters
        self.parameters = parameters
        
        # Sets the default parameters
        if 'position' not in self.parameters:
            self.parameters['position'] = [0, 0, 0]        
        if 'width' not in self.parameters:
            raise Exception('Parameter "width" required.')   
        if 'height' not in self.parameters:
            raise Exception('Parameter "height" required.')   
        if 'orientation' not in self.parameters:
            self.parameters['orientation'] = 0              
        if 'thickness' not in self.parameters:
            self.parameters['thickness'] = 0.2    
        if 'color' not in self.parameters:
            self.parameters['color'] = [0.5, 0.5, 0.5]       
        if 'edges' not in self.parameters:
            self.parameters['edges'] = False             
            
        # Objects list
        self.objects = []

        # Generates the wall from parameters
        self.generate()   
        
    # Getter
    def getParameter(self, parameterKey):
        return self.parameters[parameterKey]
    
    # Setter
    def setParameter(self, parameterKey, parameterValue):
        self.parameters[parameterKey] = parameterValue
        return self     

    # Defines the vertices and faces 
    def generate(self):
        self.vertices = [   # Définir ici les sommets
                [0,0,0],
                [self.parameters['width'],0,0],
                [self.parameters['width'],0,self.parameters['height']],
                [0,0,self.parameters['height']], 
                [0,self.parameters['thickness'],self.parameters['height']],
                [self.parameters['width'],self.parameters['thickness'],self.parameters['height']],      
				[self.parameters['width'],self.parameters['thickness'],0],
                [0,self.parameters['thickness'],0]
                ]
        self.faces = [      # définir ici les faces
                [0,1,2,3],
                [1,6,5,2],
                [6,7,4,5],
                [7,0,3,4],
                [0,1,6,7],
                [3,2,5,4]
                ]   

    # Checks if the opening can be created for the object x
    def canCreateOpening(self, x):
        # A compléter en remplaçant pass par votre code
        return (self.parameters["width"] >= x.parameters["width"] 
                and self.parameters["height"] >= x.parameters["height"] 
                and self.parameters["position"][1] == x.parameters["position"][1] 
                and self.parameters["position"][0] <= x.parameters["position"][0] 
                and self.parameters["position"][0] + self.parameters["width"]>= x.parameters["position"][0]
                + x.parameters["width"] and self.parameters["position"][2] <= x.parameters["position"][2] 
                and self.parameters["position"][2] + 
                self.parameters["height"]>= x.parameters["position"][2]+ x.parameters["height"])      
        
    # Creates the new sections for the object x
    def createNewSections(self, x):
        # A compléter en remplaçant pass par votre code
        position=self.parameters['position']
        width=self.parameters['width']
        height=self.parameters['height']
        thickness=self.parameters['thickness']
        orientation=self.parameters['orientation']
        edges=self.parameters['color']
        color=self.parameters['color']
        sections=[]
        if self.canCreateOpening(x):
          if x.getParameter('position')[0]>position[0]:
            sect1= Section({'position': position,
            'width': x.getParameter('position')[0]-position[0],
            'height': height,
            'thickness': thickness})  
            sections.append(sect1)
          
          if (x.getParameter('position')[2] + x.getParameter('height')!=height+position[2]):
            
              sect2=Section({
              'position': [x.getParameter('position')[0], position[1],x.getParameter('position')[2]
              +x.getParameter('height')],
              'width': x.getParameter('width'),
              'height': position[2]+height - (x.getParameter('position')[2]+x.getParameter('height')),
              'thickness': thickness,
              'orientation': orientation,
              'edges':edges,
              'color': color})
              sections.append(sect2)
                  
          if (x.getParameter('position')[2]>position[2]):
            sect3=Section({
            'position': [x.getParameter('position')[0], position[1],position[2]],
            'width': x.getParameter('width'),
            'height': x.getParameter('position')[2]-position[2],
            'thickness': thickness,
            'orientation': orientation,
            'edges':edges,
            'color': color})
            sections.append(sect3)
          
          if (width+position[0]>(x.getParameter('position')[0]+x.getParameter('width'))):
            sect4= Section({
            'position': [x.getParameter('position')[0]+x.getParameter('width'), position[1],position[2]],
            'width': position[0]+width-(x.getParameter('position')[0]+x.getParameter('width')),
            'height': height,
            'thickness': thickness,
            'orientation': orientation,
            'edges':edges,
            'color': color})
            sections.append(sect4)
          
        return sections              
        
    # Draws the edges
    def drawEdges(self):
        # A compléter en remplaçant pass par votre code
        gl.glPushMatrix()
        gl.glPolygonMode(gl.GL_FRONT_AND_BACK,gl.GL_LINE)
        gl.glTranslatef(self.parameters['position'][0],self.parameters['position'][1],self.parameters['position'][2])
        gl.glBegin(gl.GL_QUADS)
        gl.glColor3fv([0,0,0])
        for i in self.faces :
            gl.glVertex3fv(self.vertices[i[0]])
            gl.glVertex3fv(self.vertices[i[1]])
            gl.glVertex3fv(self.vertices[i[2]])
            gl.glVertex3fv(self.vertices[i[3]])
        gl.glEnd()
        gl.glPopMatrix()
                    
    # Draws the faces
    def draw(self):
        # A compléter en remplaçant pass par votre code
        if self.parameters['edges']:
            self.drawEdges()
        gl.glPushMatrix()
        gl.glPolygonMode(gl.GL_FRONT_AND_BACK,gl.GL_FILL)
        gl.glTranslatef(self.parameters['position'][0],self.parameters['position'][1],self.parameters['position'][2])
        gl.glBegin(gl.GL_QUADS)
        gl.glColor3fv([0.5,0.5,0.5])
        for i in self.faces :
            gl.glVertex3fv(self.vertices[i[0]])
            gl.glVertex3fv(self.vertices[i[1]])
            gl.glVertex3fv(self.vertices[i[2]])
            gl.glVertex3fv(self.vertices[i[3]])
        gl.glEnd()
        gl.glPopMatrix()

