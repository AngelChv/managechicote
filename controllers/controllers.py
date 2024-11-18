# -*- coding: utf-8 -*-
# from odoo import http


# class Managechicote(http.Controller):
#     @http.route('/managechicote/managechicote', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/managechicote/managechicote/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('managechicote.listing', {
#             'root': '/managechicote/managechicote',
#             'objects': http.request.env['managechicote.managechicote'].search([]),
#         })

#     @http.route('/managechicote/managechicote/objects/<model("managechicote.managechicote"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('managechicote.object', {
#             'object': obj
#         })
