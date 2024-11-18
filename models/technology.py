# -*- coding: utf-8 -*-

from odoo import models, fields

class technology(models.Model):
    _name = 'managechicote.technology'
    _description = 'managechicote.technology'

    name = fields.Char(string="Nombre", required=True, help="Nombre de la tecnología")
    description = fields.Text(string="Descripción")
    photo = fields.Image(string="Imagen de la tecnología", help="Imagen de la tecnología", widget="photo")
