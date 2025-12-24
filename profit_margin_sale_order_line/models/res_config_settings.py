from odoo import models, fields


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    use_profit_margin = fields.Boolean(
        string="Use the profit margin calculator on the base price for each line of sales.",
        readonly=False,
        config_parameter="profit_margin_sale_order_line.use_profit_margin",
    )
