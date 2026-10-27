import unittest
from proxy_util import normalize_socks_proxy_url


class TestProxyUtil(unittest.TestCase):
    def test_normalize_socks_proxy_url_user_pass(self):
        proxy = "1.2.3.4:1080:myuser:mypassword"
        result = normalize_socks_proxy_url(proxy)
        self.assertEqual(result, "socks5h://myuser:mypassword@1.2.3.4:1080")

    def test_normalize_socks_proxy_url_ip_port(self):
        proxy = "1.2.3.4:1080"
        result = normalize_socks_proxy_url(proxy)
        self.assertEqual(result, "socks5h://1.2.3.4:1080")

    def test_normalize_socks_proxy_url_empty(self):
        self.assertIsNone(normalize_socks_proxy_url(""))
        self.assertIsNone(normalize_socks_proxy_url(None))


if __name__ == "__main__":
    unittest.main()
