import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd
from matplotlib.widgets import Button 
from matplotlib.widgets import TextBox
from datetime import datetime

import Plot as Plot

# Generate the plot
x_value = np.linspace(-3000, 1500, 750)
periodic_function = Plot.Plot(x_value, 3 * np.pi * np.exp(-(lambda t: 5* np.sin(2 * np.pi * 1 * t))(x_value)))
fig, ax = plt.subplots() 
p, = periodic_function.draw('black')

plt.subplots_adjust(left = 0.1, bottom = 0.3) 
ax.title.set_text('Untitled experiment')

# Set title button 
def submit(expression):
    ax.title.set_text(expression)

ax_box = fig.add_axes([0.2, 0.02, 0.4, 0.050])
text_box = TextBox(ax_box, 'Enter experiment name', textalignment= "center")
text_box.on_submit(submit)

# CSV button 
ax_csv_btn = plt.axes([0.7, 0.02, 0.2, 0.050]) 
btn2 = Button( 
ax_csv_btn, label="Save as csv", color='green', hovercolor='lightgreen') 

def create_csv_file(event): 
    data_points = pd.DataFrame(p.get_data())
    date_of_export = {
    '' : ['Date of export ' + datetime.now().strftime("%d/%m/%Y %H:%M:%S")]
    }
    experiment_name = {
    '' : ['Name of experiment ' + ax.get_title('center')]
    }
    export_date_data_points = pd.DataFrame(date_of_export)
    experiment_name_data_points = pd.DataFrame(experiment_name)
    merged_data = pd.concat([data_points, export_date_data_points, experiment_name_data_points], ignore_index = True)
    merged_data.reset_index()
    merged_data.to_csv('data.csv', index = False)
            
btn2.on_clicked(create_csv_file) 

ax.grid()
plt.show()
