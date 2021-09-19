import config as cfg
from data_fetcher import city_details
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

colors = cfg.colors

class BuildPage:
        
    def get_page_heading_style(self):
        return {'backgroundColor': colors['background']}


    def get_page_heading_title(self):
        return html.H1(children='City Finder',
                                            style={
                                            'textAlign': 'center',
                                            'color': colors['text']
                                        })

    def get_page_heading_subtitle(self):
        return html.Div(children='Find city based on initial letters',
                                             style={
                                                 'textAlign':'center',
                                                 'color':colors['text']
                                             })

    def generate_page_header(self):
        main_header =  dbc.Row(
                                [
                                    dbc.Col(self.get_page_heading_title(),md=12)
                                ],
                                align="center",
                                style=self.get_page_heading_style()
                            )
        subtitle_header = dbc.Row(
                                [
                                    dbc.Col(self.get_page_heading_subtitle(),md=12)
                                ],
                                align="center",
                                style=self.get_page_heading_style()
                            )
        header = (main_header,subtitle_header)
        return header

    def generate_card_content(self,card_header,card_value):
        card_head_style = {'textAlign':'center','fontSize':'150%'}
        card_body_style = {'textAlign':'center','fontSize':'200%'}
        card_header = dbc.CardHeader(card_header,style=card_head_style)
        card_body = dbc.CardBody(
            [
                html.H5(card_value, className="card-title",style=card_body_style),
            ]
        )
        card = [card_header,card_body]
        return card

    def generate_card(self,input_value1='y'):
        if len(input_value1) == 0 :
            length = 'Provide initial'
            name_str = 'Provide initial'
        else :
            out = city_details(input_value1)
            names = out[0]
            name_str = ' ,'.join(names)
            length = out[1]
            if length==0:
                name_str='No city found'
        card = html.Div(
            [
                dbc.Row(
                    [
                        dbc.Col(dbc.Card(self.generate_card_content("City Starting with letter",length), color="success", inverse=True),md=dict(size=2,offset=3)),
                        dbc.Col(dbc.Card(self.generate_card_content("City names", name_str), color="warning", inverse=True),md=dict(size=2))
                    ],
                ),
            ],id='card1'
        )
        return card

    def generate_input(self,id):
        return html.Div([
                            html.Label('Enter initials of city:  '),
                            dcc.Input(id='my-id'+str(id),
                                type='text',
                                value=''
                            ),
                            html.Button('Submit', id='button')
            ])               

    def generate_layout(self):
        page_header = self.generate_page_header()
        layout = dbc.Container(
            [
                page_header[0],
                page_header[1],
                html.Hr(),
                dbc.Row(
                    [
                        dbc.Col(self.generate_input(id=1),md=dict(size=4,offset=3))                    
                    ]
                
                ),
                self.generate_card(),
                html.Hr(),
            ],fluid=True,style={'backgroundColor': colors['bodyColor']}
        )
        return layout