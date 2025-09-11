# -*- coding: utf-8 -*-
{
    'name': 'Various Payment Plan',
    'version': '0.0.3',
    'summary': "Add the miscellaneous payments plan to accounting",
    'description':"Changed outgoing payments to allow the use of a different debit account depending on the reason for the payment.",
    'author': 'acevedoesteban999@gmail.com',
    'website': '',
    'category': 'Accounting/Accounting',
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
