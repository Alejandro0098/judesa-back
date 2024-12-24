from django.contrib import admin
from .models import Categories, News, Players, Products, Sponsors, Staff, Matches
import json
import logging

from django.db.models import JSONField 
from django.contrib import admin
from django.forms import widgets


logger = logging.getLogger(__name__)


class NewsJSONWidget(widgets.Textarea):
    def format_value(self, value):
        try:
            value = json.dumps(json.loads(value), indent=2, sort_keys=True)
            # these lines will try to adjust size of TextArea to fit to content
            row_lengths = [len(r) for r in value.split('\n')]
            self.attrs['rows'] = min(max(len(row_lengths) + 2, 10), 30)
            self.attrs['cols'] = min(max(max(row_lengths) + 2, 40), 120)
            return value
        except Exception as e:
            logger.warning("Error while formatting JSON: {}".format(e))
            return super(PrettyJSONWidget, self).format_value(value)

@admin.register(News)
class News(admin.ModelAdmin):
    formfield_overrides = {
        JSONField: {'widget': NewsJSONWidget}
    }


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    empty_value_display = '-'
    search_fields = ["name"]


# @admin.register(News)
# class NewsAdmin(admin.ModelAdmin):
#     pass


@admin.register(Players)
class PlayersAdmin(admin.ModelAdmin):
    pass


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    pass


@admin.register(Sponsors)
class SponsorsAdmin(admin.ModelAdmin):
    pass


@admin.register(Staff)
class StaffrAdmin(admin.ModelAdmin):
    pass


@admin.register(Matches)
class MatchesAdmin(admin.ModelAdmin):
    empty_value_display = '-'
    list_filter = ["category_id"]
    list_display = ('id', 'category_id', 'rival', 'match_date', 'juega_como', 'resultado')
    list_orderable = ('editar', 'category_id', 'rival', 'match_date', 'locality', 'resultado')
    
    def juega_como(self, obj):
        return 'Local' if obj.is_local else 'Visitante'
    
    def resultado(self, obj: Matches):
        return f'{obj.local_score} - {obj.visitant_score}' if obj.show_result else '-'

    


