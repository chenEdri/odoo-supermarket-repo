# -*- coding: utf-8 -*-
from odoo import fields, models, api


class CartItem(models.Model):
    _name = 'supermarket.cart_item'
    _description = 'Cart Item'

    product = fields.One2many(comodel_name='Product', inverse_name='name') # there is only one cart for each product but a single product is referenced by several cart items.
    quantity = fields.Integer() #number of products
    cart = fields.One2many(comodel_name='Cart', ondelete='cascade') # One cart has several items, and an item is part of one cart, so it's also a one2many association.
    total_amount= fields.Float(compute='_compute_total')


    @api.depends('product_id.unit_price','quantity')
    def _compute_total(self):
         return self.product.unit_price * self.quantity 
    
    

  