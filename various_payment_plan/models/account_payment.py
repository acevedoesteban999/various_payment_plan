from odoo import fields, models

class VppAccountPyment(models.Model):
    _inherit = 'account.payment'

    is_various_payment = fields.Boolean(string='Is Various Payment', default=False)
    payment_reason_id = fields.Many2one('payment.reason', string='Payment Reason')