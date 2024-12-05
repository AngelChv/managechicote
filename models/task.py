# -*- coding: utf-8 -*-
from datetime import datetime

from odoo import models, fields, api


class task(models.Model):
    _name = "managechicote.task"
    _description = "managechicote.task"

    name = fields.Char(string="Nombre", required=True, help="Nombre de la tareaa")
    description = fields.Text(string="Descripción")
    start_date = fields.Datetime(string="Fecha de inicio")
    end_date = fields.Datetime(string="Fecha de finalización")
    is_paused = fields.Boolean(string="Pausada")
    code = fields.Char(string="Code", compute="_get_code")

    # Relaciones:
    sprint_id = fields.Many2one('managechicote.sprint', 'Sprint', compute="_get_sprint", store=True)
    technology_ids = fields.Many2many("managechicote.technology", string="Tecnologías", ondelete="cascade",
                                relation="task_technology",
                                column1="technology_ids",
                                column2="task_ids")
    history_id = fields.Many2one('managechicote.history', 'History', ondelete='cascade', required=True)

    # Métodos:
    def _get_code(self):
        for t in self:
            t.code = "TSK_" + str(t.id)


    @api.depends('code')
    def _get_sprint(self):
        for t in self:
            sprints = self.env['managechicote.sprint'].search([('project_id.id', '=', t.history_id.project_id.id)])
            found = False
            for sprint in sprints:
                if isinstance(sprint.end_date, datetime.date) and sprint.end_date > datetime.now():
                    t.sprint_id = sprint.id
                    found = True

            if not found:
                t.sprint_id = False

