from bs4 import BeautifulSoup
from urllib.parse import quote_plus
import requests
from WhatsAppManifest.adb.base import WhatsAppManifest


class APKPureDownload(WhatsAppManifest):

    def __init__(self):
        self.build_logger(type(self).__name__)

    def search(self, query):
        res = requests.get('https://apkpure.com/search?q={}&region='.format(quote_plus(query)), headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.5 (KHTML, like Gecko) '
                          'Version/9.1.2 Safari/601.7.5 '
        }).text
        soup = BeautifulSoup(res, "html.parser")
        search_result = soup.find('div', {'id': 'search-res'}).find('dl', {'class': 'search-dl'})
        app_tag = search_result.find('p', {'class': 'search-title'}).find('a')
        download_link = 'https://apkpure.com' + app_tag['href']
        return download_link

    def download(self, link, path=".", file_name: str = None):
        from os.path import join

        res = requests.get(link + '/download?from=details', headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.5 (KHTML, like Gecko) '
                          'Version/9.1.2 Safari/601.7.5 '
        }).text

        soup = BeautifulSoup(res, "html.parser").find('a', {'id': 'download_link'})

        if soup['href']:
            r = requests.get(soup['href'], stream=True, headers={
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.5 (KHTML, like Gecko) '
                              'Version/9.1.2 Safari/601.7.5 '
            })

            path = join(path, link.split('/')[-1] + '.apk' if file_name is None else file_name)

            with open(path, 'wb') as file:
                for chunk in r.iter_content(chunk_size=1024):
                    if chunk:
                        file.write(chunk)

    def download_apk(self, app_id, path: str = ".", file_name: str = None):
        download_link = self.search(app_id)

        if download_link is not None:
            self.logger.debug('Downloading {}.apk ...'.format(download_link))
            self.download(download_link, path, file_name)
            self.logger.info('Download completed!')
        else:
            self.logger.info("No results")
