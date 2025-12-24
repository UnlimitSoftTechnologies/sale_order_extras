from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = "sale.order"

    use_profit_margin = fields.Boolean(
        string="Use profit margin",
        compute="_compute_use_profit_margin",
        store=True,
        readonly=False,
        precompute=True,
    )

    def _compute_use_profit_margin(self):
        param = (
            self.env["ir.config_parameter"]
            .sudo()
            .get_param("profit_margin_sale_order_line.use_profit_margin")
        )
        enabled = param in (True, "True", "true", "1", 1)
        for rec in self:
            rec.use_profit_margin = enabled
