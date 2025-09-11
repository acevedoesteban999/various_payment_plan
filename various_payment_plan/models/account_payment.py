from odoo import fields, models

class VppAccountPyment(models.Model):
    _inherit = 'account.payment'

    is_various_payment = fields.Boolean(
                            string='Is Various Payment', 
                            default=False,
                            help="""Indicates if the payment is a various payment.
                                    Disabling this option with a multiple payment already 
                                    assigned will have no effect on the last account in the 
                                    accounting entry..""")

    payment_reason_id = fields.Many2one('payment.reason', string='Payment Reason')

    def _set_move_id_payable_account(self):
        for pay in self.with_context(skip_account_move_synchronization=True):
            liquidity_lines, counterpart_lines, writeoff_lines = pay._seek_for_lines()
            counterpart_lines.account_id = self.payment_reason_id.account_id
            
    def create(self, vals_list):
        rec = super().create(vals_list)
        if rec.is_various_payment and rec.payment_reason_id.account_id :
            rec._set_move_id_payable_account()
        return rec
    
    def write(self, vals):
        response = super().write(vals)
        if self.is_various_payment and 'payment_reason_id' in vals:
            self._set_move_id_payable_account()
        return response