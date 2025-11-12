{
    "name": "Profit Margin on Sales Order Lines",
    "summary": "Calculates the profit margin on sales order lines",
    "description": """
        This module calculates the profit margin on sales order lines.
        It allows users to view the profit margin directly on the sales order lines.
        It helps make informed decisions about pricing and profit margins.
    """,
    "author": "UnlimitSoft Technologies",
    "license": "AGPL-3",
    "website": "https://www.unlimitsoft.com.do",
    "category": "Sales Management",
    "version": "18.0.0.0.4",
    # any module necessary for this one to work correctly
    "depends": ["base", "account", "sale_management"],
    "data": [
        "views/sale_order_line.xml",
    ],
    "installable": True,
    "application": False,
    "auto_install": False
}
