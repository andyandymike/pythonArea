from queue import Queue 
from threading import Thread, Lock
import urllib.parse
import socket
import re
import time
from bs4 import BeautifulSoup
import os
from multiprocessing.pool import ThreadPool

seen_urls = set(['/'])
lock = Lock()
outfile = 'url.txt'

class Fetcher(Thread):
    def __init__(self, tasks):
        Thread.__init__(self)
        self.tasks = tasks
        self.daemon = True

    def run(self):
        while True:
            url = self.tasks.get()
            print(url)
            fp = open(outfile, 'a+')
            fp.write(str(url)+'\n')
            fp.close()
            sock = socket.socket()
            sock.connect(('localhost', 3000))
            get = 'GET {} HTTP/1.0\r\nHost: localhost\r\n\r\n'.format(url)
            sock.send(get.encode('ascii'))
            response = b''
            chunk = sock.recv(4096)
            while chunk:
                response += chunk
                chunk = sock.recv(4096)

            links = self.parse_links(url, response)

            lock.acquire()
            for link in links.difference(seen_urls):
                self.tasks.put(link)
            seen_urls.update(links)    
            lock.release()

            self.tasks.task_done()

    def parse_links(self, fetched_url, response):
        if not response:
            print('error: {}'.format(fetched_url))
            return set()
        if not self._is_html(response):
            return set()

        bsObj = BeautifulSoup(response, 'lxml')
        def has_attr_href(tag):
            return tag.has_attr('href')
        links = bsObj.find_all(has_attr_href)
        urls = (link['href'] for link in links)
        #urls = set(re.findall(r'''(?i)href=["']?([^\s"'<>]+)''', self.body(response)))

        links = set()
        for url in urls:
            normalized = urllib.parse.urljoin(fetched_url, url)
            parts = urllib.parse.urlparse(normalized)
            if parts.scheme not in ('', 'http', 'https'):
                continue
            host, port = urllib.parse.splitport(parts.netloc)
            if host and host.lower() not in ('localhost'):
                continue
            defragmented, frag = urllib.parse.urldefrag(parts.path)
            links.add(defragmented)

        return links

    def body(self, response):
        body = response.split(b'\r\n\r\n', 1)[1]
        return body.decode('utf-8')

    def _is_html(self, response):
        head, body = response.split(b'\r\n\r\n', 1)
        headers = dict(h.split(': ') for h in head.decode().split('\r\n')[1:])
        return headers.get('Content-Type', '').startswith('text/html')

if __name__ == '__main__':
    if os.path.isfile(outfile):
        os.remove(outfile)
    start = time.time()
    pool = ThreadPool()
    tasks = Queue()
    tasks.put("/")
    Workers = [Fetcher(tasks) for i in range(4)]
    pool.map_async(lambda w:w.run(), Workers)
    tasks.join()
    pool.close()

    print('{} URLs fetched in {:.1f} seconds'.format(len(seen_urls),time.time() - start))
