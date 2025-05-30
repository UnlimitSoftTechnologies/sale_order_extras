from odoo import models, fields, api


class ProfitMarginSaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    profit_margin = fields.Float(
        string='Profit Margin (%)',
        store=True,
        required=True,
        default=0.0,
        readonly=False,
        help="The profit margin percentage for the sale order line."
    )

    base_price = fields.Float(
        string="Base Price",
        store=True,
        required=True,
        default=0.0,
        readonly=False,
        help="Unit price before profit margin."
    )

    @api.model
    def create(self, vals):
        # Solo en creación: base_price toma el valor de price_unit si no se estableció
        if 'base_price' not in vals and 'price_unit' in vals:
            vals['base_price'] = vals['price_unit']
        return super().create(vals)
    
    @api.onchange('product_id')
    def _onchange_product_id_set_base_price(self):
        # Solo inicializa base_price una vez (si es cero)
        if self.product_id and not self.base_price and self.price_unit:
            self.base_price = self.price_unit

    @api.onchange('profit_margin','base_price')
    def _onchange_profit_margin(self):
        # Si cambia el margen, recalcula price_unit
        if self.base_price:
            self.price_unit = self.base_price * (1 + self.profit_margin / 100.0)
