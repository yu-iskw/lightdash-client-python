from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.api_validate_response_status import ApiValidateResponseStatus

if TYPE_CHECKING:
    from ..models.validation_error_chart_response import ValidationErrorChartResponse
    from ..models.validation_error_dashboard_response import (
        ValidationErrorDashboardResponse,
    )
    from ..models.validation_error_table_response import ValidationErrorTableResponse


T = TypeVar("T", bound="ApiValidateResponse")


@_attrs_define
class ApiValidateResponse:
    """
    Attributes:
        results (List[Union['ValidationErrorChartResponse', 'ValidationErrorDashboardResponse',
            'ValidationErrorTableResponse']]):
        status (ApiValidateResponseStatus):
    """

    results: List[
        Union["ValidationErrorChartResponse", "ValidationErrorDashboardResponse", "ValidationErrorTableResponse"]
    ]
    status: ApiValidateResponseStatus
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.validation_error_chart_response import (
            ValidationErrorChartResponse,
        )
        from ..models.validation_error_dashboard_response import (
            ValidationErrorDashboardResponse,
        )

        results = []
        for results_item_data in self.results:
            results_item: Dict[str, Any]
            if isinstance(results_item_data, ValidationErrorChartResponse):
                results_item = results_item_data.to_dict()
            elif isinstance(results_item_data, ValidationErrorDashboardResponse):
                results_item = results_item_data.to_dict()
            else:
                results_item = results_item_data.to_dict()

            results.append(results_item)

        status = self.status.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "results": results,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.validation_error_chart_response import (
            ValidationErrorChartResponse,
        )
        from ..models.validation_error_dashboard_response import (
            ValidationErrorDashboardResponse,
        )
        from ..models.validation_error_table_response import (
            ValidationErrorTableResponse,
        )

        d = src_dict.copy()
        results = []
        _results = d.pop("results")
        for results_item_data in _results:

            def _parse_results_item(
                data: object,
            ) -> Union[
                "ValidationErrorChartResponse", "ValidationErrorDashboardResponse", "ValidationErrorTableResponse"
            ]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_validation_response_type_0 = ValidationErrorChartResponse.from_dict(data)

                    return componentsschemas_validation_response_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_validation_response_type_1 = ValidationErrorDashboardResponse.from_dict(data)

                    return componentsschemas_validation_response_type_1
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_validation_response_type_2 = ValidationErrorTableResponse.from_dict(data)

                return componentsschemas_validation_response_type_2

            results_item = _parse_results_item(results_item_data)

            results.append(results_item)

        status = ApiValidateResponseStatus(d.pop("status"))

        api_validate_response = cls(
            results=results,
            status=status,
        )

        api_validate_response.additional_properties = d
        return api_validate_response

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
