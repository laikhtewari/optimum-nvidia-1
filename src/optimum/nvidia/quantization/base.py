from logging import getLogger
from typing import Iterable, Optional, Set, Tuple, Protocol, runtime_checkable

import numpy as np


LOGGER = getLogger(__name__)


@runtime_checkable
class SupportsWeightQuantization(Protocol):

    QUANTIZATION_EXCLUDED_PARAMETERS: Optional[Set[str]]

    @staticmethod
    @property
    def named_weight_parameters() -> Iterable[Tuple[str, np.array]]:
        ...



class SupportsWeightAndActivationQuantization(Protocol):
    pass


QUANTIZATION_PROTOCOLS = {SupportsWeightQuantization}
