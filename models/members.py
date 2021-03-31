
from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'
 
    penulis = fields.Boolean('Penulis ?')
    anggota = fields.Boolean('Anggota ?')
    penerbit = fields.Boolean('Penerbit ?')
 
    born_date = fields.Date('Date of Birth')
    death_date = fields.Date('Date of Death')
 
    biography = fields.Text('Biography')
    lang = fields.Selection(string='Language', selection='_get_lang')
 
 
    _sql_constraints = [('name_uniq', 'unique (name)', 'Nama harus unik !')]
 
    @api.model
    def _get_lang(self):
        return self.env['res.lang'].get_installed()