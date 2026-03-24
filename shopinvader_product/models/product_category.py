# Copyright 2023 ACSONE SA/NV
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class ProductCategory(models.Model):
    _inherit = "product.category"

    active = fields.Boolean(default=True)
    sequence = fields.Integer()
    level = fields.Integer(compute="_compute_level")

    def _get_parent(self):
        self.ensure_one()
        return self.parent_id

    @api.depends("parent_id", "parent_id.active")
    def _compute_level(self):
        for record in self:
            record.level = 0
            parent = record._get_parent()
            while parent and parent.active:
                record.level += 1
                parent = parent._get_parent()
