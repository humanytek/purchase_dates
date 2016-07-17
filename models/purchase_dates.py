from openerp import api, fields, models


class PurchaseDates(models.Model):
    _inherit = 'purchase.order'

    start_date = fields.Date()
    final_date = fields.Date()
