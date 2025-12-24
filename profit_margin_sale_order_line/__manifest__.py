{
    "name": "Sales Order line Profit Margin",
    "version": "18.0.0.0.1",
    "description": """
        Enhance your Sales workflow by calculating and displaying profit margins on sales order lines.
        This module computes the profit margin for each line based on cost and sale price data, allowing
        users to quickly assess profitability without manual calculations. View margins directly on
        sales orders and use this insight for pricing decisions and financial analysis.
    """,
    "summary": "Compute and display profit margins on sales order lines for better pricing and reporting",
    "author": "UnlimitSoft",
    "maintainer": "UnlimitSoft",
    "website": "https://www.unlimitsoft.com.do/",
    "license": "AGPL-3",
    "category": "Sales",
    "currency": "USD",
    "price": 0.0,
    "depends": ["base", "account", "sale"],
    "data": [
        "views/sale_order_line.xml",
        "views/res_config_settings.xml",
    ],
    "auto_install": False,
    "application": False,
}
