# -*- coding: utf-8 -*-
from odoo import fields, models


class ProductCategory(models.Model):
    _name = 'supermarket.product_category'
    _description = 'Product_category'

    name = fields.Char('Name')
    

  