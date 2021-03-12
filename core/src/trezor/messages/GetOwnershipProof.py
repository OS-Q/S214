# Automatically generated by pb2py
# fmt: off
import protobuf as p

from .MultisigRedeemScriptType import MultisigRedeemScriptType

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
        EnumTypeInputScriptType = Literal[0, 1, 2, 3, 4]
    except ImportError:
        pass


class GetOwnershipProof(p.MessageType):
    MESSAGE_WIRE_TYPE = 49

    def __init__(
        self,
        *,
        address_n: List[int] = None,
        ownership_ids: List[bytes] = None,
        coin_name: str = "Bitcoin",
        script_type: EnumTypeInputScriptType = 3,
        multisig: MultisigRedeemScriptType = None,
        user_confirmation: bool = False,
        commitment_data: bytes = b"",
    ) -> None:
        self.address_n = address_n if address_n is not None else []
        self.ownership_ids = ownership_ids if ownership_ids is not None else []
        self.coin_name = coin_name
        self.script_type = script_type
        self.multisig = multisig
        self.user_confirmation = user_confirmation
        self.commitment_data = commitment_data

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('address_n', p.UVarintType, p.FLAG_REPEATED),
            2: ('coin_name', p.UnicodeType, "Bitcoin"),  # default=Bitcoin
            3: ('script_type', p.EnumType("InputScriptType", (0, 1, 2, 3, 4)), 3),  # default=SPENDWITNESS
            4: ('multisig', MultisigRedeemScriptType, None),
            5: ('user_confirmation', p.BoolType, False),  # default=false
            6: ('ownership_ids', p.BytesType, p.FLAG_REPEATED),
            7: ('commitment_data', p.BytesType, b""),  # default=
        }
