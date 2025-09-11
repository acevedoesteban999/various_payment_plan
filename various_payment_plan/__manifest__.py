# -*- coding: utf-8 -*-
{
    'name': 'Various Payment Plan',
    'version': '0.0.2',
    'summary': """ Various Payment Plan Description """,
    'author': '',
    'website': '',
    'category': '',
    'depends': [
        'base',
        'account',
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/account_payment_views.xml",
        "views/payment_reason_views.xml",

        "views/menu.xml",
    ],
    
    'application': False,
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
