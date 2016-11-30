from flask_wtf import Form
from markupsafe import Markup


class FormBase(Form):

    def __init__(self, formdata=None, obj=None, method='post', **kwargs):
        self._method = method
        Form.__init__(self, formdata, obj=obj, **kwargs)

    def start(self, **kwargs):
        attributes = " ".join(
            ['{}="{}"'.format(key, value) for key, value in kwargs.iteritems()]
        )

        return Markup(
            '<form name="{name}" method="{method}" {attributes}'
        ).format(
            name=self.get_name(),
            method=self._method.lower(),
            attributes=Markup(attributes)
        )

    def end(self):
        return Markup('</form>')

    def get_name(self):
        return self.__class__.__name__.lower()