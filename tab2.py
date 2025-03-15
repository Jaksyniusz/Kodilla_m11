import dash as dcc
import dash as html
import plotly as go

def render_tab(df):

    grouped = df[df['total_amt']>0].groupby('prod_cat')['total_amt'].sum()
    fig = go.Figure(data=[go.Pie(labels=grouped.index,values=grouped.values)],layout=go.Layout(title='Udział grup produktów w sprzedaży'))

layout = html.Div([html.H1(),
            html.Div([html.Div([dcc.Graph(),
                        html.Div([dcc.Dropdown(),dcc.Graph()]),
                    html.Div(id='temp-out')
                        ])

html.H1('Produkty',style={'text-align':'center'})

[dcc.Graph(id='pie-prod-cat',figure=fig)],style={'width':'50%'}),
html.Div([html.Div([dcc.Graph(id='pie-prod-cat',figure=fig)],
                        style={'width':'50%'}),
            html.Div([dcc.Dropdown(),dcc.Graph()],
            style={'width':'50%'})],style={'display':'flex'})

dcc.Dropdown(id='prod_dropdown',
        options=[],
        value=df['prod_cat'].unique()[0])

options=[{'label':prod_cat,'value':prod_cat} for prod_cat in df['prod_cat'].unique()],
dcc.Graph(id='barh-prod-subcat')

def render_tab(df):

    grouped = df[df['total_amt']>0].groupby('prod_cat')['total_amt'].sum()
    fig = go.Figure(data=[go.Pie(labels=grouped.index,values=grouped.values)],layout=go.Layout(title='Udział grup produktów w sprzedaży'))

    layout = html.Div([html.H1('Produkty',style={'text-align':'center'}),

                        html.Div([html.Div([dcc.Graph(id='pie-prod-cat',figure=fig)],style={'width':'50%'}),
                        html.Div([dcc.Dropdown(id='prod_dropdown',
                                    options=[{'label':prod_cat,'value':prod_cat} for prod_cat in df['prod_cat'].unique()],
                                    value=df['prod_cat'].unique()[0]),
                                    dcc.Graph(id='barh-prod-subcat')],style={'width':'50%'})],style={'display':'flex'}),
                                    html.Div(id='temp-out')
                        ])

    return layout
