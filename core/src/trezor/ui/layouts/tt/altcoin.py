from trezor import ui, wire
from trezor.messages import ButtonRequestType
from trezor.utils import chunks_intersperse

from ...components.common.confirm import raise_if_cancelled
from ...components.tt.confirm import Confirm, HoldToConfirm
from ...components.tt.scroll import Paginated
from ...components.tt.text import Text
from ...constants.tt import MONO_ADDR_PER_LINE
from ..common import interact

if False:
    from typing import Sequence


async def confirm_total_ethereum(
    ctx: wire.GenericContext, total_amount: str, gas_price: str, fee_max: str
) -> None:
    text = Text("Confirm transaction", ui.ICON_SEND, ui.GREEN, new_lines=False)
    text.bold(total_amount)
    text.normal(" ", ui.GREY, "Gas price:", ui.FG)
    text.bold(gas_price)
    text.normal(" ", ui.GREY, "Maximum fee:", ui.FG)
    text.bold(fee_max)
    await raise_if_cancelled(
        interact(ctx, HoldToConfirm(text), "confirm_total", ButtonRequestType.SignTx)
    )


async def confirm_total_ripple(
    ctx: wire.GenericContext,
    address: str,
    amount: str,
) -> None:
    title = "Confirm sending"
    text = Text(title, ui.ICON_SEND, ui.GREEN, new_lines=False)
    text.bold("{} XRP\n".format(amount))
    text.normal("to\n")
    text.mono(*chunks_intersperse(address, MONO_ADDR_PER_LINE))

    await raise_if_cancelled(
        interact(ctx, HoldToConfirm(text), "confirm_output", ButtonRequestType.SignTx)
    )


async def confirm_timebounds_stellar(
    ctx: wire.GenericContext, start: int, end: int
) -> None:
    text = Text("Confirm timebounds", ui.ICON_SEND, ui.GREEN)
    text.bold("Valid from (UTC):")
    if start:
        text.normal(str(start))
    else:
        text.mono("[no restriction]")

    text.bold("Valid to (UTC):")
    if end:
        text.normal(str(end))
    else:
        text.mono("[no restriction]")

    await raise_if_cancelled(
        interact(
            ctx, Confirm(text), "confirm_timebounds", ButtonRequestType.ConfirmOutput
        )
    )


async def confirm_proposals_tezos(
    ctx: wire.GenericContext, proposals: Sequence[str]
) -> None:
    if len(proposals) > 1:
        title = "Submit proposals"
    else:
        title = "Submit proposal"

    pages: list[ui.Component] = []
    for page, proposal in enumerate(proposals):
        text = Text(title, ui.ICON_SEND, icon_color=ui.PURPLE, new_lines=False)
        text.bold("Proposal {}:\n".format(page + 1))
        text.mono(*chunks_intersperse(proposal, 17))
        pages.append(text)

    pages[-1] = Confirm(pages[-1])
    paginated = Paginated(pages)

    await raise_if_cancelled(
        interact(ctx, paginated, "confirm_proposals", ButtonRequestType.SignTx)
    )


async def confirm_transfer_binance(
    ctx: wire.GenericContext, inputs_outputs: Sequence[tuple[str, str, str]]
) -> None:
    pages: list[ui.Component] = []
    for title, amount, address in inputs_outputs:
        coin_page = Text(title, ui.ICON_SEND, icon_color=ui.GREEN, new_lines=False)
        coin_page.bold(amount)
        coin_page.normal("\nto\n")
        coin_page.mono(*chunks_intersperse(address, MONO_ADDR_PER_LINE))
        pages.append(coin_page)

    pages[-1] = HoldToConfirm(pages[-1])

    await raise_if_cancelled(
        interact(
            ctx, Paginated(pages), "confirm_transfer", ButtonRequestType.ConfirmOutput
        )
    )


async def confirm_decred_sstx_submission(
    ctx: wire.GenericContext,
    address: str,
    amount: str,
) -> None:
    text = Text("Purchase ticket", ui.ICON_SEND, ui.GREEN, new_lines=False)
    text.normal(amount)
    text.normal("\nwith voting rights to\n")
    text.mono(*chunks_intersperse(address, MONO_ADDR_PER_LINE))
    await raise_if_cancelled(
        interact(
            ctx,
            Confirm(text),
            "confirm_decred_sstx_submission",
            ButtonRequestType.ConfirmOutput,
        )
    )
