from django.conf.urls import patterns  # , url

jornadas_urls = patterns('website',
    (r'^$', 'views.home'),
)
