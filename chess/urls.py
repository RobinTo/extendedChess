from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SimpleChess.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

	url(r'^$', "chess.simpleChess.views.chess", name='chess'),
	url(r'^getGameFen/', "chess.simpleChess.views.getGameFen", name='getFen'),
    url(r'^admin/', include(admin.site.urls)),
)
