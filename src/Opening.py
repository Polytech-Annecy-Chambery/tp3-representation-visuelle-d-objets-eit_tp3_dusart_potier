# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:47:50 2017

@author: lfoul
"""

import OpenGL.GL as gl

class Opening:
    # Constructor
    def __init__(self, parameters = {}) :  
        # Parameters
        # position: mandatory
        # width: mandatory
        # height: mandatory
        # thickness: mandatory
        # color: mandatory        

        # Sets the parameters
        self.parameters = parameters

        # Sets the default parameters 
        if 'position' not in self.parameters:
            raise Exception('Parameter "position" required.')       
        if 'width' not in self.parameters:
            raise Exception('Parameter "width" required.')
        if 'height' not in self.parameters:
            raise Exception('Parameter "height" required.')
        if 'thickness' not in self.parameters:
            raise Exception('Parameter "thickness" required.')    
        if 'color' not in self.parameters:
            raise Exception('Parameter "color" required.')  
            
        # Generates the opening from parameters
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
        self.vertices = [ # Définir ici les sommets
                [self.parameters['position']],
                [self.parameters['position'][0]+self.parameters['width'],self.parameters['position'][1],
                 self.parameters['position'][2]],
                [self.parameters['position'][0]+self.parameters['width'],self.parameters['position'][1],
                 self.parameters['position'][2]+self.parameters['height']],
                [self.parameters['position'][0],self.parameters['position'][1],
                 self.parameters['position'][2]+self.parameters['height']],
                [self.parameters['position'][0],self.parameters['position'][1]+self.parameters['thickness'],
                 self.parameters['position'][2]+self.parameters['height']],
                [self.parameters['position'][0]+self.parameters['width'],
                 self.parameters['position'][1]+self.parameters['thickness'],
                 self.parameters['position'][2]+self.parameters['height']],
                [self.parameters['position'][0]+self.parameters['width'],
                 self.parameters['position'][1]+self.parameters['thickness'],self.parameters['position'][2]],
                [self.parameters['position'][0],self.parameters['position'][1]+self.parameters['thickness'],
                 self.parameters['position'][2]]
                ]
        self.faces = [  # définir ici les faces
                [1,6,5,2],
                [7,0,3,4],
                [0,1,6,7],
                [3,3,5,4]
                ]   
        
    # Draws the faces                
    def draw(self):        
        # A compléter en remplaçant pass par votre code
        gl.glPushMatrix()
        gl.glTranslatef(self.parameters['position'][0],self.parameters['position'][1],self.parameters['position'][2])
        gl.glPolygonMode(gl.GL_FRONT_AND_BACK,gl.GL_FILL)
        gl.glBegin(gl.GL_QUADS)
        gl.glColor3fv([0.5,0.5,0.5])
        for i in self.faces :
            gl.glVertex3fv(self.vertices[i[0]])
            gl.glVertex3fv(self.vertices[i[1]])
            gl.glVertex3fv(self.vertices[i[2]])
            gl.glVertex3fv(self.vertices[i[3]])
        gl.glEnd()
        gl.glPopMatrix()
