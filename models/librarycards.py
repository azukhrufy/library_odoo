from odoo import models, fields, api, exceptions

class KartuPerpustakaan(models.Model):
    _name = 'kartu.perpustakaan'
    _description = 'Kartu Perpustakaan odoo'
    
    name = fields.Char('Reference', readonly=True, default='/')
    partner_id = fields.Many2one('res.partner', 'Member', required=True, domain=[('anggota', '=', True)], readonly=True, states={'draft': [('readonly', False)]})
    kartu_lines = fields.One2many('kartu.perpustakaan.line', 'kartu_id', 'Kartu Perpustakaan Line', readonly=True, states={'confirm': [('readonly', False)]})
    state = fields.Selection([('draft', 'Draft'), ('confirm', 'Confirm')], "State", default='draft', readonly=True)
    note = fields.Text('Notes')
    
    @api.multi
    def kartu_confirm(self):
        return self.write({'state': 'confirm'})
 
    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('kartu.perpustakaan')
        return super(KartuPerpustakaan, self).create(vals)
 
    @api.multi
    def unlink(self):
        if self.state != 'draft':
            raise exceptions.UserError(("Kartu pinjaman tidak bisa dihapus pada state %s !") % (self.state))
        return super(KartuPerpustakaan, self).unlink()
    
    
class KartuPerpustakaanLine(models.Model):
    _name = 'kartu.perpustakaan.line'
    _description = 'Kartu Perpustakaan Line'
    
    kartu_id = fields.Many2one('kartu.perpustakaan', 'Kartu Perpustakaan', required=True, ondelete='cascade')
    product_id = fields.Many2one('product.product', 'Books', required=True)
    state = fields.Selection([('draft', 'Draft'), ('rent', 'Rented'), ('return', 'Done')], "State", default='draft', readonly=True)
    start_date = fields.Date('Start Date', default=fields.Date.context_today)
    end_date = fields.Date('End Date', default=fields.Date.context_today)
    duration = fields.Integer('Duration (Days)', readonly=True, compute='compute_day',  store=True)
    
    partner_id = fields.Many2one('res.partner', 'Member', related="kartu_id.partner_id", store=True, readonly=True)
    nama_kartu = fields.Char(string='Card', related='kartu_id.name', readonly=True, store=True)

    @api.multi
    def unlink(self):
        if self.state != 'draft':
            raise exceptions.UserError(("Data buku pinjaman tidak bisa dihapus pada state %s !") % (self.state))
        return super(KartuPerpustakaanLine, self).unlink()
 
    @api.one
    @api.depends('start_date', 'end_date')
    def compute_day(self):
        if self.start_date and self.end_date:
            start_date = fields.Datetime.from_string(self.start_date)
            end_date = fields.Datetime.from_string(self.end_date)
            self.duration = abs((end_date - start_date).days) + 1
 
 
    @api.multi
    def pinjaman_confirm(self):
        self.product_id.state = 'rent'
        return self.write({'state': 'rent'})
 
    @api.multi
    def pinjaman_done(self):
        self.product_id.state = 'available'
        return self.write({'state': 'return'})