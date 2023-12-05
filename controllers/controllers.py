# -*- coding: utf-8 -*-
from odoo import http


class CwcWeb(http.Controller):
    @http.route('/', auth='public', type='http', website=True)
    def home(self, **kw):
        return http.request.render('cwc_web.home')

    @http.route('/aboutus', auth='public', type='http', website=True)
    def about(self, **kw):
        return http.request.render('cwc_web.about')

    @http.route('/contactus', auth='public', type='http', website=True)
    def contact(self, **kw):
        return http.request.render('cwc_web.contactus')

    @http.route('/directory', auth='public', type='http', website=True)
    def directory(self, **kw):
        return http.request.render('cwc_web.directory')

    @http.route('/resources', auth='public', type='http', website=True)
    def resources(self, **kw):
        return http.request.render('cwc_web.resources')

    @http.route('/join-our-team', auth='public', type='http', website=True)
    def join(self, **kw):
        return http.request.render('cwc_web.join-our-team')

    @http.route('/get-help', auth='public', type='http', website=True)
    def help(self, **kw):
        return http.request.render('cwc_web.get-help')

#     @http.route('/cwc_web/cwc_web/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('cwc_web.listing', {
#             'root': '/cwc_web/cwc_web',
#             'objects': http.request.env['cwc_web.cwc_web'].search([]),
#         })

#     @http.route('/cwc_web/cwc_web/objects/<model("cwc_web.cwc_web"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cwc_web.object', {
#             'object': obj
#         })
