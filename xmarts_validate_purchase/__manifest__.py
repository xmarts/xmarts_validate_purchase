# -*- coding: utf-8 -*-
{
    'name': "XMARTS VALIDATE PURCHASE",

    'summary': """
        Add validation on purhase""",

    'description': """
         - Add checkbox to validate if the user authorize purchase
         - Add model Purchase Type  
         - Add field Purchase type to purchase order
         - Add confirmation to purchase order
         - Add submenu on configuration purchase menu
         - Add submenu on purchase menu
         
    """,

    'author': "XMARTS, Pablo Osorio",
    'website': "https://xmarts.com",

    'category': 'Uncategorized',
    'version': '0.2',

    'depends': ['base','purchase'],

    'data': [
        'views/views.xml',
    ],
    'demo': [
        #'demo/demo.xml',
    ],
}