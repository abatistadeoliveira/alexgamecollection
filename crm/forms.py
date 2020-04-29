from django import forms
from .models import Collector, Console, VideoGame


class CollectorForm(forms.ModelForm):
    class Meta:
        model = Collector
        fields = ('coll_name', 'account_number', 'address', 'city', 'state', 'zipcode', 'email','phone_number')


class ConsoleForm(forms.ModelForm):
   class Meta:
        model = Console
        fields = ('coll_name', 'console_name', 'description', 'console_model', 'console_color', 'console_brand', 'console_price' )


class VideoGameForm(forms.ModelForm):
    class Meta:
        model = VideoGame
        fields = ('coll_name', 'videogame_name', 'videogame_console', 'v_description', 'quantity', 'videogame_charge' )
