import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
import plotly.io as io
from dash.dependencies import Input, Output
from datetime import datetime

from CovidMap import CovidMap
from data.CreateNewCsv import CreateNewCsv
from graphs.TopTen import TopTen

# def something()
import time

app = dash.Dash(__name__)

covid_mapp = CreateNewCsv().get_covid_csv

covid_mapp["Date"] = CreateNewCsv().get_covid_csv["Date"].replace(',', '', regex=True)
covid_mapp["Date"] = pd.to_datetime(covid_mapp["Date"], format='%b %d %Y').dt.date
covid_mapp["date"] = covid_mapp['Date'].astype(str).str.replace('/', ' ')

covid_map = covid_mapp.sort_values(by=['Date']).reset_index()


# covid_map['Date'] = covid_map['Date'].astype("|S")

# def new_example():
#     year = 1960
#     scl = [[0.0, '#ffffff'], [0.2, '#ff9999'], [0.4, '#ff4d4d'],
#            [0.6, '#ff1a1a'], [0.8, '#cc0000'], [1.0, '#4d0000']]  # reds
#
#     data_slider = []
#     for col in covid_map.columns:
#         covid_map[col] = covid_map[col].astype(str)
#
#     data = [dict(
#         type='choropleth',  # type of map-plot
#         colorscale=scl,
#         autocolorscale=False,
#         locations=covid_map['Code'],  # the column with the state
#         z=covid_map['deaths'].astype(float),  # the variable I want to color-code
#         marker=dict(  # for the lines separating states
#             line=dict(
#                 color='rgb(255,255,255)',
#                 width=2)),
#         colorbar=dict(
#             title="Murder rate per 100,000 people")
#     )]
#     data_one_year = dict(
#         type='choropleth',
#         locations=covid_map['Code'],
#         z=covid_map['deaths'].astype(float),
#         colorscale=scl,
#     )
#
#     data_slider.append(data_one_year)
#     steps = []
#
#     for i in range(len(data_slider)):
#         step = dict(method='restyle',
#                     args=['visible', [False] * len(data_slider)],
#                     label='Year {}')  # label to be displayed for each step (year)
#         step['args'][1][i] = True
#         steps.append(step)
#
#     sliders = [dict(active=0, pad={"t": 1}, steps=steps)]
#
#     layout = dict(
#         title=year,
#         sliders=sliders
#     )
#
#     fig = dict(data=data_slider, layout=layout)
#
#     return fig


# print(covid_map)


# def covid_slider_map() :


def return_data():
    ranges = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 1, 2, 3, 4, 5, 10, 35]
    df_sub = TopTen().min_top_ten()
    trace = go.Bar(x=df_sub['Area'], y=ranges)
    data = [trace]
    return data


#
def test():
    y1 = TopTen().get_by_year['Value']

    trace0 = go.Box(
        y=y1,
        name="All countries"
    )
    data = [trace0]
    return data


def boxplot_two():
    bool = TopTen().get_by_year['Area'] != 'Singapore'
    y0 = TopTen().get_by_year[bool]['Value']
    trace1 = go.Box(
        y=y0,
        name="Without Singapore"
    )
    data = [trace1]
    return data


def boxplot_three():
    bool = (TopTen().get_by_year['Area'] != 'Singapore') & (TopTen().get_by_year['Area'] != 'Brunei Darussalam')
    y2 = TopTen().get_by_year[bool]['Value']
    trace2 = go.Box(
        y=y2,
        name="Without Singapore and Brunei Darussalam"
    )
    data = [trace2]
    return data


def slider_steps():
    tes = covid_map.Date.nunique()
    return tes


def slider_marks():
    return ''


# def transform_value(value):
#     return 10 ** value
#
#
# print(slider_steps())

app.layout = html.Div([
    html.Div([
        html.Div([html.H4('Livestock production and disease outbreaks')], className='row center-text xpadding'),
        html.Div([
            html.P('Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. '
                   'Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus '
                   'mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa '
                   'quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, '
                   'rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. '
                   'Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. '
                   'Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, '
                   'dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet. '
                   'Quisque rutrum. Aenean imperdiet. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies '
                   'nisi. Nam eget dui.')
        ], className='container center-text')
    ], className='row'),
    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    html.P('Top ten per country, calculated with lsu/ha - (livestock units per hectare)'),
                    html.Div(dcc.RadioItems(id='checklist',
                                            options=[
                                                {'label': 'With Singapore', 'value': 'Met'},
                                                {'label': 'Without Singapore', 'value': 'Zonder'},
                                                {'label': 'Without Singapore & Brunei Darussalam',
                                                 'value': 'Zonderbrunai'}
                                            ],
                                            value='Met',
                                            labelStyle={'display': 'inline-block'}
                                            )
                             ),
                ], className='row'),
            ], className='six columns'),
            html.Div([
                html.P('Lowest ten countries, calculated with lsu/ha - (livestock units per hectare)'),
            ], className='six columns'),
        ], className='row center-text'),
        html.Div([
            html.Div([
                html.Div(dcc.Graph(id="bar_chart",
                                   config={'displayModeBar': False}
                                   )
                         ),
            ], className='six columns'),
            html.Div([html.Div([
                html.Div(dcc.Graph(id="",
                                   figure={'data': return_data()},
                                   config={'displayModeBar': False}
                                   )
                         )
            ])

            ], className='six columns'),
        ], className='row'),
    ], className='row'),
    html.Div([
        html.Div([
            html.P('test'),
            html.Div([dcc.RadioItems(
                id='worldmap-checklist',
                options=[
                    {'label': 'With Singapore', 'value': 'Met'},
                    {'label': 'Without Singapore', 'value': 'Zonder'},
                    {'label': 'Without Singapore & Brunei Darussalam', 'value': 'Zonderbrunai'}
                ],
                value='Zonderbrunai',
                labelStyle={'display': 'inline-block'}
            )]),
        ], className='row center-text'),
        html.Div([
            dcc.Graph(id='worldmap', config={'displayModeBar': False})
        ], className='worldmap'),
    ], className='row'),
    html.Div([
        html.Div([
            html.P('As you can see below ')
        ], className='container justify')
    ], className='row'),
    html.Div([
        html.Div([
            html.Div([
                html.P('test'),
            ], className='four columns justify'),
            html.Div([
                html.P('test'),
            ], className='four columns justify'),
            html.Div([
                html.P('test'),
            ], className='four columns justify'),
        ], className='row'),
        html.Div([
            html.Div([
                dcc.Graph(figure={'data': test()}, id='box-plot-1', config={'displayModeBar': False})
            ], className='four columns'),
            html.Div([
                dcc.Graph(figure={'data': boxplot_two()}, id='box-plot-2', config={'displayModeBar': False})
            ], className='four columns'),
            html.Div([
                dcc.Graph(figure={'data': boxplot_three()}, id='box-plot-3', config={'displayModeBar': False})
            ], className='four columns')

        ], className='row')
    ]),
    html.Div([
        html.Div([
            html.P('Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. '
                   'Aenean massa.')
        ], className='container justify center-text')
    ], className='row'),
    html.Div([
        html.Div([
            html.Div([
                dcc.Graph(id='worldmap_covid', config={'displayModeBar': False})
            ], className='worldmap_covid'),
            dcc.Slider(
                id='year-month-slider',
                min=0,
                max=len(covid_map['Date'].unique())-1,
                step=1,
                value=0,
                marks={i: yearm for i, yearm in enumerate(covid_map['Date'].unique())}
            ),
            html.Div(id='slider-output-container')
        ]),
    ], className='row')
], className="container")


@app.callback(
    [dash.dependencies.Output('worldmap_covid', 'figure'), dash.dependencies.Output('year-month-slider', 'children')],
    [dash.dependencies.Input('year-month-slider', 'value')],
    [dash.dependencies.State('year-month-slider', 'marks')])
def update_figure(selected_year_month_key, marks):
    scl = [[0.0, '#ffbe0b'], [0.2, '#fb5607'], [0.4, '#ff006e'], \
           [0.6, '#8338ec'], [0.8, '#3a86ff'], [1.0, '#03045e']]
    # print(selected_year_month_key)
    selected_year_month = marks[str(selected_year_month_key)]  # use the selected marker to get date
    # filtered_df = covid_map[covid_map.Date == selected_year_month]
    # print(covid_map['Date'])
    covid_map['Date'] = covid_map['Date'].astype(str).str.replace('/', ' ')
    # print(covid_map['Date'])
    b = covid_map['Date'] == selected_year_month
    test = covid_map[b]
    print(test.info())

    trace3 = []

    trace3.append(go.Choropleth(
        locations=test['Alpha-3_y'],
        z=test['deaths'],
        colorscale=scl,
        autocolorscale=False,
    ))
    layout = go.Layout(
        autosize=False,
        width=1000,
        height=500,
        margin=dict(l=20, r=20, t=20, b=20)
    )
    figure = {
        'data': trace3,
        'layout': layout
    }
    return [figure, 'You have selected "{}"'.format(selected_year_month)]
    # return 'You have selected "{}"'.format(selected_year_month)


@app.callback(
    dash.dependencies.Output('worldmap', 'figure'),
    [dash.dependencies.Input('worldmap-checklist', 'value')])
def update_worldmap(value):
    scl = [[0.0, '#ffbe0b'], [0.2, '#fb5607'], [0.4, '#ff006e'], \
           [0.6, '#8338ec'], [0.8, '#3a86ff'], [1.0, '#03045e']]
    trace1 = []
    df = TopTen().get_by_year

    if value == 'Met':
        test = df
    if value == 'Zonder':
        s = df['Area'] != 'Singapore'
        test = df[s]
    if value == 'Zonderbrunai':
        s = (df['Area'] != 'Singapore') & (df['Area'] != 'Brunei Darussalam')
        test = df[s]

    trace1.append(go.Choropleth(
        locations=test['Alpha-3'],
        z=test['Value'],
        colorscale=scl,
        autocolorscale=False,
    ))
    layout = go.Layout(
        autosize=False,
        width=1000,
        height=500,
        margin=dict(l=20, r=20, t=20, b=20)
    )
    figure = {
        'data': trace1,
        'layout': layout
    }

    return figure


@app.callback(
    dash.dependencies.Output('bar_chart', 'figure'),
    [dash.dependencies.Input('checklist', 'value')])
def update_output(value):
    trace1 = []
    if value == 'Met':
        test = TopTen().top_ten_bool()
    if value == 'Zonder':
        test = TopTen().top_eleven_bool()
    if value == 'Zonderbrunai':
        test = TopTen().top_without_both()

    df_sub = TopTen().df_get_top_eleven()
    trace1.append(go.Bar(x=df_sub[test]['Area'],
                         y=df_sub[test]['Value']), )
    layout = go.Layout(
        xaxis={'title': value},
        yaxis={'title': value},
    )

    fig = {'data': trace1,
           'layout': layout
           }

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
