from odoo import models, fields, api, exceptions

class StockLocation(models.Model):
    _inherit = 'stock.location'
    _description= 'this is stock location'
    lokasi_buku = fields.Boolean('Lokasi Buku ?')