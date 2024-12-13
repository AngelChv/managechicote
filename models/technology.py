# -*- coding: utf-8 -*-

from odoo import models, fields

class technology(models.Model):
    _name = 'managechicote.technology'
    _description = 'managechicote.technology'

    name = fields.Char(string="Nombre", required=True, help="Nombre de la tecnología")
    description = fields.Text(string="Descripción")
    photo = fields.Image(string="Imagen de la tecnología", help="Imagen de la tecnología", widget="photo")

    # Relaciones:
    task_ids = fields.Many2many("managechicote.task", string="Tareas", ondelete="cascade",
                                   relation="task_technology",
                                   column1="task_ids",
                                   column2="technology_ids")
    developers = fields.Many2many('manage.developer', string='Developers',
                                    relation='developer_technologies',
                                    column2='developer_id',
                                    column1='technologies_id')
