# -*- coding: utf-8 -*-
from odoo import http

# class LibraryOdoo(http.Controller):
#     @http.route('/library_odoo/library_odoo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/library_odoo/library_odoo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('library_odoo.listing', {
#             'root': '/library_odoo/library_odoo',
#             'objects': http.request.env['library_odoo.library_odoo'].search([]),
#         })

#     @http.route('/library_odoo/library_odoo/objects/<model("library_odoo.library_odoo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('library_odoo.object', {
#             'object': obj
#         })