# -*- coding: utf-8 -*-
from datetime import datetime

import requests
from odoo import models, fields, api
from odoo.exceptions import UserError


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
    history_id = fields.Many2one('managechicote.history', 'History', ondelete='cascade', required=False)

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


    @api.model
    def import_trello_tasks(self):
        """Método para importar tareas desde Trello a Odoo"""
        trello_config = self.env['managechicote.trello.config'].search([], limit=1)
        if not trello_config:
            raise UserError("No se ha configurado Trello correctamente.")

        # URL para obtener las tarjetas (tareas) desde Trello
        url = f'https://api.trello.com/1/boards/{trello_config.board_id}/cards'
        params = {
            'key': trello_config.api_key,
            'token': trello_config.token,
        }

        response = requests.get(url, params=params)
        if response.status_code != 200:
            raise UserError("Error al obtener datos de Trello.")

        trello_data = response.json()

        # Crear tareas en Odoo basadas en los datos de Trello
        for card in trello_data:
            # Puedes personalizar cómo quieres que se creen las tareas
            self.create({
                'name': card.get('name'),
                'description': card.get('desc'),
                'start_date': card.get('dateStart'),
                'end_date': card.get('dateEnd'),
                'is_paused': card.get('paused', False),  # Asume que el campo `paused` existe en Trello
            })
