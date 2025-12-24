from odoo import models, fields, api


class ProfitMarginSaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    use_profit_margin = fields.Boolean(
        related="order_id.use_profit_margin",
        string="Use profit margin",
        store=False,
        readonly=True,
    )

    profit_margin = fields.Float(
        string="Profit margin (%)",
        store=True,
        required=True,
        default=0.0,
        readonly=False,
        help="Percentage of profit applied over the base price.",
    )

    base_price = fields.Float(
        string="Base price",
        store=True,
        required=True,
        default=0.0,
        readonly=False,
        help="Unit price before applying the profit margin.",
    )

    @api.model
    def create(self, vals):
        # Only apply profit-margin-related defaults when the system option is enabled
        param = (
            self.env["ir.config_parameter"]
            .sudo()
            .get_param("profit_margin_sale_order_line.use_profit_margin")
        )
        use_margin = param in (True, "True", "true", "1", 1)

        if use_margin:
            # If base_price is not defined, take price_unit as the base
            if "base_price" not in vals and "price_unit" in vals:
                vals["base_price"] = vals["price_unit"]

            # If profit margin and base price are defined, recalculate price_unit
            if "profit_margin" in vals and "base_price" in vals:
                vals["price_unit"] = vals["base_price"] * (
                    1 + vals["profit_margin"] / 100.0
                )

        return super().create(vals)

    @api.onchange("product_id")
    def _onchange_product_id_set_base_price(self):
        """When a product is selected, initialize the base price."""
        # Only set base/price when the feature is enabled for this order
        if not self.order_id or not self.order_id.use_profit_margin:
            return
        if self.product_id:
            self.base_price = self.product_id.lst_price or 0.0
            self.price_unit = self.base_price * (1 + self.profit_margin / 100.0)

    @api.onchange("profit_margin", "base_price")
    def _onchange_profit_margin(self):
        """Recalculate the unit price when the margin or base price changes."""
        if not self.order_id or not self.order_id.use_profit_margin:
            return
        if self.base_price:
            self.price_unit = self.base_price * (1 + self.profit_margin / 100.0)

    @api.onchange("price_unit")
    def _onchange_price_unit_update_profit(self):
        """If the user manually changes the unit price, update the profit margin."""
        if not self.order_id or not self.order_id.use_profit_margin:
            return
        if self.base_price:
            self.profit_margin = ((self.price_unit / self.base_price) - 1) * 100
