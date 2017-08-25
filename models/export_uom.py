# -*- coding: utf-8 -*-
############################################################################
#    Coded by: Humanytek-Team (https://github.com/humanytek-team)
############################################################################
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
from openerp import api, fields, models


class ExportUOM(models.Model):
    _name = 'product.template.export_oum'

    code = fields.Integer(
        index=True,
        required=True,
    )
    name = fields.Char(
        index=True,
        required=True,
        string='Description',
    )

    @api.model
    def name_search(self, name, args=None, operator='ilike', limit=100):
        if name and not args:
            args = ['|', ('code', operator, name)]
        return super(ExportUOM, self).name_search(name, args, operator, limit)
