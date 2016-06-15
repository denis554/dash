import datetime
import time
import random

from dash.react import Dash
from dash.components import div, p, InputControl

dash = Dash(__name__)

dash.layout = div([
    p('basic <p> component'),
    div([
        div('B, C, D, depend on A'),
        div('E depends on B and C'),
        div('F depends on A and D')
    ], style=dict(fontSize=14)),

    InputControl(placeholder='A', id='A'),
    InputControl(placeholder='B', id='B'),
    InputControl(placeholder='C', id='C'),
    InputControl(placeholder='D', id='D'),
    InputControl(placeholder='E', id='E'),
    InputControl(placeholder='F', id='F')

])


def update_component(*components):
    time.sleep(random.random() * 5)
    return {
        'value': str(datetime.datetime.now().second)
    }


dash.react('B', ['A'])(update_component)
dash.react('C', ['A'])(update_component)
dash.react('D', ['A'])(update_component)
dash.react('E', ['B', 'C'])(update_component)
dash.react('F', ['A', 'D'])(update_component)


if __name__ == '__main__':
    dash.server.run(port=8050, debug=True)
