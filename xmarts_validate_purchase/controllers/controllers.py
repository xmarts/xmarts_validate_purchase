# -*- coding: utf-8 -*-
from odoo import http

# class Belenes(http.Controller):
#     @http.route('/belenes/belenes/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/belenes/belenes/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('belenes.listing', {
#             'root': '/belenes/belenes',
#             'objects': http.request.env['belenes.belenes'].search([]),
#         })

#     @http.route('/belenes/belenes/objects/<model("belenes.belenes"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('belenes.object', {
#             'object': obj
#         })