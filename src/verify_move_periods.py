# -*- coding: utf-8 -*-
"""Module for daily verification

Example:
        $ python verify_move_periods.py

Attributes:
    none
"""
from drivers import odoo_connector
from datetime import timedelta, date, datetime
import logging, pprint

#Establish connection
con = odoo_connector.Connection()

#Find all supplier invoices not in draft
moves = con.searchRead('account.move')

for move in moves:
    # Verify period against date
    if (move['date'][:4] != move['period_id'][1][-4:]) or (move['date'][5:7] != move['period_id'][1][:2]):
        logging.warning(move['journal_id'][1] + ' ' + move['name'] + ' dated ' + move['date'] + ' has conflicting period and date')
print(len(moves), 'moves analyzed')
