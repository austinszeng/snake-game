import pygame

#Takes rectangle's size, position and a point. Returns true if that
#point is inside the rectangle and false if it isnt.
def pointInRectangle(px, py, rw, rh, rx, ry):
    if px > rx and px < rx  + rw:
        if py > ry and py < ry + rh:
            return True
    return False

#Blueprint to make sliders in the game
class Slider:
    def __init__(self, position:tuple, upperValue:int, sliderWidth:int,
                 outlineSize:tuple=(300, 50))->None:
        self.position = position
        self.outlineSize = outlineSize
        self.sliderWidth = sliderWidth
        self.upperValue = upperValue
        
    #returns the current value of the slider
    def getValue(self)->float:
        # sliderWidth is the interval that each increment adds to slider
        return round(self.sliderWidth / (self.outlineSize[0] / self.upperValue), 2)

    #renders slider and the text showing the value of the slider
    def render(self, display:pygame.display, text:str)->None:
        #draw outline and slider rectangles
        pygame.draw.rect(display, (40, 40, 40), (self.position[0], self.position[1], 
                                              self.outlineSize[0], self.outlineSize[1]), 3)
        
        pygame.draw.rect(display, (40, 40, 40), (self.position[0], self.position[1], 
                                              self.sliderWidth, self.outlineSize[1]))

        #determine size of font
        self.font = pygame.font.Font('Font/LEMONMILK-Light.otf', int((15/50)*self.outlineSize[1]))

        #create text surface with value
        valueSurf = self.font.render(f"{text}: {round(self.getValue(), 2)}x", True, (255, 255, 255))
        
        #centre text
        textx = self.position[0] + (self.outlineSize[0]/2) - (valueSurf.get_rect().width/2)
        texty = self.position[1] + (self.outlineSize[1]/2) - (valueSurf.get_rect().height/2)

        display.blit(valueSurf, (textx, texty))

    #allows users to change value of the slider by dragging it.
    def changeValue(self)->None:
        #If mouse is pressed and mouse is inside the slider
        mousePos = pygame.mouse.get_pos()
        if pointInRectangle(mousePos[0], mousePos[1]
                            , self.outlineSize[0], self.outlineSize[1], self.position[0], self.position[1]):
            if pygame.mouse.get_pressed()[0]:
                #the size of the slider
                self.sliderWidth = mousePos[0] - self.position[0]

                #limit the size of the slider
                if self.sliderWidth < 1:
                    self.sliderWidth = 0
                if self.sliderWidth >= self.outlineSize[0]:
                    self.sliderWidth = self.outlineSize[0]