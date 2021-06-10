from trezor.messages import SymbolTransactionCommon, SymbolSecretLock, SymbolSecretProof

from trezor import ui
from trezor.messages import (
    ButtonRequestType,
)
from trezor.ui.components.tt.text import Text

from apps.common.confirm import require_confirm



async def ask_secret_lock(
    ctx,
    common: SymbolTransactionCommon,
    lock: SymbolSecretLock,
):
    msg = Text("Secret lock", ui.ICON_SEND, ui.GREEN)
    
    msg.normal("Recipient: %s" % lock.recipient)
    msg.normal("Mosaic ID: %s" % lock.mosaic.id)
    msg.normal("Hash algo: %s" % lock.hash_algorithm)
    msg.normal("Max fee: %s"   % common.max_fee)

    await require_confirm( ctx, msg, ButtonRequestType.ConfirmOutput )



async def ask_secret_proof(
    ctx,
    common: SymbolTransactionCommon,
    lock: SymbolSecretProof,
):
    msg = Text("Secret proof", ui.ICON_SEND, ui.GREEN)
    
    msg.normal("Recipient: %s" % lock.recipient)
    msg.normal("Hash algo: %s" % lock.hash_algorithm)
    msg.normal("Max fee: %s"   % common.max_fee)

    await require_confirm( ctx, msg, ButtonRequestType.ConfirmOutput )



