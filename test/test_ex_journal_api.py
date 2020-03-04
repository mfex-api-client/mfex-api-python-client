# coding: utf-8

"""
    マネーフォワード クラウド経費API

    このページは[マネーフォワード クラウド経費](https://expense.moneyforward.com)（クラウド型の経費精算・ワークフローサービス）のAPIドキュメントです。ご利用開始の手順については、[github](https://github.com/moneyforward/expense-api-doc) をご覧ください。バグ報告や改善要望はgithub上からissue登録をして頂ければ幸いです。このドキュメントは[Swagger](http://swagger.io)の仕様で作成されています。実際にこのページでAPIの試打を行うことができます。試打を行いたい場合は、APIを利用するアプリケーションの登録の際に、Redirect URIを`https://expense.moneyforward.com/api/oauth2-redirect.html`に指定してお試しください。  # noqa: E501

    The version of the OpenAPI document: 1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import mfexapiclient
from mfexapiclient.api.ex_journal_api import ExJournalApi  # noqa: E501
from mfexapiclient.rest import ApiException


class TestExJournalApi(unittest.TestCase):
    """ExJournalApi unit test stubs"""

    def setUp(self):
        self.api = mfexapiclient.api.ex_journal_api.ExJournalApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_find_office_ex_journals_by_ex_reports(self):
        """Test case for find_office_ex_journals_by_ex_reports

        事業所全体の申請に紐づく仕訳リストを返す  # noqa: E501
        """
        pass

    def test_find_office_ex_journals_by_ex_transactions(self):
        """Test case for find_office_ex_journals_by_ex_transactions

        事業所全体の明細に紐づく仕訳リストを返す  # noqa: E501
        """
        pass

    def test_find_office_ex_report_journal(self):
        """Test case for find_office_ex_report_journal

        申請に対応する仕訳を返す  # noqa: E501
        """
        pass

    def test_find_office_ex_report_unit_journal(self):
        """Test case for find_office_ex_report_unit_journal

        集計に対応する仕訳を返す  # noqa: E501
        """
        pass

    def test_find_office_ex_transaction_journal(self):
        """Test case for find_office_ex_transaction_journal

        経費明細に対応する仕訳を返す  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()