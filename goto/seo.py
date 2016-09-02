from djangoseo import seo



class MyMetadata(seo.Metadata):
    description = seo.MetaTag(max_length=155)
    keywords = seo.KeywordTag()
    rights = seo.MetaTag(max_length=155)
    title = seo.MetaTag(name="title",
                           verbose_name="title")
    image = seo.MetaTag(name="og:image",
                        verbose_name='image')
    og_title = seo.MetaTag(name="og:title",
                           populate_from="title",
                           verbose_name="facebook title")
    og_site_name = seo.MetaTag(name="og:site_name",
                           populate_from="title",
                           verbose_name="facebook sitename")
    class Meta():
        use_sites = False
        seo_models = ('goto.Event', )


