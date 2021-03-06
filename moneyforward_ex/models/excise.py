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


class Excise(object):
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
        'long_name': 'str',
        'code': 'str',
        'rate': 'float'
    }

    attribute_map = {
        'id': 'id',
        'long_name': 'long_name',
        'code': 'code',
        'rate': 'rate'
    }

    def __init__(self, id=None, long_name=None, code=None, rate=None, local_vars_configuration=None):  # noqa: E501
        """Excise - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._long_name = None
        self._code = None
        self._rate = None
        self.discriminator = None

        self.id = id
        if long_name is not None:
            self.long_name = long_name
        if code is not None:
            self.code = code
        if rate is not None:
            self.rate = rate

    @property
    def id(self):
        """Gets the id of this Excise.  # noqa: E501

        税区分id  # noqa: E501

        :return: The id of this Excise.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Excise.

        税区分id  # noqa: E501

        :param id: The id of this Excise.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                id is not None and len(id) > 40):
            raise ValueError("Invalid value for `id`, length must be less than or equal to `40`")  # noqa: E501

        self._id = id

    @property
    def long_name(self):
        """Gets the long_name of this Excise.  # noqa: E501


        :return: The long_name of this Excise.  # noqa: E501
        :rtype: str
        """
        return self._long_name

    @long_name.setter
    def long_name(self, long_name):
        """Sets the long_name of this Excise.


        :param long_name: The long_name of this Excise.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                long_name is not None and len(long_name) > 100):
            raise ValueError("Invalid value for `long_name`, length must be less than or equal to `100`")  # noqa: E501

        self._long_name = long_name

    @property
    def code(self):
        """Gets the code of this Excise.  # noqa: E501


        :return: The code of this Excise.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this Excise.


        :param code: The code of this Excise.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                code is not None and len(code) > 20):
            raise ValueError("Invalid value for `code`, length must be less than or equal to `20`")  # noqa: E501

        self._code = code

    @property
    def rate(self):
        """Gets the rate of this Excise.  # noqa: E501

        税率  # noqa: E501

        :return: The rate of this Excise.  # noqa: E501
        :rtype: float
        """
        return self._rate

    @rate.setter
    def rate(self, rate):
        """Sets the rate of this Excise.

        税率  # noqa: E501

        :param rate: The rate of this Excise.  # noqa: E501
        :type: float
        """

        self._rate = rate

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
        if not isinstance(other, Excise):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Excise):
            return True

        return self.to_dict() != other.to_dict()
