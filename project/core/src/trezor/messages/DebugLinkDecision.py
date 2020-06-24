# Automatically generated by pb2py
# fmt: off
import protobuf as p

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
        EnumTypeDebugSwipeDirection = Literal[0, 1, 2, 3]
    except ImportError:
        pass


class DebugLinkDecision(p.MessageType):
    MESSAGE_WIRE_TYPE = 100

    def __init__(
        self,
        yes_no: bool = None,
        swipe: EnumTypeDebugSwipeDirection = None,
        input: str = None,
        x: int = None,
        y: int = None,
        wait: bool = None,
    ) -> None:
        self.yes_no = yes_no
        self.swipe = swipe
        self.input = input
        self.x = x
        self.y = y
        self.wait = wait

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('yes_no', p.BoolType, 0),
            2: ('swipe', p.EnumType("DebugSwipeDirection", (0, 1, 2, 3)), 0),
            3: ('input', p.UnicodeType, 0),
            4: ('x', p.UVarintType, 0),
            5: ('y', p.UVarintType, 0),
            6: ('wait', p.BoolType, 0),
        }