import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from page_builder import BuildPage
import logger 
import config as cfg

external_stylesheets = [dbc.themes.BOOTSTRAP]

if __name__ == '__main__':
    
    logger = logger.create_logger()
    page_obj = BuildPage()

    app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
    app.title = 'City Finder'

    logger.info('Building Page layout')
    try:
        app.layout = page_obj.generate_layout()
        logger.info('Page layout builded')
    except Exception as e:
        logger.error(e)
        raise e

    @app.callback(
        Output(component_id='card1',component_property='children'),
        [dash.dependencies.Input('button', 'n_clicks')],
        [dash.dependencies.State('my-id1', 'value')],
    )
    def update_output_div(input_value, input_value1):
        return page_obj.generate_card(input_value1)

    logger.info('Starting server')
    app.run_server(debug=False)

