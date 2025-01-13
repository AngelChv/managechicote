# -*- coding: utf-8 -*-
from odoo import models, fields, api

class TrelloConfig(models.Model):
    _name = 'managechicote.trello.config'
    _description = 'Configuración de Trello'

    api_key = fields.Char(string="API Key", required=True)
    token = fields.Char(string="Token", required=True)
    board_id = fields.Char(string="Board ID", required=True)

    @api.model
    def create(self, vals):
        # Si ya existe un registro, modificamos ese registro en lugar de crear uno nuevo
        existing_record = self.search([], limit=1)
        if existing_record:
            existing_record.write(vals)  # Actualiza el registro existente
            return existing_record  # Devuelve el registro actualizado
        return super(TrelloConfig, self).create(vals)

    @api.model
    def init(self):
        # Si no existe el registro, creamos el primero
        if not self.search([]):
            self.create({
                'api_key': 'DEFAULT_API_KEY',
                'token': 'DEFAULT_TOKEN',
                'board_id': 'DEFAULT_BOARD_ID',
            })
