from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions

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
    MOUNTAIN_RANGES = [[x.pk, x.name] for x in MountainRange.objects.all()]

    # allow selection of multiple mountain ranges in which to search
    mountain_range = forms.MultipleChoiceField(choices=MOUNTAIN_RANGES,
        widget=forms.CheckboxSelectMultiple(), required=False)

class MountainCrispySearchForm(forms.Form):
    text = forms.CharField(label="search text", max_length=100)
    
    # may need to move this into an __init__ method?
    # but it seems to be ok when I add a new mountain range.. maybe the server restarted?
    MOUNTAIN_RANGES = [[x.pk, x.name] for x in MountainRange.objects.all()]

    # allow selection of multiple mountain ranges in which to search
    mountain_range = forms.MultipleChoiceField(choices=MOUNTAIN_RANGES,
        widget=forms.CheckboxSelectMultiple(), required=False)
    
    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.label_class = 'col-lg-2'
    helper.field_class = 'col-lg-8'

    helper.layout = Layout(
        Field('text'),
        HTML("""
            <a class="btn btn-primary" role="button" data-toggle="collapse" href="#collapseExample" aria-expanded="false" aria-controls="collapseExample">
  Search by mountain range:
    </a>
    <div class="collapse" id="collapseExample">
        <div class="well">
        """),
   
        Field('mountain_range'),
        HTML("""
              </div>
            </div>
            """),
        FormActions(
            Submit('submit', 'Go!', css_class="btn-primary"),
            )
        )