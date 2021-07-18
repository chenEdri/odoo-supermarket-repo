# -*- coding: utf-8 -*-
from datetime import date
from xmlrpc.client import DateTime, datetime 
from odoo import fields, models, api


class Cart(models.Model):
    _name = 'supermarket.cart'
    _description = 'Cart'

    # there is only one cart for each customer but a single customer can have more than one cart.
    customer = fields.One2many(comodel_name='Customer', inverse_name='Name')
    # not neccesary- it is a default one
    creation_time = fields.Datetime('YYYY-MM-DD HH:MM:SS')
    checkout_time = fields.Datetime('YYYY-MM-DD HH:MM:SS')
    update_time = fields.Datetime('YYYY-MM-DD HH:MM:SS')
    total_purchase_this_week = fields.Integer(
        compute='_compute_total_purchase')
    is_twice_aweek = fields.Boolean(compute='_compute_twice_aweek')

    @api.depends('customer', 'record.customer')
    def _compute_total_purchase(self):
        return self.product.unit_price * self.quantity

    @api.depends('customer', 'checkout_time')
    def _compute_twice_aweek(self):
        last_check = self.checkout_time
        # start_delta = datetime.timedelta(days=last_check[-2:], weeks=1)
        for record in self:
            if (record.checkout_date - last_check < 8 ): return True 
        return False  