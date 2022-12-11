import re

from .common import InfoExtractor

class Kamababa2IE(InfoExtractor):
    _VALID_URL = r'(?:https?://)?(?:www\.)?kamababa\.desi/(?P<id>[a-zA-Z0-9-]+)' # match a-z 0-9 and dash

    def _real_extract(self, url):
        mobj = re.match(self._VALID_URL, url)

        video_id = mobj.group('id')
        webpage_url = 'https://www.kamababa.desi/' + video_id
        webpage = self._download_webpage(webpage_url, video_id)

        # Log that we are starting to parse the page
        self.report_extraction(video_id)

        iframe_url = self._html_search_regex(r'<iframe src="(.+?)" frameborder="0" scrolling="no" allowfullscreen></iframe>', webpage, u'iframe URL')
        iframe_webpage = self._download_webpage(iframe_url, '')

        video_url = self._html_search_regex(r'<source src="(.+?)" type="video/mp4"></source>', iframe_webpage, u'video URL')

        return {
            'id':        video_id,
            'url':       video_url,
            'ext':       'mp4',
            'title':     self._og_search_title(webpage),
        }
