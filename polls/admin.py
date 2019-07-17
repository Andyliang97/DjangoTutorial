from django.contrib import admin
from .models import Question, Choice


# Register your models here.

# admin.TabularInline can save some space while displaying everything
class ChoiceInline(admin.StackedInline):
    """
    This tells Django: “Choice objects are edited on the Question admin page.
    By default, provide enough fields for 3 choices.”
    """
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):

    # this changes the outlook of the whole question list

    list_display = ('question_text', 'pub_date', 'was_published_recently')

    # this change the outlook inside of a single question
    """
    this will order the fields in the following order
    fields = ['pub_date', 'question_text']
    """

    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    # add choice into the question
    inlines = [ChoiceInline]

    # That adds a “Filter” sidebar that lets people filter the change list by the pub_date field
    list_filter = ['pub_date']

    # That adds a search box at the top of the change list
    search_fields = ['question_text', 'pub_date']


admin.site.register(Question, QuestionAdmin)

# admin.site.register(Choice)
