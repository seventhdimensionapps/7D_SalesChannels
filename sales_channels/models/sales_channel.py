# -*- coding: utf-8 -*-

from odoo import api, fields, models


class SalesChannel(models.Model):
    _name = 'sales.channel'

    name = fields.Char(string="Channel Name", required=True)