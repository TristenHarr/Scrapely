from Forms._SuperTable import *
from flask import session
import sqlite3

def _SuperTable(request, table, action):
    dropform = DropForm(request.form)
    swapform = SwapForm(request.form)
    tableform = TableForm(request.form)
    savenew = SaveNew(request.form)
    pushform = PushForm(request.form)
    newrow = NewRow(request.form)
    if action == "drop" and request.method == 'POST' and dropform.validate():
        con = sqlite3.
    elif action == 'swap' and request.method == "POST" and swapform.validate():
        print("DO THE SWAP HERE")
    elif action == 'select_table' and request.method == 'POST' and tableform.validate():
        print("DO THE SELECT HERE")
    elif action == 'save_new' and request.method == "POST" and savenew.validate():
        print("DO THE SAVE HERE")
    elif action == 'push' and request.method == 'POST' and pushform.validate():
        print("DO THE PUSH HERE")
    elif action == 'new_row' and request.method == "POST" and newrow.validate():
        print("DO THE NEW ROW HERE")

    x = SuperTable('tweet', table, session['username'])
    x.generate_functions()
    x.main_maker()
    return Response(x.table_starter(10)