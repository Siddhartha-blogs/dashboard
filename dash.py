import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px

#import plotly.graph_objects as go
import plotly.graph_objs as go
import ipywidgets as ipw

from plotly.subplots import make_subplots
path='/home/siddhartha/k_means/EGSB_processed_clustered_3_std.csv'
from base64 import b64encode
import io
buffer = io.StringIO()
html_bytes = buffer.getvalue().encode()
encoded = b64encode(html_bytes).decode()
columns=['EGSB Feed Flow','Product flow', 'Recircualtion Flow', 'Upflow velocity', 'HRT',
       'pH feed', 'ph reactor', 'ph product', 'Sludge ORP',
       'Product Turbidity', 'Temperature feed', 'Temperature Reactor',
       ]
unit=['m\u00b3'+'/hr','m\u00b3'+'/hr','m\u00b3'+'/hr','m/hr','hr','','','','mV','NTU','\u00b0'+'C','\u00b0'+'C']
ranges=[[35,45],[8,12],[25,35],[4,5],[9,12],[5,10],[5,10],[5,10],
[-650,50],[0,500],[30,45],[0,100]]
def plot(path,column,unit,rang):
    df=pd.read_csv(path)
    df=df.sort_values("group")
    
    #for i in columns:
    df_1=pd.DataFrame()
    for j in range(3):
        df_=pd.DataFrame()
        name='Group'+'_'+str(j)
        df1=df[df['group']==j][column]
        df_[name]=df1
        df_1=pd.concat([df_1,df_])
    
        
        #fig = make_subplots(rows=1, cols=1)
    fig = px.box(df_1)
    fig.update_layout(xaxis_title="Groups", yaxis_title=column+' '+unit) 
    fig.update_yaxes(range=rang)
    fig.write_html(buffer)
    return fig
        
        #ig.add_box(df_1)
        #fig=go.Figure()
        #print(df_1)
        #for i,column in enumerate(df_1.columns):
            

        #    fig.append_trace(go.Box(y=df_1[df_1[column]!='NaN'],x=[i]),row=1,col=1)
        #fig = make_subplots(rows=len(columns), cols=1)
        #fig.append_trace(fig,row=1, col=1)
        #fig.update_yaxes(range=[35, 45])
        #fig = go.FigureWidget(fig)
        
                #display(ipw.HBox([fig, fig, fig]))
        #go.FigureWidget(fig)
        #fig_subplots=  HBox([fig])

    #fig.show()
    
import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

fig1=plot(path,columns[0],unit[0],ranges[0])
fig2=plot(path,columns[1],unit[1],ranges[1])
fig3=plot(path,columns[2],unit[2],ranges[2])
fig4=plot(path,columns[3],unit[3],ranges[3])
fig5=plot(path,columns[4],unit[4],ranges[4])
fig6=plot(path,columns[5],unit[5],ranges[5])
fig7=plot(path,columns[6],unit[6],ranges[6])
fig8=plot(path,columns[7],unit[7],ranges[7])
fig9=plot(path,columns[8],unit[8],ranges[8])
fig10=plot(path,columns[9],unit[9],ranges[9])
fig11=plot(path,columns[10],unit[10],ranges[10])
fig12=plot(path,columns[11],unit[11],ranges[11])

app.layout = html.Div(html.Div([
    dash.html.H1(children='Expanded Granular Sludge Bioreactor Operation',
        style={'textAlign': 'center','width': '100%', 'height': 50}),
    dcc.Graph(figure=fig1),dcc.Graph(figure=fig2),
    dcc.Graph(figure=fig3),dcc.Graph(figure=fig4),
    dcc.Graph(figure=fig5),dcc.Graph(figure=fig6),
    dcc.Graph(figure=fig7),dcc.Graph(figure=fig8),
    dcc.Graph(figure=fig9),dcc.Graph(figure=fig10),
    dcc.Graph(figure=fig11),dcc.Graph(figure=fig12),
    html.A(
        html.Button("Download as HTML"), 
        id="download",
        href="data:text/html;base64," + encoded,
        download="plotly_graph.html"
    )

]))

app.run_server(debug=True, use_reloader=False)

#print(plot(path))


