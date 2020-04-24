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


class Attendant(object):
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
        'company_name': 'str',
        'department_name': 'str',
        'position_name': 'str',
        'is_own_company': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'company_name': 'company_name',
        'department_name': 'department_name',
        'position_name': 'position_name',
        'is_own_company': 'is_own_company'
    }

    def __init__(self, id=None, name=None, company_name=None, department_name=None, position_name=None, is_own_company=None, local_vars_configuration=None):  # noqa: E501
        """Attendant - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._company_name = None
        self._department_name = None
        self._position_name = None
        self._is_own_company = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.company_name = company_name
        if department_name is not None:
            self.department_name = department_name
        if position_name is not None:
            self.position_name = position_name
        self.is_own_company = is_own_company

    @property
    def id(self):
        """Gets the id of this Attendant.  # noqa: E501

        出席者id  # noqa: E501

        :return: The id of this Attendant.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Attendant.

        出席者id  # noqa: E501

        :param id: The id of this Attendant.  # noqa: E501
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
        """Gets the name of this Attendant.  # noqa: E501

        氏名  # noqa: E501

        :return: The name of this Attendant.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Attendant.

        氏名  # noqa: E501

        :param name: The name of this Attendant.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 100):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `100`")  # noqa: E501

        self._name = name

    @property
    def company_name(self):
        """Gets the company_name of this Attendant.  # noqa: E501

        会社名  # noqa: E501

        :return: The company_name of this Attendant.  # noqa: E501
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """Sets the company_name of this Attendant.

        会社名  # noqa: E501

        :param company_name: The company_name of this Attendant.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and company_name is None:  # noqa: E501
            raise ValueError("Invalid value for `company_name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                company_name is not None and len(company_name) > 100):
            raise ValueError("Invalid value for `company_name`, length must be less than or equal to `100`")  # noqa: E501

        self._company_name = company_name

    @property
    def department_name(self):
        """Gets the department_name of this Attendant.  # noqa: E501

        部門名  # noqa: E501

        :return: The department_name of this Attendant.  # noqa: E501
        :rtype: str
        """
        return self._department_name

    @department_name.setter
    def department_name(self, department_name):
        """Sets the department_name of this Attendant.

        部門名  # noqa: E501

        :param department_name: The department_name of this Attendant.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                department_name is not None and len(department_name) > 100):
            raise ValueError("Invalid value for `department_name`, length must be less than or equal to `100`")  # noqa: E501

        self._department_name = department_name

    @property
    def position_name(self):
        """Gets the position_name of this Attendant.  # noqa: E501

        役職  # noqa: E501

        :return: The position_name of this Attendant.  # noqa: E501
        :rtype: str
        """
        return self._position_name

    @position_name.setter
    def position_name(self, position_name):
        """Sets the position_name of this Attendant.

        役職  # noqa: E501

        :param position_name: The position_name of this Attendant.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                position_name is not None and len(position_name) > 100):
            raise ValueError("Invalid value for `position_name`, length must be less than or equal to `100`")  # noqa: E501

        self._position_name = position_name

    @property
    def is_own_company(self):
        """Gets the is_own_company of this Attendant.  # noqa: E501

        自社/他社フラグ  # noqa: E501

        :return: The is_own_company of this Attendant.  # noqa: E501
        :rtype: bool
        """
        return self._is_own_company

    @is_own_company.setter
    def is_own_company(self, is_own_company):
        """Sets the is_own_company of this Attendant.

        自社/他社フラグ  # noqa: E501

        :param is_own_company: The is_own_company of this Attendant.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and is_own_company is None:  # noqa: E501
            raise ValueError("Invalid value for `is_own_company`, must not be `None`")  # noqa: E501

        self._is_own_company = is_own_company

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
        if not isinstance(other, Attendant):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Attendant):
            return True

        return self.to_dict() != other.to_dict()