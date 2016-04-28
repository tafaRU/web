# -*- coding: utf-8 -*-
# © 2012 Savoir-faire Linux (<http://www.savoirfairelinux.com>).
# © 2014 Anybox <http://anybox.fr>
# © 2015 Taktik SA <http://taktik.be>
# © 2015 Étienne Beaudry Auger - Savoir-faire Linux
# © 2016 Alex Comba - Agile Business Group sagl
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Web Widget Color',
    'category': 'web',
    'version': '9.0.1.0.0',
    "author": 'Savoir-faire Linux, '
              'Anybox, '
              'Taktik SA, '
              'Odoo Community Association (OCA)',
    'depends': [
        'base', 'web'
    ],
    'data': [
        'view/web_widget_color_view.xml'
    ],
    'qweb': [
        'static/src/xml/widget.xml',
    ],
    'auto_install': False,
    'installable': True,
    'web_preload': True,
}
