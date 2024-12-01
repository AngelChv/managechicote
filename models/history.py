# -*- coding: utf-8 -*-

from odoo import models, fields

class history(models.Model):
    _name = 'managechicote.history'
    _description = 'managechicote.history'

    name = fields.Char(string="Nombre", required=True, help="Nombre del la historia")
    description = fields.Text(string="Descripción")

    # Relaciones:
    project_id = fields.Many2one('managechicote.project', string="Project", ondelete='cascade', required=True)
    task_ids = fields.One2many('managechicote.task', 'history_id', string="Task")