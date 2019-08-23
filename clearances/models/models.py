
from odoo import models, fields, api

class ConstructionInheritSale(models.Model):
     _inherit = 'sale.order'


class ConstructionInheritinvoice(models.Model):
     _inherit = 'account.invoice'

     types_of_work=fields.Char("نوع اﻻعمال")
     operation = fields.Char("لعملية")
     clearance = fields.Selection([
            ('Inprogress', 'جاري'),
            ('Closed', 'منتهي'),
            ('Draft', 'تحت التخطيط'),
            ('Other', 'اخري'),

        ],string='مستخلص')


class ConstructionInheritinvoice(models.Model):
     _inherit = 'purchase.order'
