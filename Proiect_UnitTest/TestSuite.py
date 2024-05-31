import unittest
import HtmlTestRunner

from TestsInternetLogin import TestsLoginTheInternet
from TestsInternetAlerts import TestsAlertsTheInternet
from TestsInternetCheckbox import TestsCheckboxTheInternet


class TestSuite(unittest.TestCase):

    def test_suite(self):

        teste_de_rulat = unittest.TestSuite()

        teste_de_rulat.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(TestsLoginTheInternet),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestsAlertsTheInternet),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestsCheckboxTheInternet)
        ])

        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_title='TestReport',
            report_name='Smoke Test Result'
        )

        runner.run(teste_de_rulat)

# comanda terminal pip install html-testRunner
# comanda terminal python -m unittest TestSuite.py
