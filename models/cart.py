# -*- coding: utf-8 -*-
from odoo import fields, models


class Cart(models.Model):
    _name = 'supermarket.cart'
    _description = 'Cart'

    custumer = fields.Char('Name')
    date_of_creation = fields.Datetime(String='Date of creation')
    
    

  