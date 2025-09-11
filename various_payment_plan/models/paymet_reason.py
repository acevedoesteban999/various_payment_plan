from odoo import fields,models,api


class PaymentReason(models.Model):
    _name = 'payment.reason'
    _description = 'Payment Reason'

    active = fields.Boolean(string='Active', default=True)
    name = fields.Char(string='Name', required=True)
    account_id = fields.Many2one(
                    'account.account', 
                    string='Account', 
                    required=True,
                    help="""Account to use for this payment reason.
                        Changing this option does not edit existing accounting entries, 
                        it only acts on new ones."""
                    )
    company_id = fields.Many2one('res.company', string='Company', required=True, default=lambda self: self.env.company)

