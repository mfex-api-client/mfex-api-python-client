# coding: utf-8

"""
    マネーフォワード クラウド経費API

    このページは[マネーフォワード クラウド経費](https://expense.moneyforward.com)（クラウド型の経費精算・ワークフローサービス）のAPIドキュメントです。ご利用開始の手順については、[github](https://github.com/moneyforward/expense-api-doc) をご覧ください。バグ報告や改善要望はgithub上からissue登録をして頂ければ幸いです。このドキュメントは[Swagger](http://swagger.io)の仕様で作成されています。実際にこのページでAPIの試打を行うことができます。試打を行いたい場合は、APIを利用するアプリケーションの登録の際に、Redirect URIを`https://expense.moneyforward.com/api/oauth2-redirect.html`に指定してお試しください。  # noqa: E501

    The version of the OpenAPI document: 1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from moneyforward_ex.configuration import Configuration


class ExReportType(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'id': 'str',
        'name': 'str',
        'use_ex_transaction_reserves': 'bool',
        'use_transaction_action_after_approval': 'str',
        'is_active': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'use_ex_transaction_reserves': 'use_ex_transaction_reserves',
        'use_transaction_action_after_approval': 'use_transaction_action_after_approval',
        'is_active': 'is_active'
    }

    def __init__(self, id=None, name=None, use_ex_transaction_reserves=False, use_transaction_action_after_approval='none', is_active=True, local_vars_configuration=None):  # noqa: E501
        """ExReportType - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._use_ex_transaction_reserves = None
        self._use_transaction_action_after_approval = None
        self._is_active = None
        self.discriminator = None

        self.id = id
        if name is not None:
            self.name = name
        if use_ex_transaction_reserves is not None:
            self.use_ex_transaction_reserves = use_ex_transaction_reserves
        if use_transaction_action_after_approval is not None:
            self.use_transaction_action_after_approval = use_transaction_action_after_approval
        if is_active is not None:
            self.is_active = is_active

    @property
    def id(self):
        """Gets the id of this ExReportType.  # noqa: E501

        申請種別id  # noqa: E501

        :return: The id of this ExReportType.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ExReportType.

        申請種別id  # noqa: E501

        :param id: The id of this ExReportType.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                id is not None and len(id) > 40):
            raise ValueError("Invalid value for `id`, length must be less than or equal to `40`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this ExReportType.  # noqa: E501

        申請種別名称  # noqa: E501

        :return: The name of this ExReportType.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ExReportType.

        申請種別名称  # noqa: E501

        :param name: The name of this ExReportType.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 100):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `100`")  # noqa: E501

        self._name = name

    @property
    def use_ex_transaction_reserves(self):
        """Gets the use_ex_transaction_reserves of this ExReportType.  # noqa: E501

        明細を添付するかどうかのフラグ  # noqa: E501

        :return: The use_ex_transaction_reserves of this ExReportType.  # noqa: E501
        :rtype: bool
        """
        return self._use_ex_transaction_reserves

    @use_ex_transaction_reserves.setter
    def use_ex_transaction_reserves(self, use_ex_transaction_reserves):
        """Sets the use_ex_transaction_reserves of this ExReportType.

        明細を添付するかどうかのフラグ  # noqa: E501

        :param use_ex_transaction_reserves: The use_ex_transaction_reserves of this ExReportType.  # noqa: E501
        :type: bool
        """

        self._use_ex_transaction_reserves = use_ex_transaction_reserves

    @property
    def use_transaction_action_after_approval(self):
        """Gets the use_transaction_action_after_approval of this ExReportType.  # noqa: E501

        明細を添付した場合に申請承認後の処理。transfer_to_ex_transaction: 立替の経費明細にコピー, create_journal: 仕訳を作成, none: 何もしない  # noqa: E501

        :return: The use_transaction_action_after_approval of this ExReportType.  # noqa: E501
        :rtype: str
        """
        return self._use_transaction_action_after_approval

    @use_transaction_action_after_approval.setter
    def use_transaction_action_after_approval(self, use_transaction_action_after_approval):
        """Sets the use_transaction_action_after_approval of this ExReportType.

        明細を添付した場合に申請承認後の処理。transfer_to_ex_transaction: 立替の経費明細にコピー, create_journal: 仕訳を作成, none: 何もしない  # noqa: E501

        :param use_transaction_action_after_approval: The use_transaction_action_after_approval of this ExReportType.  # noqa: E501
        :type: str
        """
        allowed_values = ["transfer_to_ex_transaction", "create_journal", "none"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and use_transaction_action_after_approval not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `use_transaction_action_after_approval` ({0}), must be one of {1}"  # noqa: E501
                .format(use_transaction_action_after_approval, allowed_values)
            )

        self._use_transaction_action_after_approval = use_transaction_action_after_approval

    @property
    def is_active(self):
        """Gets the is_active of this ExReportType.  # noqa: E501

        使用フラグ  # noqa: E501

        :return: The is_active of this ExReportType.  # noqa: E501
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """Sets the is_active of this ExReportType.

        使用フラグ  # noqa: E501

        :param is_active: The is_active of this ExReportType.  # noqa: E501
        :type: bool
        """

        self._is_active = is_active

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ExReportType):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ExReportType):
            return True

        return self.to_dict() != other.to_dict()
