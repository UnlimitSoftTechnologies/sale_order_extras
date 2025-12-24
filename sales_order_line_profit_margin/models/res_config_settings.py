from odoo import models, fields


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    use_profit_margin = fields.Boolean(
        string="Use the profit margin calculator on the base price for each line of sales.",
        config_parameter="sales_order_line_profit_margin.use_profit_margin",
        implied_group="sales_order_line_profit_margin.use_profit_margin",
        readonly=False,
    )

    def set_values(self):
        super().set_values()
        group = self.env.ref(
            "sales_order_line_profit_margin.use_profit_margin", raise_if_not_found=False
        )
        if not group:
            return

        users = self.env["res.users"].sudo().search([])
        # If enabled, assign group to all users; otherwise remove from all users
        if self.use_profit_margin:
            group.sudo().write({"users": [(6, 0, users.ids)]})
        else:
            group.sudo().write({"users": [(6, 0, [])]})
