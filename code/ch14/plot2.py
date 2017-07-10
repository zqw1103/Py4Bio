from bokeh.plotting import figure, output_file, show

x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [.7, 1.4, 2.1, 3, 3.85, 4.55, 5.8, 6.45]
z = [.5, 1.1, 1.9, 2.5, 3.1, 3.9, 4.85, 5.2]

p = figure(title='Mean wt increased vs. time',
           x_axis_label='Time in days',
           y_axis_label='% Mean WT increased')
p.circle(x, y, legend='Subject 1', size=10)
p.circle(x, z, legend='Subject 2', size=10, line_color='red',
         fill_color='white')
p.legend.location = 'top_left'
output_file('test.html')
show(p)
