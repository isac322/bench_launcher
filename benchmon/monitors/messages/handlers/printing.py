# coding: UTF-8

from __future__ import annotations

from typing import Optional, TYPE_CHECKING, TypeVar

from .base import BaseHandler

if TYPE_CHECKING:
    from .. import MonitoredMessage
    from .... import Context

_MT = TypeVar('_MT')


class PrintHandler(BaseHandler):
    """
    전달되는 모든 메시지를 ``stdout`` 으로 출력하고, 메시지를 그대로 다음 핸들러에게 전달하는 핸들러.

    .. note::

        디버깅용이기 때문에, 로깅에 사용하지 않는다.
    """

    async def on_message(self, context: Context, message: MonitoredMessage[_MT]) -> Optional[MonitoredMessage[_MT]]:
        print({'data': message.data, 'src': type(message.source).__name__})
        return message
