from trezor import strings, ui, utils
from trezor.messages import ButtonRequestType
from trezor.messages.ButtonAck import ButtonAck
from trezor.messages.ButtonRequest import ButtonRequest
from trezor.ui.text import Text

if False:
    from typing import List, Iterator, Union
    from trezor.wire import Context
    from trezor.ui import Component


async def naive_pagination(
    ctx: Context,
    lines: List[Union[str, int]],
    title: str,
    icon: str = ui.ICON_RESET,
    icon_color: int = ui.ORANGE,
    per_page: int = 5,
) -> bool:
    from trezor.ui.scroll import CANCELLED, CONFIRMED, PaginatedWithButtons

    pages = []  # type: List[Component]
    page_lines = paginate_lines(lines, per_page)

    for i, lines_on_page in enumerate(page_lines):
        if len(page_lines) > 1:
            paging = "%s/%s" % (i + 1, len(page_lines))
        else:
            paging = ""
        text = Text("%s %s" % (title, paging), icon, icon_color)
        text.normal(*lines_on_page)
        pages.append(text)

    paginated = PaginatedWithButtons(pages, one_by_one=True)

    while True:
        await ctx.call(ButtonRequest(code=ButtonRequestType.SignTx), ButtonAck)
        result = await ctx.wait(paginated)
        if result is CONFIRMED:
            return True
        if result is CANCELLED:
            return False


def paginate_lines(
    lines: List[Union[str, int]], lines_per_page: int = 5
) -> List[List[Union[int, str]]]:
    """Paginates lines across pages with preserving formatting modifiers (e.g., mono)"""
    pages = []
    cpage = []
    nlines = 0
    last_modifier = None
    for line in lines:
        cpage.append(line)
        if not isinstance(line, int):
            nlines += 1
        else:
            last_modifier = line

        if nlines >= lines_per_page:
            pages.append(cpage)
            cpage = []
            nlines = 0
            if last_modifier is not None:
                cpage.append(last_modifier)

    if nlines > 0:
        pages.append(cpage)
    return pages


def format_amount(value: int) -> str:
    return "%s XMR" % strings.format_amount(value, 12)


def split_address(address: str) -> Iterator[str]:
    return utils.chunks(address, 16)
