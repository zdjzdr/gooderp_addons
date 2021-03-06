# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2013-Today OpenERP SA (<http://www.openerp.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    "name": "GOODERP Goods Management",
    "version": "0.1",
    "author": 'ZhengXiang',
    "website": "http://www.osbzr.com",
    "category": "Generic Modules",
    "depends": ['core', 'decimal_precision'],
    "description": """
    """,
    "data": [
        'security/groups.xml',
        'view/goods_view.xml',
        'action/goods_action.xml',
        'menu/goods_menu.xml',
        'security/ir.model.access.csv',
    ],
    'demo': ['goods_demo.xml'],
    'installable': True,
    "active": False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
