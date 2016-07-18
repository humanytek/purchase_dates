from openerp import api, fields, models, _
from openerp.exceptions import ValidationError


class PurchaseDates(models.Model):
    _inherit = 'purchase.order'

    start_date = fields.Date()
    final_date = fields.Date()

    @api.one
    @api.constrains('start_date', 'final_date')
    def _check_dates(self):
        if self.start_date > self.final_date:
            raise ValidationError(_("The start date cannot be greater than final date"))
