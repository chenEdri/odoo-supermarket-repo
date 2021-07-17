# -*- coding: utf-8 -*-
from odoo import fields, models


class Product(models.Model):
    _name = 'supermarket.product'
    _description = 'Product'

    name = fields.Char('Name')
    category = fields.Many2one(comodel_name ='Category', ondelete='cascade') # there are many product for each category and not vice versa.
    unit_price = fields.Integer(String='Unit Price')

    #if I can add colums to the field I will add :
    # total_amount = field.Integer(String='Total amount')
    # currency = field.Char('Currency')
    

  