import pandas as pd
import plotly.express as px

file_name = input('Enter the name of your csv file along with the extension (the file needs to be in this folder as well): ')
independent = input('Enter the name of the independent variable name in your csv file verbatim: ')
dependent = input('Enter the name of the dependent variable name in your csv file verbatim: ')
control = input('Enter the name of the controlling variable name in your csv file verbatim: ')
title_of_graph = input('Enter the name of the title of your graph: ')
type_of_graph = input('What kinds of a graph are you looking for: ').lower()

df = pd.read_csv(file_name)

if type_of_graph == 'line':
    fig = px.line(df, x=independent, y=dependent, color=control, title=title_of_graph)
    fig.show()
elif type_of_graph == 'bar':
    fig = px.bar(df, x=independent, y=dependent, color=control, title=title_of_graph)
    fig.show()
else:
    print('Please choose from line and bar')

