# -*- coding: utf-8 -*-
{
    "name": "Sales Channel",

    "version": "16.0.0.1",

    "summary": """ """,

    "description": """ Group all your omni-channel business by Sales Channel like 'Distribution, POS, 	Field, eCommerce and more """,

    "website": "https://www.7d.com.kw",
    'images': ['static/description/img_2.png'],

    "category": "Sales",

    "license": 'OPL-1',

    "author": "Seventh Dimension",

    "depends" : ["base", "sale", "point_of_sale", "sales_team", "pos_sale"],

    "data" : [
        "security/ir.model.access.csv",
        "views/sales_channel.xml",
        "views/crm_team.xml",
        "views/sale_order.xml",
        "views/pos_order.xml",
    ],
}
