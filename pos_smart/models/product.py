
from odoo import api, fields, models, _


class ProductProduct(models.Model):
    _inherit='product.product'

    show_qty_on_hand = fields.Boolean("Show qty on hand",default=False,compute="compute_rights")

    def compute_rights(self):
        self.show_qty_on_hand = self.env.user.has_group('pos_smart.group_cf')


class ProductProduct(models.Model):
    _inherit='product.template'

    show_qty_on_hand = fields.Boolean("Show qty on hand",default=False,compute="compute_rights")

    def compute_rights(self):
        self.show_qty_on_hand = self.env.user.has_group('pos_smart.group_cf')
