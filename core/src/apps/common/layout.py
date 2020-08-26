from ubinascii import hexlify

from trezor import ui
from trezor.messages import ButtonRequestType
from trezor.ui.button import ButtonDefault
from trezor.ui.container import Container
from trezor.ui.model import layout as model
from trezor.ui.qr import Qr
from trezor.ui.scroll import Paginated
from trezor.ui.text import Text
from trezor.utils import chunks

from apps.common import HARDENED
from apps.common.confirm import confirm, require_confirm

if False:
    from typing import Iterable, Iterator, List
    from trezor import wire


async def show_address(
    ctx: wire.Context, address: str, desc: str = "Confirm address", network: str = None,
) -> bool:
    text = model.layout_show_address(desc, split_address(address), network)

    return await confirm(
        ctx,
        text,
        code=ButtonRequestType.Address,
        confirm=model.SHOW_ADDRESS_CONFIRM,
        cancel=model.SHOW_ADDRESS_CANCEL,
        cancel_style=model.SHOW_ADDRESS_CANCEL_STYLE,
    )


async def show_qr(
    ctx: wire.Context,
    address: str,
    desc: str = "Confirm address",
    cancel: str = model.SHOW_QR_CANCEL,
) -> bool:
    coef = model.qr_coef(len(address))
    qr = Qr(address, model.QR_X, model.QR_Y, coef)
    text = model.layout_show_qr(desc)
    content = Container(qr, text)

    return await confirm(
        ctx,
        content,
        code=ButtonRequestType.Address,
        confirm=model.SHOW_QR_CONFIRM,
        cancel=cancel,
        cancel_style=model.SHOW_QR_CANCEL_STYLE,
    )


async def show_pubkey(ctx: wire.Context, pubkey: bytes) -> None:
    lines = chunks(hexlify(pubkey).decode(), 18)
    text = Text("Confirm public key", ui.ICON_RECEIVE, ui.GREEN)
    text.mono(*lines)
    await require_confirm(ctx, text, ButtonRequestType.PublicKey)


async def show_xpub(ctx: wire.Context, xpub: str, desc: str, cancel: str) -> bool:
    pages = []  # type: List[ui.Component]
    for lines in chunks(list(chunks(xpub, 16)), 5):
        text = Text(desc, ui.ICON_RECEIVE, ui.GREEN)
        text.mono(*lines)
        pages.append(text)

    return await confirm(
        ctx,
        Paginated(pages),
        code=ButtonRequestType.PublicKey,
        cancel=cancel,
        cancel_style=ButtonDefault,
    )


def split_address(address: str) -> Iterator[str]:
    return chunks(address, 17)


def address_n_to_str(address_n: list) -> str:
    def path_item(i: int) -> str:
        if i & HARDENED:
            return str(i ^ HARDENED) + "'"
        else:
            return str(i)

    if not address_n:
        return "m"

    return "m/" + "/".join([path_item(i) for i in address_n])


async def show_warning(
    ctx: wire.GenericContext,
    content: Iterable[str],
    subheader: Iterable[str] = [],
    button: str = "Try again",
) -> None:
    text = Text("Warning", ui.ICON_WRONG, ui.RED)
    if subheader:
        for row in subheader:
            text.bold(row)
        text.br_half()
    for row in content:
        text.normal(row)
    await require_confirm(
        ctx, text, ButtonRequestType.Warning, confirm=button, cancel=None
    )


async def show_success(
    ctx: wire.GenericContext,
    content: Iterable[str] = [],
    subheader: Iterable[str] = [],
    button: str = "Continue",
) -> None:
    text = Text("Success", ui.ICON_CONFIRM, ui.GREEN)
    if subheader:
        for row in subheader:
            text.bold(row)
        text.br_half()
    for row in content:
        text.normal(row)
    await require_confirm(
        ctx, text, ButtonRequestType.Success, confirm=button, cancel=None
    )
