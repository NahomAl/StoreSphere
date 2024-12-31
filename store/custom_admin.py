from django.contrib import admin
from django.urls import path
from django.template.response import TemplateResponse


class CustomAdminSite(admin.AdminSite):
    site_header = 'StoreSphere Administration'
    site_title = 'StoreSphere Admin'
    index_title = 'Admin Dashboard'

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('dashboard/', self.admin_view(self.dashboard_view), name='dashboard'),
        ]
        return custom_urls + urls

    def dashboard_view(self, request):
        context = dict(
            self.each_context(request),
            title=self.index_title,
        )
        return TemplateResponse(request, 'admin/dashboard.html', context)


custom_admin_site = CustomAdminSite(name='custom_admin')
