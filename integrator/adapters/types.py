from __future__ import annotations

from typing import Dict, Any, Callable, Awaitable

AdapterEntity = Dict
AdapterContext = Any
AdapterProcessorIn = Callable[[AdapterContext], Awaitable]
AdapterProcessorOut = Callable[[AdapterContext, AdapterEntity], Awaitable]
AdapterProcessorFunc = AdapterProcessorIn | AdapterProcessorOut
