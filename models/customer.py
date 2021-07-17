# -*- coding: utf-8 -*-
from odoo import fields, models,api


class Customer(models.Model):
    _name = 'supermarket.customer'
    _description = 'Customer'

    name = fields.Char('Name')
    email = fields.Char('Email')
    city = fields.Char('City')
    street = fields.Char('Street')
    # build a function that will check after each purchase if there where any other purchases in the last seven days. if so the bool value will be truthy.

    isPremiumCustomer = fields.Boolean(compute='_compute_check_visits')

    @api.depends('cart_id.customer', 'cart_id.is_twice_aweek') #use compute info from other Module table.
    def _compute_check_visits(self):
       return (self.cart_id.is_twice_aweek)


    
    