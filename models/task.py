# -*- coding: utf-8 -*-
from odoo import models, fields


class task(models.Model):
    _name = "managechicote.task"
    _description = "managechicote.task"

    name = fields.Char(string="Nombre", required=True, help="Nombre de la tareaa")
    description = fields.Text(string="Descripción")
    start_date = fields.Datetime(string="Fecha de inicio")
    end_date = fields.Datetime(string="Fecha de finalización")
    is_paused = fields.Boolean(string="Pausada")

    # Relaciones:
    sprint_id = fields.Many2one('managechicote.sprint', 'Sprint', ondelete='cascade', required=True)
    technology_ids = fields.Many2many("managechicote.technology", string="Tecnologías", ondelete="cascade",
                                relation="task_technology",
                                column1="technology_ids",
                                column2="task_ids")
    history_id = fields.Many2one('managechicote.history', 'History', ondelete='cascade', required=True)
