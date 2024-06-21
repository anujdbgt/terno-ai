from django.shortcuts import render
from django.http import JsonResponse
import terno.models as models
import terno.utils as utils
import sqlalchemy
import sqlshield.models as shield_models


def index(request):
    return render(request, 'frontend/index.html')


def settings(request):
    return render(request, 'frontend/index.html')


def generate_table_response(request):
    # convert the resultset generated by SQLAlchemy to JSON
    pass


def get_sql_for_english_query(request):
    datasource = models.DataSource.objects.first()
    role = request.user.groups.all()
    allowed_tables, allowed_columns = utils.get_admin_config_object(datasource, role)  # Gives us tables and column allowed for user

    engine = sqlalchemy.create_engine(datasource.connection_str)
    inspector = sqlalchemy.inspect(engine)
    mDb = shield_models.MDatabase.from_inspector(inspector)
    mDb.keep_only_tables(allowed_tables.values_list('name', flat=True))
    tables = mDb.get_table_dict()
    print(tables)
    return JsonResponse({'response': 'This is LLM response', 'tables': list(tables.keys())})
