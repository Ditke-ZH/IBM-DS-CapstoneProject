# Import required libraries
import pandas as pd
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read the airline data into pandas dataframe
spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# Create a dash application
app = dash.Dash(__name__)

# Create an app layout
app.layout = html.Div(children=[html.H1('SpaceX Launch Records Dashboard',
                                        style={'textAlign': 'center', 'color': '#503D36',
                                               'font-size': 40}),
                                # TASK 1: Add a dropdown list to enable Launch Site selection
                                # The default select value is for ALL sites
                                dcc.Dropdown(
                                    id='site-dropdown',
                                    options=[
                                        {'label': 'All Sites', 'value': 'ALL'},
                                        {'label': 'CCAFS LC-40', 'value': 'CCAFS LC-40'},
                                        {'label': 'CCAFS SLC-40', 'value': 'CCAFS SLC-40'},
                                        {'label': 'KSC LC-39A', 'value': 'KSC LC-39A'},
                                        {'label': 'VAFB SLC-4E', 'value': 'VAFB SLC-4E'}
                                    ],
                                    value='ALL',
                                    placeholder='Select a Launch Site here',
                                    searchable=True
                                ),
                                html.Br(),

                                # TASK 2: Add a pie chart to show the total successful launches count for all sites
                                # If a specific launch site was selected, show the Success vs. Failed counts for the site
                                html.Div(dcc.Graph(id='success-pie-chart')),
                                html.Br(),

                                html.P("Payload range (Kg):"),
                                # TASK 3: Add a slider to select payload range
                                #dcc.RangeSlider(id='payload-slider',...)
                                dcc.RangeSlider(
                                    id='payload-slider',
                                    min=0,
                                    max=10000,
                                    step=1000,
                                    marks={i: f'{i}' for i in range(0, 10001, 2500)},
                                    value=[min_payload, max_payload]
                                ),

                                # TASK 4: Add a scatter chart to show the correlation between payload and launch success
                                html.Div(dcc.Graph(id='success-payload-scatter-chart')),
                                ])

# TASK 2:
# Add a callback function for `site-dropdown` as input, `success-pie-chart` as output
@app.callback(
    Output(component_id='success-pie-chart', component_property='figure'),
    Input(component_id='site-dropdown', component_property='value')
)
def get_pie_chart(selected_site):
    if selected_site == 'ALL':
        # Show total successful launches per site (class = 1)
        df_success = spacex_df[spacex_df['class'] == 1]
        fig = px.pie(
            df_success,
            names='Launch Site',
            title='Total Successful Launches by Site'
        )
        return fig
    else:
        # Filter to the selected site and show success vs failure counts
        df_site = spacex_df[spacex_df['Launch Site'] == selected_site]
        outcome_counts = (
            df_site['class']
            .value_counts()
            .rename_axis('class')
            .reset_index(name='count')
        )
        outcome_counts['Outcome'] = outcome_counts['class'].map({1: 'Success', 0: 'Failed'})
        fig = px.pie(
            outcome_counts,
            values='count',
            names='Outcome',
            title=f'Total Launch Outcomes for {selected_site}'
        )
        return fig

# TASK 4:
# Add a callback function for `site-dropdown` and `payload-slider` as inputs, `success-payload-scatter-chart` as output
@app.callback(
    Output(component_id='success-payload-scatter-chart', component_property='figure'),
    [Input(component_id='site-dropdown', component_property='value'),
     Input(component_id='payload-slider', component_property='value')]
)
def update_scatter(selected_site, payload_range):
    low, high = payload_range

    # Filter by payload range first
    filtered = spacex_df[spacex_df['Payload Mass (kg)'].between(low, high)]

    # If a specific site is selected, filter by site
    if selected_site != 'ALL':
        filtered = filtered[filtered['Launch Site'] == selected_site]
        title = f'Payload vs. Outcome for {selected_site}'
    else:
        title = 'Payload vs. Outcome for All Sites'

    # Build scatter: x=payload, y=class(0/1), color by booster category
    fig = px.scatter(
        filtered,
        x='Payload Mass (kg)',
        y='class',
        color='Booster Version Category',
        title=title,
        hover_data=['Launch Site', 'class']
    )
    return fig

# Run the app
if __name__ == '__main__':
    app.run()
