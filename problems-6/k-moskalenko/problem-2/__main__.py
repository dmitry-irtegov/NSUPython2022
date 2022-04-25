import unittest
from .problem import url_regex, extract_urls


# noinspection HttpUrlsUsage
class URLTestCase(unittest.TestCase):
    def test_correct(self):
        correct_urls = (
            'http://foo.com/blah_blah',
            'http://foo.com/blah_blah/',
            'http://foo.com/blah_blah_(wikipedia)',
            'http://foo.com/blah_blah_(wikipedia)_(again)',
            'http://www.example.com/wpstyle/?p=364',
            'https://www.example.com/foo/?bar=baz&inga=42&quux',
            'http://a.b.c.d.e.f.g.h.i.j.k.l.m.n.o.p.q.r.s.t.u.v.w.x.y.z.com',
            'http://user:pass@example.com:123/one/two.three?q1=a1&q2=a2#body',
            'http://www.microsoft.xn--comindex-g03d.html.irongeek.com',
            'http://localhost/',
            'http://localhost/blah_blah',
            'http://userid:password@example.com:8080',
            'http://userid:password@example.com:8080/',
            'http://userid@example.com',
            'http://userid@example.com/',
            'http://userid@example.com:8080',
            'http://userid@example.com:8080/',
            'http://userid:password@example.com',
            'http://userid:password@example.com/',
            'http://142.42.1.1/',
            'http://142.42.1.1:8080/',
            'http://foo.com/blah_(wikipedia)#cite-1',
            'http://foo.com/blah_(wikipedia)_blah#cite-1',
            'http://foo.com/(something)?after=parens',
            'http://code.google.com/events/#&product=browser',
            'http://j.mp',
            'http://foo.bar/?q=Test%20URL-encoded%20stuff',
            'http://-.~_!$&\'()*+\';=:%40:80%2f::::::@example.com',
            'http://a.b-c.de',
            'http://223.255.255.254',
            'http://example.com?foo=bar',
            'http://example.com#foo',
            'http://example.com.',
            'www.google.com/unicorn',
            'http://example',
            'http://example/foo/?bar=baz&inga=42&quux',
            'https://userid:password@a.b.c.d.example:8080',
        )

        for url in correct_urls:
            self.assertRegex(url, f'^{url_regex}$')

    def test_incorrect(self):
        incorrect_urls = (
            'http://',
            'http://.',
            'http://..',
            'http://../',
            'http://?',
            'http://??',
            'http://??/',
            'http://#',
            'http://##',
            'http://##/',
            'http://foo.bar?q=Spaces should be encoded',
            '//',
            '//a',
            '///a',
            '///',
            'http:///a',
            'foo.com',
            'rdar://1234',
            'http:// shouldfail.com',
            ':// should fail',
            'http://foo.bar/foo(bar)baz quux',
            'http://-error-.invalid/',
            'http://-a.b.co',
            'http://a.b-.co',
            'http://123.123.123',
            'http://3628126748',
            'http://.www.foo.bar/',
            'http://.www.foo.bar./',
            'http://foo.bar/ /',
            'http://a.b_z.com',
            'http://ab_.z.com',
            'http://google\\.com',
            'http://www(google.com',
            'http://www=google.com',
            'https://www.g.com/error\n/bleh/bleh',
            'rdar://1234',
            '/foo.bar/',
            '///www.foo.bar./'
        )

        for url in incorrect_urls:
            self.assertNotRegex(url, f'^{url_regex}$')

    def test_extract(self):
        text = '''
            Lorem ipsum www.dolor.sit
            <a href="http://example.com">example.com</a>
            <a href="http://example.com/with-path">with path</a>
            [and another](https://another.example.com) and
            Foo https://bar.net/?q=Query with spaces
        '''

        urls = [
            'www.dolor.sit',
            'http://example.com',
            'http://example.com/with-path',
            'https://another.example.com',
            'https://bar.net/?q=Query'
        ]

        self.assertListEqual(urls, extract_urls(text))


if __name__ == '__main__':
    unittest.main()
