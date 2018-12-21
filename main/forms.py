from django.forms import ModelForm

from main.models import Comments


class CommentForm(ModelForm):
    """Форма для комментариев"""

    class Meta:
        model = Comments
        fields = ['text']

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update({'placeholder': 'Сообщение...', 'rows':'3'})