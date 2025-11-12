from odoo import models, fields, api


class ProfitMarginSaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    profit_margin = fields.Float(
        string='Profit Margin (%)',
        store=True,
        required=True,
        default=0.0,
        readonly=False,
        help="Porcentaje de ganancia aplicado sobre el precio base."
    )

    base_price = fields.Float(
        string="Base Price",
        store=True,
        required=True,
        default=0.0,
        readonly=False,
        help="Precio unitario base antes de aplicar margen de ganancia."
    )

    @api.model
    def create(self, vals):
        # Si no se ha definido base_price, se toma el price_unit como base
        if 'base_price' not in vals and 'price_unit' in vals:
            vals['base_price'] = vals['price_unit']

        # Si se definió margen y precio base, recalcula el price_unit
        if 'profit_margin' in vals and 'base_price' in vals:
            vals['price_unit'] = vals['base_price'] * (1 + vals['profit_margin'] / 100.0)

        return super().create(vals)

    @api.onchange('product_id')
    def _onchange_product_id_set_base_price(self):
        """Cuando se selecciona un producto, inicializa el precio base."""
        if self.product_id:
            self.base_price = self.product_id.lst_price or 0.0
            self.price_unit = self.base_price * (1 + self.profit_margin / 100.0)

    @api.onchange('profit_margin', 'base_price')
    def _onchange_profit_margin(self):
        """Recalcula el precio unitario cuando cambia el margen o el precio base."""
        if self.base_price:
            self.price_unit = self.base_price * (1 + self.profit_margin / 100.0)

    @api.onchange('price_unit')
    def _onchange_price_unit_update_profit(self):
        """Si el usuario cambia manualmente el precio unitario, actualiza el margen."""
        if self.base_price:
            self.profit_margin = ((self.price_unit / self.base_price) - 1) * 100
