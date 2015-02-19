Installation & configuration
============================

Requirements
------------

1. Python
2. Django
3. Requests

Installation
------------

    $ pip install dproxy

Next, you need to add "dproxy" to the ``INSTALLED_APPS`` list 
in your Django settings module (typically ``settings.py``)::

    INSTALLED_APPS = (
        ...
        'dproxy',
    )

Configuration
-------------

The core of DProxy is a class-based Django view, 
:class:`dproxy.views.DProxy`.

To use DProxy, you create an entry in your ``urls.py`` that forwards
requests to the :class:`~dproxy.views.DProxy` view class, e.g.::

    from dproxy.views import DProxy

    urlpatterns += patterns('',
        (r'^proxy/(?P<url>.*)$', DProxy.as_view(base_url='http://www.python.org')),
    )
    
Given the above url config, request matching ``/proxy/<any-url>`` will be 
handled by the configured :class:`~dproxy.views.DProxy` view instance and 
forwarded to ``http://www.python.org/<any-url>``.
