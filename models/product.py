# -*- coding: utf-8 -*-
from odoo import fields, models


class Product(models.Model):
    _name = 'supermarket.product'
    _description = 'Product'

    name = fields.Char('Name')
    product = fields.Char('Product')
    category = fields.Char('Category')
    unit_price = fields.Integer(String='Unit Price')
    

  