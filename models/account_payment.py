from odoo import fields, models , exceptions , _

class VppAccountPyment(models.Model):
    _inherit = 'account.payment'

    is_various_payment = fields.Boolean(
                            string='Is Various Payment', 
                            default=False,
                            help="Indicates if the payment is a various payment.\
                                    Disabling this option with a multiple payment already \
                                    assigned will have no effect on the last account in the \
                                    accounting entry.")

    payment_reason_id = fields.Many2one('payment.reason', string='Payment Reason')

    def _set_move_id_payable_account(self,raise_not_vp=False):
        self.ensure_one()
        if self.is_various_payment:
            for pay in self.with_context(skip_account_move_synchronization=True):
                liquidity_lines, counterpart_lines, writeoff_lines = pay._seek_for_lines()
                counterpart_lines.account_id = self.payment_reason_id.account_id
        elif raise_not_vp:
            raise exceptions.UserError(_("'%s' It is not assigning as various payments") % self.name)

    def create(self, vals_list):
        rec = super().create(vals_list)
        if rec.payment_reason_id.account_id :
            rec._set_move_id_payable_account()
        return rec
    
    def write(self, vals):
        response = super().write(vals)
        self._set_move_id_payable_account()
        return response
        
    def action_set_move_id_payable_account(self):
        for rec in self:
            rec._set_move_id_payable_account(True)
        _len = len(self)
        return {
                'type': 'ir.actions.client',
                'tag': 'display_notification',
                'params': {
                    'title': 'Success',
                    'message':  _('Reasons for payment recalculated successfully for %s records.') % (_len) \
                                if _len > 1 else _('Payment reason has been recalculated correctly'),
                    'type': 'success',   
                    'sticky': False,    
                }
            }