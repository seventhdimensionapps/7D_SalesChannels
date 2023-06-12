# -*- coding: utf-8 -*-

from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    sales_channel_id = fields.Many2one('sales.channel', string="Sales Channel", store=True, related='team_id.sales_channel_id')
