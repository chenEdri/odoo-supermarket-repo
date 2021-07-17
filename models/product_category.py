# -*- coding: utf-8 -*-
from odoo import fields, models


class Product_category(models.Model):
    _name = 'supermarket.product_category'
    _description = 'Product_category'

    name = fields.Char('Name')
    

  