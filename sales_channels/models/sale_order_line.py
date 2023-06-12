# -*- coding: utf-8 -*-

from odoo import api, fields, models


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    sales_channel_id = fields.Many2one('sales.channel', string="Sales Channel", store=True, related='order_id.team_id.sales_channel_id')