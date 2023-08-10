from odoo import _, api, fields, models, SUPERUSER_ID
from odoo.exceptions import UserError, RedirectWarning, ValidationError


class Partner(models.Model):
    _inherit = "res.partner"

    field1 = fields.Char("Field1")
    field2 = fields.Char("Field2", compute="_compute_field2", store=True)

    @api.depends("field1")
    def _compute_field2(self):
        for rec in self:
            rec.field2 = rec.field1
