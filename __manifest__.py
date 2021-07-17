# -*- coding: utf-8 -*-
{
    'name': "Supermarket Management",
    'summary':"""Supermarket management""",
    'sequence':-10,
    'description': """
        Manage a SuperMarket: customers, products, etc.... 
    """,
    'category':    'Supermarket',
    'version':     '1.0.0',
    # any module necessary for this one to work correctly
    'depends':['base'],
    # always loaded
    'data':        [
        "security/ir.model.access.csv",
    ],
   'installable':True,
   'application':True,
   'auto_install':False
   
}
