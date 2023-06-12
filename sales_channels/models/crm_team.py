# -*- coding: utf-8 -*-

from odoo import api, fields, models


class CrmTeam(models.Model):
    _inherit = "crm.team"

    sales_channel_id = fields.Many2one('sales.channel', string="Sales Channel")