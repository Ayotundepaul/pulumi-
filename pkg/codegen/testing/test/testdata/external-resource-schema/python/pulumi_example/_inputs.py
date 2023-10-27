# coding=utf-8
# *** WARNING: this file was generated by test. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
import pulumi_random

__all__ = [
    'PetArgs',
]

@pulumi.input_type
class PetArgs:
    def __init__(__self__, *,
                 required_name: pulumi.Input['pulumi_random.RandomPet'],
                 required_name_array: pulumi.Input[Sequence[pulumi.Input['pulumi_random.RandomPet']]],
                 required_name_map: pulumi.Input[Mapping[str, pulumi.Input['pulumi_random.RandomPet']]],
                 age: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input['pulumi_random.RandomPet']] = None,
                 name_array: Optional[pulumi.Input[Sequence[pulumi.Input['pulumi_random.RandomPet']]]] = None,
                 name_map: Optional[pulumi.Input[Mapping[str, pulumi.Input['pulumi_random.RandomPet']]]] = None):
        pulumi.set(__self__, "required_name", required_name)
        pulumi.set(__self__, "required_name_array", required_name_array)
        pulumi.set(__self__, "required_name_map", required_name_map)
        if age is not None:
            pulumi.set(__self__, "age", age)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if name_array is not None:
            pulumi.set(__self__, "name_array", name_array)
        if name_map is not None:
            pulumi.set(__self__, "name_map", name_map)

    @property
    @pulumi.getter(name="requiredName")
    def required_name(self) -> pulumi.Input['pulumi_random.RandomPet']:
        return pulumi.get(self, "required_name")

    @required_name.setter
    def required_name(self, value: pulumi.Input['pulumi_random.RandomPet']):
        pulumi.set(self, "required_name", value)

    @property
    @pulumi.getter(name="requiredNameArray")
    def required_name_array(self) -> pulumi.Input[Sequence[pulumi.Input['pulumi_random.RandomPet']]]:
        return pulumi.get(self, "required_name_array")

    @required_name_array.setter
    def required_name_array(self, value: pulumi.Input[Sequence[pulumi.Input['pulumi_random.RandomPet']]]):
        pulumi.set(self, "required_name_array", value)

    @property
    @pulumi.getter(name="requiredNameMap")
    def required_name_map(self) -> pulumi.Input[Mapping[str, pulumi.Input['pulumi_random.RandomPet']]]:
        return pulumi.get(self, "required_name_map")

    @required_name_map.setter
    def required_name_map(self, value: pulumi.Input[Mapping[str, pulumi.Input['pulumi_random.RandomPet']]]):
        pulumi.set(self, "required_name_map", value)

    @property
    @pulumi.getter
    def age(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "age")

    @age.setter
    def age(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "age", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input['pulumi_random.RandomPet']]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input['pulumi_random.RandomPet']]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="nameArray")
    def name_array(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['pulumi_random.RandomPet']]]]:
        return pulumi.get(self, "name_array")

    @name_array.setter
    def name_array(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['pulumi_random.RandomPet']]]]):
        pulumi.set(self, "name_array", value)

    @property
    @pulumi.getter(name="nameMap")
    def name_map(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input['pulumi_random.RandomPet']]]]:
        return pulumi.get(self, "name_map")

    @name_map.setter
    def name_map(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input['pulumi_random.RandomPet']]]]):
        pulumi.set(self, "name_map", value)


