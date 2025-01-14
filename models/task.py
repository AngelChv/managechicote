# -*- coding: utf-8 -*-
import logging
from datetime import datetime
from pytz import UTC
import requests
from odoo import models, fields, api
from odoo.exceptions import UserError

_logger = logging.getLogger(__name__)

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

    @staticmethod
    def convert_iso_to_odoo_format(iso_date):
        """Convierte una fecha ISO 8601 al formato esperado por Odoo (%Y-%m-%d %H:%M:%S)."""
        if iso_date:
            try:
                # Convertir de ISO 8601 (UTC) al formato Odoo
                date_utc = datetime.strptime(iso_date, '%Y-%m-%dT%H:%M:%S.%fZ').replace(tzinfo=UTC)
                return date_utc.strftime('%Y-%m-%d %H:%M:%S')
            except ValueError as e:
                raise UserError(f"Error al convertir la fecha: {iso_date}. Detalles: {e}")
        return False

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
            self.create({
                'name': card.get('name'),
                'description': card.get('desc'),
                'start_date': self.convert_iso_to_odoo_format(card.get('start')),
                'end_date': self.convert_iso_to_odoo_format(card.get('due')),
                'is_paused': card.get('paused', False),
            })

        _logger.info("La importación desde Trello ha terminado.")
        # Notificación al usuario usando action_notify
        return {
            'type': 'ir.actions.client',
            'tag': 'reload',
            'params': {
                'title': 'Trello Importación',
                'message': 'Se han importado correctamente todas las tareas desde Trello.',
                'sticky': False,  # La notificación desaparece después de un tiempo.
            },
        }
