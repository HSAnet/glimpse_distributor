import json

from django.http import HttpResponse, HttpResponseBadRequest
from django.views.generic.edit import BaseFormView

from distributor.packages import handlers
from distributor.packages.forms import PackageUploadForm
from distributor.packages.settings import CHANNEL_SETTINGS


class PackageUploadView(BaseFormView):
    form_class = PackageUploadForm

    def get(self, request, *args, **kwargs):
        return HttpResponseBadRequest('Internal service url, please see documentation on how to communicate.')

    def select_handler(self, raw_channel):
        if raw_channel in CHANNEL_SETTINGS:
            channel = CHANNEL_SETTINGS[raw_channel]
            try:
                handler = getattr(handlers, channel)
            except:
                raise Exception("Unable to load handler for this channel.")
            else:
                return handler
        raise Exception("Unknown channel, please check the value or the configuration in the settings file.")

    def form_valid(self, form):
        try:
            handler = self.select_handler(form.cleaned_data.get('channel'))
        except Exception as e:
            return self.response(False, {'Selector': str(e)})
        else:
            handler.handle_upload(form.cleaned_data.get('package'), self.request.FILES['package'])
            return self.response(True)

    def form_invalid(self, form):
        return self.response(False, form.errors)

    def response(self, success, errors={}):
        data = {
            'status': 'error'
        }
        if success:
            data['status'] = 'ok'
        else:
            data['errors'] = errors
        return HttpResponse(json.dumps(data))
