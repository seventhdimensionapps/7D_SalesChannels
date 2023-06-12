# -*- coding: utf-8 -*-

from odoo import api, fields, models


class PosOrder(models.Model):
    _inherit = 'pos.order'

    sales_channel_id = fields.Many2one('sales.channel', string="Sales Channel", store=True, compute='compute_sales_channel')


    @api.depends('config_id', 'config_id.crm_team_id', 'config_id.crm_team_id.sales_channel_id')
    def compute_sales_channel(self):
        for record in self:
            if record.config_id.crm_team_id and record.config_id.crm_team_id.sales_channel_id:
                record.sales_channel_id = record.config_id.crm_team_id.sales_channel_id.id
            else:
                record.sales_channel_id = False