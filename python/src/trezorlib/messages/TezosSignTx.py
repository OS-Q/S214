# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

from .TezosBallotOp import TezosBallotOp
from .TezosDelegationOp import TezosDelegationOp
from .TezosOriginationOp import TezosOriginationOp
from .TezosProposalOp import TezosProposalOp
from .TezosRevealOp import TezosRevealOp
from .TezosTransactionOp import TezosTransactionOp

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class TezosSignTx(p.MessageType):
    MESSAGE_WIRE_TYPE = 152

    def __init__(
        self,
        *,
        branch: bytes,
        address_n: List[int] = None,
        reveal: TezosRevealOp = None,
        transaction: TezosTransactionOp = None,
        origination: TezosOriginationOp = None,
        delegation: TezosDelegationOp = None,
        proposal: TezosProposalOp = None,
        ballot: TezosBallotOp = None,
    ) -> None:
        self.address_n = address_n if address_n is not None else []
        self.branch = branch
        self.reveal = reveal
        self.transaction = transaction
        self.origination = origination
        self.delegation = delegation
        self.proposal = proposal
        self.ballot = ballot

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('address_n', p.UVarintType, p.FLAG_REPEATED),
            2: ('branch', p.BytesType, p.FLAG_REQUIRED),
            3: ('reveal', TezosRevealOp, None),
            4: ('transaction', TezosTransactionOp, None),
            5: ('origination', TezosOriginationOp, None),
            6: ('delegation', TezosDelegationOp, None),
            7: ('proposal', TezosProposalOp, None),
            8: ('ballot', TezosBallotOp, None),
        }
