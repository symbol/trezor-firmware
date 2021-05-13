import trezorconfig as config  # noqa: F401
import trezorio as io  # noqa: F401
from trezorutils import MODEL

if False:
    import trezorio.fatfs as fatfs
else:
    if MODEL == "T":
        # a bug in mypy causes a crash at _usage site_ of the following:
        fatfs = io.fatfs
        # hence the if False branch that does what mypy understands - but which doesn't
        # actually work because `trezorio.fatfs` is not importable.
    else:
        fatfs = None  # type: ignore
