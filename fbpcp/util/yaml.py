#!/usr/bin/env python3
# Copyright (c) Meta Platforms, Inc. and affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

# pyre-strict

from pathlib import Path
from typing import Any, Dict

import yaml


def load(file_path: Path) -> Dict[str, Any]:
    with open(file_path) as stream:
        return yaml.safe_load(stream)


def dump(data: Dict[str, Any], file_path: Path) -> None:
    with open(file_path, "w") as f:
        return yaml.dump(data, f)
