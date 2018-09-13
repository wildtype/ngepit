from bs4 import BeautifulSoup
from unittest import TestCase
from ..dashboard import generate_html

class TestDashboardGenerateHtml(TestCase):
    def assertContainSelector(self, html, selector, text=None):
        parsed_html = BeautifulSoup(html, 'html.parser')

        node = parsed_html.select(selector)
        node_contains_text = node[0].text == text
        self.assertTrue(node)
        self.assertIn(text, node[0].text)

    def test_it_generate_html_with_data(self):
        html = generate_html(total_distance=1, total_moving_time=2.3, max_speed=3.4, average_speed=4.5)
        
        self.assertContainSelector(html, '.stats__metric-value.stats__total-distance', text='1')
        self.assertContainSelector(html, '.stats__metric-value.stats__total-moving-time', text='2.3')
        self.assertContainSelector(html, '.stats__metric-value.stats__max-speed', text='3.4')
        self.assertContainSelector(html, '.stats__metric-value.stats__average-speed', text='4.5')
