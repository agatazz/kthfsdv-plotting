import matplotlib.pyplot as plt 

class Plot:
  
  def __init__(self, x_axix, y_axis):
    self.x_axis = x_axix
    self.y_axis = y_axis

  def draw(self, color: str):  
    return plt.plot(self.x_axis, self.y_axis, color = color) 

