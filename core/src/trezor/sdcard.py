from trezorutils import MODEL

if MODEL == "T":
    from .sdcard_tt import *  # noqa: F401,F403
else:
    if False:
        from typing import Any, NoReturn

    def filesystem(mounted: Any) -> NoReturn:  # type: ignore
        raise NotImplementedError

    def with_filesystem(func: Any) -> Any:  # type: ignore
        def wrapped_func(*args, **kwargs) -> NoReturn:  # type: ignore
            raise NotImplementedError

        return wrapped_func

    def is_present() -> bool:
        return False

    def capacity() -> NoReturn:
        raise NotImplementedError
