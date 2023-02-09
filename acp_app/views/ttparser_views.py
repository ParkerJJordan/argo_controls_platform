import pandas as pd
from flask import Blueprint, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, StringField
from acp_app import db
from sqlalchemy.orm import sessionmaker
from acp_app.models import Truthtables
from wtforms.validators import DataRequired  
from acp_app.services.common import render_dataframe
from acp_app.services.truthtable_parser import TruthtableDB
from pathlib import Path


class TruthtableParseForm(FlaskForm):
    
    ttname = StringField('Truthtable/Unit', validators=[DataRequired()])
    seqnum = IntegerField('Sequence', validators=[DataRequired()])
    submit = SubmitField('Read Truthtable')

bp = Blueprint('ttparser', __name__)


@bp.route('/truthtable_parser/<search_name>/<search_num>', methods=['GET', 'POST'])
def ttparse(search_name, search_num):

    tt_table = None
    ttname = search_name
    seqnum = search_num

    # Session = sessionmaker(bind=db.engine)
    # session = Session()
    
    df = Truthtables
    try:
        # tt_table = session.query(Truthtables) \
        # .filter(Truthtables.name.like(ttname),
        #         Truthtables.seq.like(seqnum)).all() #Properly filter out?
        tt_table = df.query(f'Truthtable==@ttname and `Sequence Number`==@seqnum')        
    except:
        SortError = True
        tt_table = pd.DataFrame()
        
    tt_table = render_dataframe(tt_table, True)
    ttparse_form = TruthtableParseForm(prefix='ttparser')
    
    if ttparse_form.validate_on_submit() and ttparse_form.submit.data:
        ttname = str(ttparse_form.ttname.data)
        seqnum = int(ttparse_form.seqnum.data)
        return redirect(url_for('ttparser.ttparse',
                        search_name=ttname,
                        search_num=seqnum))

    if SortError:
        flash(
            f'{ttname} - Sequence {seqnum} not found. The truthtable name or sequence may be invaild.', 'alert-danger')

    return render_template('ttparser/ttparser.html',
                           ttparse_form=ttparse_form,
                           ttname=ttname,
                           seqnum=seqnum,
                           tt_table=tt_table)


@bp.cli.command('init')
def load_truthtable_db():
    all_tts = []
    #path = f'acp_app/data/raw/gcc'
    path = f'C:/Users/pjordan/TruthtablesTest/ref1'

    files = Path(path).glob('**/*.xls')
    for file in files:
        truthtable = TruthtableDB(file)
        all_tts.append(truthtable.tt)
    tt_master = pd.concat(all_tts)

    tt_master.to_sql('tt_master',
                             db.engine,
                             if_exists='replace',
                             index=True,
                             index_label='index')

    print('Successfully loaded truthtables into the database')

    return True
