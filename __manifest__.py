# -*- coding: utf-8 -*-
{
    "name": "Margen de beneficio en las líneas de venta",
    "summary": "Calcula el margen de beneficio en las líneas de venta",
    "description":
        """
            Este módulo calcula el margen de beneficio en las líneas de venta.
            Permite a los usuarios ver el margen de beneficio directamente en las líneas de pedido de venta.
            Facilita la toma de decisiones informadas sobre precios y márgenes de beneficio.
        """,
    "author": "UnlimitSoft Technologies",
    "license": "AGPL-3",
    "website": "https://www.unlimitsoft.com.do",
    "category": "Uncategorized",
    "version": "18.0.0.0.4",
    # any module necessary for this one to work correctly
    "depends": ["base","account","sale_management"],
    "data": [
        "views/profit_margin_sale_order_line_views.xml",
    ],
    "installable": True,
    "application": False,
    "auto_install": False
}
