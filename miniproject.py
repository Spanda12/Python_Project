import plotly.express as px
import pandas as pd
import text2emotion as te
import dash
from dash import dcc
from dash import html
from dash.dependencies import Output,Input,State
import dash_bootstrap_components as dbc
# import nltk
# nltk.download('omw-1.4')


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SKETCHY])

app.layout = html.Div([
                        html.H1(children="Text Emotion Analyzer",style={"marginLeft": "38%"}),
                        html.Div(children="Enter text and press submit button to see emotion analysis", className='form-label mt-4',style={"marginLeft": "40%"}),
                        dcc.Textarea(id='text_input',placeholder='Enter text here',className='form-control',style={"marginLeft": "40%",'width':"20%"}),
                        html.Br(),
                        dbc.Button("Submit", id='submit-button',className="btn btn-lg btn-primary", style={"marginLeft": "47%"}),
                        html.Br(),
                        dcc.Loading(
                            html.Div([
                            dcc.Graph(id='graph_output',style={"margin-top": "2%"})
                        ]), type="graph"
                        )
                ])


@app.callback(Output('graph_output','figure'),
              Input('submit-button', 'n_clicks'),
              State('text_input', 'value')
              )
def update_output(clicks, input_value):
    print("triggerd")
    if clicks is not None:
        print(input_value)
        text = input_value
        out_dict = te.get_emotion(text)
        labels = out_dict.keys()
        values = out_dict.values()
        df = pd.DataFrame(dict(
            r=values,
            theta=labels))
        fig = px.line_polar(df, r='r', theta='theta', line_close=True)
        fig.update_traces(fill='toself')
        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 1]
                )),
            showlegend=False)

        return fig
    else:
        return dash.no_update


if __name__ == '__main__':
    app.run_server(debug=True)