# -*- coding: utf-8 -*-
from odoo import models, fields

class TrelloConfig(models.Model):
    _name = 'managechicote.trello.config'
    _description = 'Configuración de la API de Trello'

    api_key = fields.Char(string="API Key", required=True)
    token = fields.Char(string="Token", required=True)
    board_id = fields.Char(string="Board ID", required=True)
