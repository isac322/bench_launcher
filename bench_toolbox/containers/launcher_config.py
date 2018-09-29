# coding: UTF-8

from dataclasses import dataclass
from pathlib import Path
from typing import Tuple

from .base_config import BaseConfig


@dataclass(frozen=True)
class LauncherConfig(BaseConfig):
    post_scripts: Tuple[Path]
    hyper_threading: bool
    stops_with_the_first: bool