from dataclasses import dataclass
from typing import Optional, Callable

@dataclass
class Fail:
    msg: str
    exception: Optional[Exception]

def Result(t: type):
    return t | Fail


@dataclass
class Function:
    name: str
    func: Callable

@dataclass
class Sample:
    name: str
    data: any