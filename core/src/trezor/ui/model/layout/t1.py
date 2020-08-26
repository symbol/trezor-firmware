from micropython import const

from trezor.messages import BackupType
from trezor.ui.text import Text

from ..button import ButtonCancel

if False:
    from typing import Iterable, Optional
    from ..button import ButtonContent, ButtonStyleType
    from trezor.messages.ResetDevice import EnumTypeBackupType


def layout_reset_device_warning(
    backup_type: EnumTypeBackupType = BackupType.Bip39,
) -> Text:
    assert backup_type == BackupType.Bip39

    text = Text("", "", new_lines=False)
    text.bold("Do you want to")
    text.br()
    text.bold("create a new wallet?")
    text.br()
    text.br_half()
    text.normal("By continuing you agree")
    text.br()
    text.normal("to")
    text.bold("trezor.io/tos")
    return text


RESET_DEVICE_WARNING_CONFIRM = "CREATE"  # type: ButtonContent


# no mockup
def layout_confirm_backup1() -> Text:
    text = Text("", "", new_lines=False)
    text.bold("New wallet created")
    text.br()
    text.bold("successfully!")
    text.br()
    text.br_half()
    text.normal("You should back up your")
    text.br()
    text.normal("new wallet right now.")

    return text


# no mockup
def layout_confirm_backup2() -> Text:
    text = Text("Skip the backup?", "", new_lines=False)
    text.normal("You can back up ", "your Trezor once, ", "at any time.")

    return text


CONFIRM_BACKUP_CANCEL = "NO"  # type: ButtonContent
CONFIRM_BACKUP_CONFIRM = "BACK UP"  # type: ButtonContent


def confirm_path_warning(path_lines: Iterable[str]) -> Text:
    text = Text("WRONG ADDRESS PATH", "")
    text.br_half()
    text.mono(*path_lines)
    text.br_half()
    text.normal("Are you sure?")

    return text


QR_X = const(32)
QR_Y = const(32)
QR_SIZE_THRESHOLD = const(43)


def qr_coef(datalen: int) -> int:
    return const(2) if datalen < QR_SIZE_THRESHOLD else const(1)


SHOW_QR_CONFIRM = "CONTINUE"  # type: ButtonContent
SHOW_QR_CANCEL = ""
SHOW_QR_CANCEL_STYLE = ButtonCancel  # type: ButtonStyleType

SHOW_ADDRESS_CONFIRM = "CONTINUE"  # type: ButtonContent
SHOW_ADDRESS_CANCEL = "QR CODE"  # type: ButtonContent
SHOW_ADDRESS_CANCEL_STYLE = ButtonCancel  # type: ButtonStyleType


def layout_show_qr(desc: str) -> Text:
    return Text("", "")


def layout_show_address(
    desc: str, address: Iterable[str], network: Optional[str]
) -> Text:
    text = Text(desc, "")
    assert network is None  # TODO
    # if network is not None:
    #    text.normal("%s network" % network)
    text.bold("Address:")
    text.mono(*address)

    return text
