from odoo import _, api, fields, models, SUPERUSER_ID
from odoo.exceptions import UserError, RedirectWarning, ValidationError


class Partner(models.Model):
    _inherit = "res.partner"

    field3 = fields.Char("Field3")

    @api.depends("field3")
    def _compute_field2(self):
        breakpoint()
        for rec in self:
            rec.field2 = (rec.field1 or '') + ' ' + (rec.field3 or '')
