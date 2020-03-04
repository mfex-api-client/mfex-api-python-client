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
from mfexapiclient.api.ex_destination_api import ExDestinationApi  # noqa: E501
from mfexapiclient.rest import ApiException


class TestExDestinationApi(unittest.TestCase):
    """ExDestinationApi unit test stubs"""

    def setUp(self):
        self.api = mfexapiclient.api.ex_destination_api.ExDestinationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_ex_destination(self):
        """Test case for create_ex_destination

        支払先マスタを作成する  # noqa: E501
        """
        pass

    def test_delete_ex_destination(self):
        """Test case for delete_ex_destination

        支払先マスタを削除する  # noqa: E501
        """
        pass

    def test_find_ex_destination(self):
        """Test case for find_ex_destination

        支払先マスタを返す  # noqa: E501
        """
        pass

    def test_find_ex_destinations(self):
        """Test case for find_ex_destinations

        支払先マスタ一覧を返す  # noqa: E501
        """
        pass

    def test_update_ex_destination(self):
        """Test case for update_ex_destination

        支払先マスタを更新する  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()