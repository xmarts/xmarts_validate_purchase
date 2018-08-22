# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions, _
from odoo.exceptions import AccessError, UserError, RedirectWarning, ValidationError, Warning
from odoo.tools.misc import formatLang
from odoo.addons.base.res.res_partner import WARNING_MESSAGE, WARNING_HELP


class addPermission(models.Model):
    _name = 'res.users'
    _inherit = 'res.users'

    valid_purchase = fields.Boolean(string='Valida Compras')


class purchaseTypes(models.Model):
    _name = 'purchase.order.types'

    name = fields.Char(string='Tipo de compra', required=True)
    userss = fields.Many2many('res.users', string='Usuarios')


class PurchaseOrder(models.Model):
    _name = 'purchase.order'
    _inherit = 'purchase.order'

    valid_purchase = fields.Boolean(string='Validar Compra')
    purchase_type = fields.Many2one('purchase.order.types', string='Tipo de Compra')
    #user_valid = fields.Many2one('res.users', string='Valido')
    id_active = fields.Boolean(default=False, compute='rev_users',string="Puede validar")

    @api.one
    def rev_users(self):
        lista=[]
        for l in self.purchase_type.userss:
            lista.append(l.id)
        if self.env.uid in lista:
            self.id_active = True
        else:
            self.id_active = False

    @api.one
    @api.multi
    def button_confirm(self):
        if self.valid_purchase == False:
            raise exceptions.ValidationError('Necesita confirmación del pedido')

        res = super(validPurchase, self).button_confirm()

        return res
