from flask import render_template, url_for, flash, redirect
from web_page import app
from web_page.forms import InsertDataForm, ReturnButton
from prtpy.partitioning.recursive_number_partitioning_sy_v2 import rnp
from prtpy.binners import BinnerKeepingContents


@app.route('/results',  methods=['GET', 'POST'])
def results_page():
    button = ReturnButton()
    if button.is_submitted():
        return redirect(url_for(main_page.__name__))
    else:
        return render_template('results.html', results=results_page.results, button=button)
results_page.results = None


@app.route('/', methods=['GET', 'POST'])
def main_page():
    form = InsertDataForm()
    is_submitted = form.validate_on_submit()
    if not is_submitted:
        return render_template('home.html', form=form)
    else:
        numbers = [float(num) for num in form.numbers.data.split()]
        if len(numbers) >= 25 or form.k.data > 5:
            flash(f'Input is big ({len(form.numbers.data)} numbers and {form.k.data} bins. calculation may take a '
                  f'long time)', 'danger')
        results_page.results = rnp(BinnerKeepingContents(), form.k.data, numbers)[1]
        return redirect(url_for(results_page.__name__))
