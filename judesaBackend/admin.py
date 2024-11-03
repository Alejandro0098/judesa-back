from django.contrib import admin
from .models import Categories, News, Players, Products, Sponsors, Staff, Matches

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    empty_value_display = '-'
    search_fields = ["name"]


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    pass


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

    


