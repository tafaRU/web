# -*- coding: utf-8 -*-
# © 2012 Étienne Beaudry Auger - Savoir-faire Linux
# © 2016 Alex Comba - Agile Business Group sagl
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Web Color',
    'author': 'Savoir-faire Linux,Odoo Community Association (OCA)',
    'category': 'Hidden',
    'version': '9.0.1.0.0',
    'depends': [
        'web'
    ],
    'js': [
        'static/src/js/lib.js',
        'static/lib/really-simple-color-picker/jquery.colorPicker.js',
    ],
    'css': [
        'static/src/css/color.css',
        'static/lib/really-simple-color-picker/colorPicker.css',
     ],
    'qweb': [
        'static/src/xml/lib.xml'
    ],
    'installable': True,
    'auto_install': False,
    'web_preload': False,
}
