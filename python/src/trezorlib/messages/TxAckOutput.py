# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

from .TxAckOutputWrapper import TxAckOutputWrapper

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class TxAckOutput(p.MessageType):
    MESSAGE_WIRE_TYPE = 22

    def __init__(
        self,
        *,
        tx: TxAckOutputWrapper,
    ) -> None:
        self.tx = tx

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('tx', TxAckOutputWrapper, p.FLAG_REQUIRED),
        }
