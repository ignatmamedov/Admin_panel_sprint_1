from django.contrib import admin
from .models import Genre, Person, Filmwork


class PersonRoleInline(admin.TabularInline):
    model = Person
    extra = 0

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_filter = ('type',)
    list_display = ('type', 'name', 'last_name', 'film',)
    pass


@admin.register(Filmwork)
class FilmworkAdmin(admin.ModelAdmin):
    list_filter = ('type',)
    list_display = ('type', 'title', 'creation_date', 'age_rating',)

    inlines = [
        PersonRoleInline
    ]
    pass
