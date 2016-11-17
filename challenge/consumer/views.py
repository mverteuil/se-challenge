from django.views.generic.edit import FormView
from django.views.generic.list import ListView

from .forms import CSVMigrateForm
from .migrator import CSVMigrator
from .models import Expense


class CSVMigrateFormView(FormView):
    """ Migrates data from files in CSV format to the database. """
    form_class = CSVMigrateForm
    template_name = "csvmigrate.html"
    success_url = '/list/'

    def form_valid(self, form):
        migrator = CSVMigrator(form.files['csv_file'])
        migrator.migrate()
        return super(CSVMigrateFormView, self).form_valid(form)


class ExpenseListView(ListView):
    model = Expense