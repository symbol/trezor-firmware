from micropython import const

from trezor import ui
from trezor.messages import BackupType
from trezor.ui.text import Text

from ..button import ButtonDefault
from ..confirm import DEFAULT_CONFIRM

if False:
    from typing import Iterable, Optional
    from ..button import ButtonContent
    from trezor.messages.ResetDevice import EnumTypeBackupType


def layout_reset_device_warning(
    backup_type: EnumTypeBackupType = BackupType.Bip39,
) -> Text:
    text = Text("Create new wallet", ui.ICON_RESET, new_lines=False)
    if backup_type == BackupType.Slip39_Basic:
        text.bold("Create a new wallet")
        text.br()
        text.bold("with Shamir Backup?")
    elif backup_type == BackupType.Slip39_Advanced:
        text.bold("Create a new wallet")
        text.br()
        text.bold("with Super Shamir?")
    else:
        text.bold("Do you want to create")
        text.br()
        text.bold("a new wallet?")

    text.br()
    text.br_half()
    text.normal("By continuing you agree")
    text.br()
    text.normal("to")
    text.bold("https://trezor.io/tos")

    return text


RESET_DEVICE_WARNING_CONFIRM = DEFAULT_CONFIRM  # type: ButtonContent


def layout_confirm_backup1() -> Text:
    # First prompt
    text = Text("Success", ui.ICON_CONFIRM, ui.GREEN, new_lines=False)
    text.bold("New wallet created")
    text.br()
    text.bold("successfully!")
    text.br()
    text.br_half()
    text.normal("You should back up your")
    text.br()
    text.normal("new wallet right now.")

    return text


def layout_confirm_backup2() -> Text:
    # If the user selects Skip, ask again
    text = Text("Warning", ui.ICON_WRONG, ui.RED, new_lines=False)
    text.bold("Are you sure you want")
    text.br()
    text.bold("to skip the backup?")
    text.br()
    text.br_half()
    text.normal("You can back up your")
    text.br()
    text.normal("Trezor once, at any time.")

    return text


CONFIRM_BACKUP_CANCEL = "Skip"  # type: ButtonContent
CONFIRM_BACKUP_CONFIRM = "Back up"  # type: ButtonContent


def confirm_path_warning(path_lines: Iterable[str]) -> Text:
    text = Text("Confirm path", ui.ICON_WRONG, ui.RED)
    text.normal("Path")
    text.mono(*path_lines)
    text.normal("is unknown.")
    text.normal("Are you sure?")

    return text


QR_X = const(120)
QR_Y = const(115)
QR_SIZE_THRESHOLD = const(63)


def qr_coef(datalen: int) -> int:
    return const(4) if datalen < QR_SIZE_THRESHOLD else const(3)


SHOW_QR_CONFIRM = DEFAULT_CONFIRM
SHOW_QR_CANCEL = "Address"
SHOW_QR_CANCEL_STYLE = ButtonDefault

SHOW_ADDRESS_CONFIRM = DEFAULT_CONFIRM
SHOW_ADDRESS_CANCEL = "QR"
SHOW_ADDRESS_CANCEL_STYLE = ButtonDefault


def layout_show_qr(desc: str) -> Text:
    return Text(desc, ui.ICON_RECEIVE, ui.GREEN)


def layout_show_address(
    desc: str, address: Iterable[str], network: Optional[str]
) -> Text:
    text = Text(desc, ui.ICON_RECEIVE, ui.GREEN)
    if network is not None:
        text.normal("%s network" % network)
    text.mono(*address)

    return text
