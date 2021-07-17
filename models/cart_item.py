# -*- coding: utf-8 -*-
from odoo import fields, models


class CartItem(models.Model):
    _name = 'supermarket.cart_item'
    _description = 'Cart Item'

    product = fields.Char('Product')
    quantity = fields.Integer(String='Quantity')
    cart = fields.One2many(String='Cart')
    
    

  