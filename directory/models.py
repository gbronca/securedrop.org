from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils.text import slugify

from wagtail.contrib.wagtailroutablepage.models import RoutablePageMixin, route
from wagtail.wagtailcore.models import Page
from wagtail.wagtailadmin.edit_handlers import (
    InlinePanel,
)

from directory.forms import DirectoryForm
from landing_page_checker.landing_page import scanner
from landing_page_checker.models import Securedrop as SecuredropInstance


class DirectoryPage(RoutablePageMixin, Page):
    @route('form/')
    def form_view(self, request):
        if request.method == 'POST':
            # create a form instance and populate it with data from the request:
            form = DirectoryForm(request.POST)
            # check whether it's valid:
            if form.is_valid():
                data = form.cleaned_data
                # create secure_drop instance, adding parent page to the form
                instance = SecuredropInstance.objects.create(
                    page=self,
                    landing_page_domain=data['url'],
                    organization=data['organization'],
                    slug=slugify(data['organization']),
                    onion_address=data['tor_address'],
                )
                result = scanner.scan(instance)
                result.save()

                return HttpResponseRedirect('{0}thanks/'.format(self.url))

        # else redirect to a page with errors
        else:
            form = DirectoryForm()

        return render(
            request,
            'directory/directory_form.html',
            {'form': form, 'submit_url': '{0}form/'.format(self.url)}
        )

    @route('thanks/')
    def thanks_view(self, request):
        return render(request, 'directory/thanks.html')

    content_panels = Page.content_panels + [
        InlinePanel('instances', label='Securedrop Instances'),
    ]