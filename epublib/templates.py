# -*- coding: utf-8 -*-

template_container_xml = '''
<?xml version="1.0"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
    <rootfiles>
        <rootfile full-path="EPUB/{}"
            media-type="application/oebps-package+xml" />
    </rootfiles>
</container>
'''

template_package_doc_xml = '''\
<metadata xmlns:dc="http://purl.org/dc/terms/">
  <dc:identifier id={uuid}>urn:uuid:{uuid}</dc:identifier>
  <dc:title>{title}</dc:title>
  <dc:language>{lang}</dc:lang>
  <meta property="dcterms:modified">{modified_at}</meta>
</metadata>\
'''