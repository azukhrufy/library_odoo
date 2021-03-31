# -*- coding: utf-8 -*-
{
    'name': "Library Odoo",

    'summary': """
        Aplikasi Library Odoo""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Ananda Zukhruf Awalwi",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'stock', 'product', 'contacts'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        #Information,
        'views/information/books.xml',
        'views/information/members.xml',
        #Pinjaman,
        'views/Pinjaman/cards.xml',
        'views/Pinjaman/lenderlist.xml',
        #actions,
        'views/actions/books_actions.xml',
        'views/actions/members_actions.xml',
        'views/actions/books_rent_actions.xml',
        'views/actions/books_available_actions.xml',
        'views/actions/librarycards_actions.xml',
        'views/actions/lenderlist_actions.xml',
        'views/actions/categ_actions.xml',
        'views/actions/rack_actions.xml',
        #config,
        'views/config/rack.xml',
        'views/config/writer.xml',
        'views/config/publisher.xml',
        'views/config/category.xml',
        #main view,
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
}