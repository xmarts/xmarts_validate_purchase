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

    valid_purchase = fields.Boolean(string='Validar Compra',default=False)
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

    @api.model
    def purchse_searchs(self):
        cr = self.env.cr
        sql = "select po.id from purchase_order po inner join purchase_order_types pot on pot.id=po.purchase_type inner join purchase_order_types_res_users_rel potu on potu.purchase_order_types_id=pot.id where (po.valid_purchase=False or po.valid_purchase is null) AND potu.res_users_id='"+str(self.env.uid)+"'"
        cr.execute(sql)
        compras = cr.fetchall()
        if compras==None:
            raise exceptions.ValidationError('No tiene compras por validar')

        lista=[]
        for l in compras:
            lista.append(l[0])
        action = {
            'type': 'ir.actions.act_window',
            'view_mode': 'tree,form',
            'name': _('Compras Prueba'),
            'res_model': 'purchase.order',
            'domain': ['&',('valid_purchase', '=', False),('id', 'in', lista)],
        }
        return action

    @api.one
    @api.multi
    def button_confirm(self):
        if self.valid_purchase == False:
            raise exceptions.ValidationError('Necesita confirmación del pedido')

        res = super(validPurchase, self).button_confirm()

        return res
