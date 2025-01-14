# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions


class TrelloConfig(models.Model):
    _name = 'managechicote.trello.config'
    _description = 'Configuración de Trello'

    api_key = fields.Char(string="API Key", required=True)
    token = fields.Char(string="Token", required=True)
    board_id = fields.Char(string="Board ID", required=True)

    @api.model
    def init(self):
        # Si no existe el registro, se crea el primero
        if not self.search([]):
            self.create({
                'api_key': 'DEFAULT_API_KEY',
                'token': 'DEFAULT_TOKEN',
                'board_id': 'DEFAULT_BOARD_ID',
            })

    @api.model
    def create(self, vals):
        # Evitar que se puedan crear más registros, ya que la configuración solo es una.
        # También quito el permiso del csv
        # Y en la vista tree se oculta el botón
        if self.search([], limit=1):
            raise exceptions.UserError("Solo se permite un único registro de configuración.")
        return super(TrelloConfig, self).create(vals)

    # No necesita el decorador @api.model, ya que no trabaja a nivel de modelo.
    def unlink(self):
        # Evitar que se borre el único registro.
        # También quito el permiso del csv
        # Y en la vista tree se oculta el botón
        if len(self.search([])) <= 1:
            raise exceptions.UserError("No puedes eliminar el único registro existente.")
        return super(TrelloConfig, self).unlink()
