from email import utils
from time import time
from xml.dom.minidom import Document


class RSSFeed(object):
    """Represents an RSS feed."""

    def __init__(self, title, description, url):
        """Initialize the feed."""
        self._document = Document()
        rss_element = self._document.createElement('rss')
        rss_element.setAttribute('version', '2.0')
        self._document.appendChild(rss_element)
        self._channel = self._document.createElement('channel')
        rss_element.appendChild(self._channel)
        self._channel.appendChild(self._create_text_element('title', title))
        self._channel.appendChild(self._create_text_element('link', url))
        self._channel.appendChild(self._create_text_element('description', description))
        self._channel.appendChild(self._create_text_element('lastBuildDate', utils.formatdate(time())))

    def _create_text_element(self, type_, text):
        """Create an element with a text node."""
        element = self._document.createElement(type_)
        element.appendChild(self._document.createTextNode(text))
        return element

    def append_item(self, title, link=None, description=None, pubDate=None):
        """Append an item to the feed."""
        item = self._document.createElement('item')
        item.appendChild(self._create_text_element('title', title))
        if link is not None:
            item.appendChild(self._create_text_element('link', link))
        if description is not None:
            item.appendChild(self._create_text_element('description', description))
        if pubDate is not None:
            item.appendChild(self._create_text_element('pubDate', pubDate))
        self._channel.appendChild(item)

    def get_xml(self):
        """Return the XML for the feed."""
        return self._document.toxml()
