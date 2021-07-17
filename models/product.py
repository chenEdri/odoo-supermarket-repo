# -*- coding: utf-8 -*-
from odoo import fields, models


class Product(models.Model):
    _name = 'supermarket.product'
    _description = 'Product'

    name = fields.Char('Name')
    product_category = fields.Id(String='Product')
    unit_price = fields.Integer(String='Unit Price')

    #if I can add colums to the field I will add :
    # is_available = fields.Bool(Stirng="availability")
    # total_amount = field.Integer(String="")
    

  