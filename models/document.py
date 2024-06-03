from odoo import models, fields, api


class Document(models.Model):
    _name = 'ng_libre.document'
    _description = 'Document'

    title = fields.Char(string="Title", required=True)
    description = fields.Text(string='Description')
    partner_id = fields.Many2one('res.partner', string='Partner')
    user_id = fields.Many2one("res.users", string='Created by custom', default=lambda self: self.env.user)
    date = fields.Date(string="Date", required=False)
    employer_ids = fields.Many2many("hr.employee", string="Employers", required=False)
