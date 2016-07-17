from openerp import api, fields, models


class PurchaseDates(models.Model):
    _inherit = 'purchase.order'

    start_date = fields.Date()
    final_date = fields.Date()

    @api.one
    @api.constrains('start_date', 'final_date')
    def _check_dates(self):
        if self.start_date > self.final_date:
            raise ValidationError("The start date cannot be greater than final date")
