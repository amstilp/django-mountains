from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field, Reset
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions, InlineCheckboxes

from . models import Mountain, MountainRange

class MountainForm(forms.ModelForm):

    class Meta:
        model = Mountain
        fields = ('name', 'mountain_range', 'description', 'height', 'latitude', 'longitude', 'number_of_summits', 'image', 'snow_level', 'number_of_marmots_seen')


class MountainRangeForm(forms.ModelForm):

    class Meta:
        model = MountainRange
        fields = ('name', 'region', )


class MountainSearchForm(forms.Form):
    text = forms.CharField(label="search text", max_length=100)
    
    # may need to move this into an __init__ method?
    # but it seems to be ok when I add a new mountain range.. maybe the server restarted?
    MOUNTAIN_RANGES = [[x.pk, x.name] for x in MountainRange.objects.all().order_by('name')]

    # allow selection of multiple mountain ranges in which to search
    mountain_range = forms.MultipleChoiceField(choices=MOUNTAIN_RANGES,
        widget=forms.CheckboxSelectMultiple(), required=False)

class MountainCrispySearchForm(forms.Form):
    text = forms.CharField(label="search text", max_length=100)
    
    # may need to move this into an __init__ method?
    # but it seems to be ok when I add a new mountain range.. maybe the server restarted?
    # could possible separate this into multiple phases?
    MOUNTAIN_RANGES = [[x.pk, x.name] for x in MountainRange.objects.all().order_by('name')]

    # allow selection of multiple mountain ranges in which to search
    mountain_range = forms.MultipleChoiceField(choices=MOUNTAIN_RANGES,
        widget=forms.CheckboxSelectMultiple(), required=False, label=None,
        help_text="If no mountain range is selected, all will be searched.")
    
    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.label_class = 'col-lg-2'
    helper.field_class = 'col-lg-8'

    helper.layout = Layout(
        Field('text'),
        HTML("""
            <a class="btn btn-default" role="button" data-toggle="collapse" href="#collapseMountainRange" aria-expanded="false" aria-controls="collapseMountainRange">
  Select by mountain range:
    </a>
    <div class="collapse" id="collapseMountainRange">
        <div class="well">
        """),
   
        InlineCheckboxes('mountain_range'),
        HTML("""
              </div>
            </div>
            <hr>
            """), # the <hr> adds some space between this button and the submit button
        FormActions(
            Submit('submit', 'Search!', css_class="btn-primary btn-disable"),
            Reset('name', 'Reset!', css_class="btn-disable"),
            )
        )



