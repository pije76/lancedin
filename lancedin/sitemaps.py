from django.contrib.sitemaps import Sitemap
from project.models import Project


class StaticSitemap(Sitemap):
    priority = 0.5
    lastmod = None

    def items(self):
        return [
        "/",
        "/about",
        "/press",
        ("/opportunities", "daily"),
        ("/people", "daily")
        ]

    def location(self, obj):
        return obj[0] if isinstance(obj, tuple) else obj

    def changefreq(self, obj):
        return obj[1] if isinstance(obj, tuple) else "monthly"


class BaseSitemap(Sitemap):
    priority = 0.5
    changefreq = "weekly"

    def location(self, obj):
        return obj.get_absolute_url(False)

    def lastmod(self, obj):
        return obj.modified or obj.created


class ProjectSitemap(BaseSitemap):
    changefreq = "daily"

    def items(self):
        return Project.objects.filter(
            is_private=False,
            state=u'CONFIRMED'
        )
