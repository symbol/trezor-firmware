from trezor import wire


class Error(wire.DataError):
    pass


class ChangeAddressError(wire.DataError):
    pass


class NotEnoughOutputsError(wire.DataError):
    pass


class RctType:
    """
    There are two types of monero Ring Confidential Transactions:
    1. RCTTypeFull = 1 (used if num_inputs == 1)
    2. RCTTypeSimple = 2 (for num_inputs > 1)
    3. Bulletproof2 = 4, HF11+

    There is actually also RCTTypeNull but we ignore that one.
    """

    Bulletproof2 = 4
