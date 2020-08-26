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
