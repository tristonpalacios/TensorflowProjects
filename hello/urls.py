from django.urls import path
from hello import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from hello.models import LogMessage
from django.contrib import admin
from django.urls import include, path

home_list_view = views.HomeListView.as_view(
    queryset=LogMessage.objects.order_by("-log_date")[:5],  # :5 limits the results to the five most recent
    context_object_name="message_list",
    template_name="hello/home.html",
)

urlpatterns = [
    path("", home_list_view, name="home"),
    path("log/", views.log_message, name="log"),
    path("hello/<name>", views.hello_there, name="hello_there"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path('admin/', admin.site.urls),
]



urlpatterns += staticfiles_urlpatterns()