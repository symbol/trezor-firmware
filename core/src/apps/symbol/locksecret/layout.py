from trezor.messages.SymbolSecretProof import SymbolSecretProof
from trezor.messages.SymbolHeader import SymbolHeader
from trezor.messages.SymbolSecretLock import SymbolSecretLock

from trezor import ui
from trezor.messages import (
    ButtonRequestType,
)
from trezor.ui.components.tt.text import Text

from apps.common.confirm import require_confirm

from .. import common_layout


def int_to_hash_algo( idx : int ):
    int_to_str = ["Op_Sha3_256", "Op_Hash_160", "Op_Hash_256"]
    return int_to_str[idx]



async def ask_secret_lock(
    ctx,
    header: SymbolHeader,
    lock: SymbolSecretLock,
):
    msg = Text("Secret lock", ui.ICON_SEND, ui.GREEN)    
    msg.normal("Recipient: %s" % lock.recipient)
    await require_confirm( ctx, msg, ButtonRequestType.ConfirmOutput )

    msg = Text("Fields", ui.ICON_SEND, ui.GREEN)    
    msg.normal("Mosaic ID: %s" % lock.mosaic.id)
    msg.normal("Hash algo: %s" % int_to_hash_algo(lock.hash_algorithm))
    await require_confirm( ctx, msg, ButtonRequestType.ConfirmOutput )

    await common_layout.require_confirm_final(ctx, header)



async def ask_secret_proof(
    ctx,
    header: SymbolHeader,
    lock: SymbolSecretProof,
):
    msg = Text("Secret proof", ui.ICON_SEND, ui.GREEN)
    
    msg.normal("Recipient: %s" % lock.recipient)
    await require_confirm( ctx, msg, ButtonRequestType.ConfirmOutput )

    msg = Text("Fields", ui.ICON_SEND, ui.GREEN)    
    msg.normal("Hash algo: %s" % int_to_hash_algo(lock.hash_algorithm))
    await require_confirm( ctx, msg, ButtonRequestType.ConfirmOutput )

    await common_layout.require_confirm_final(ctx, header)



