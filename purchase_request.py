# This file is part of the purchase_margin module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import PoolMeta

__all__ = ['CreatePurchase']
__metaclass__ = PoolMeta


class CreatePurchase:
    __name__ = 'purchase.request.create_purchase'

    @classmethod
    def compute_purchase_line(cls, request, purchase):
        '''Create purchase line with supplier code and description'''
        line = super(CreatePurchase, cls).compute_purchase_line(request,
            purchase)
        line.on_change_product()
        return line
