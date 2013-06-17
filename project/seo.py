from rollyourown import seo


class MyMetadata(seo.Metadata):
    title = seo.Tag(head=True, max_length=68)
    description = seo.MetaTag(max_length=155)
    keywords = seo.KeywordTag()
    heading = seo.Tag(name="h1")

    class HelpText:
        title = "This will appear in the window/tab name, as well as in search results."
        keywords = "A comma separated list of words or phrases that describe the content"
        description = "This will appear in the description"

    class Meta:
        seo_views = ('project', )
