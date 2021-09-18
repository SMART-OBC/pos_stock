

from odoo import api, fields, models, _


class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.model
    def create(self, vals):
        res = super(SaleOrder, self).create(vals)
        # seq = self.env['ir.sequence'].next_by_code('project.issue')
        if res.company_id.name == 'My Company (San Francisco)':
            res.name = res.name.replace('S','SFC')
        elif res.company_id.name == 'My Company (Chicago)':
            res.name = res.name.replace('S', 'CHI')
        return res