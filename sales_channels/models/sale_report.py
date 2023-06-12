# -*- coding: utf-8 -*-

from odoo import models, fields, _


class SaleReport(models.Model):
    _inherit = "sale.report"

    sales_channel_id = fields.Many2one('sales.channel', string="Sales Channel")

    def _query(self, with_clause='', fields={}, groupby='', from_clause=''):
        res = super()._query()

        Sale_SQL = res.split('UNION ALL')[0]
        Pos_SQL  = res.split('UNION ALL')[1]

        sale_select_index = Sale_SQL.find('SELECT')
        pos_select_index = Pos_SQL.find('SELECT')

        Sale_SQL = Sale_SQL[:sale_select_index + len('SELECT')] + '\n s.sales_channel_id AS sales_channel_id, ' + Sale_SQL[sale_select_index + len('SELECT'):]
        Pos_SQL  = Pos_SQL[:pos_select_index + len('SELECT')] + '\n pos.sales_channel_id AS sales_channel_id, ' + Pos_SQL[pos_select_index + len('SELECT'):]

        sale_groupby_index = Sale_SQL.find('GROUP BY')
        pos_groupby_index = Pos_SQL.find('GROUP BY')

        Sale_SQL = Sale_SQL[:sale_groupby_index + len('GROUP BY')] + '\n s.sales_channel_id, ' + Sale_SQL[sale_groupby_index + len('GROUP BY'):]
        Pos_SQL = Pos_SQL[:pos_groupby_index + len('GROUP BY')] + '\n pos.sales_channel_id, ' + Pos_SQL[pos_groupby_index + len('GROUP BY'):]

        return Sale_SQL + 'UNION ALL' + Pos_SQL

