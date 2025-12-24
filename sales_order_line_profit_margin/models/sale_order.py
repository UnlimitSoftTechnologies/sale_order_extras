from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = "sale.order"

    use_profit_margin = fields.Boolean(
        string="Use profit argin",
        default=lambda self: self.env.user.has_group(
            "sales_order_line_profit_margin.use_profit_margin"
        ),
        readonly=False,
    )
