"""Data test.

Test data is discovered by glob from ``tests/data/{valid,invalid}/``. Each
filename must follow the convention ``<ClassName>-<description>.yaml``; the
stem prefix before the first ``-`` names the LinkML class to load against.
"""
import os
import glob
import pytest
from pathlib import Path

import fix_orchestra.datamodel.fix_orchestra
from linkml_runtime.loaders import yaml_loader

DATA_DIR_VALID = Path(__file__).parent / "data" / "valid"
DATA_DIR_INVALID = Path(__file__).parent / "data" / "invalid"

VALID_EXAMPLE_FILES = sorted(glob.glob(os.path.join(DATA_DIR_VALID, '*.yaml')))
INVALID_EXAMPLE_FILES = sorted(glob.glob(os.path.join(DATA_DIR_INVALID, '*.yaml')))


def _target_class(filepath: str):
    """Resolve the target dataclass from the filename stem prefix."""
    target_class_name = Path(filepath).stem.split("-")[0]
    return getattr(fix_orchestra.datamodel.fix_orchestra, target_class_name)


@pytest.mark.parametrize("filepath", VALID_EXAMPLE_FILES,
                         ids=[Path(p).name for p in VALID_EXAMPLE_FILES])
def test_valid_data_files(filepath):
    """Each file in ``tests/data/valid/`` must load cleanly."""
    obj = yaml_loader.load(filepath, target_class=_target_class(filepath))
    assert obj is not None


@pytest.mark.parametrize("filepath", INVALID_EXAMPLE_FILES,
                         ids=[Path(p).name for p in INVALID_EXAMPLE_FILES])
def test_invalid_data_files(filepath):
    """Each file in ``tests/data/invalid/`` must fail to load.

    The negative test asserts that ``yaml_loader.load`` raises an exception
    (typically ``ValueError`` for missing required fields, bad enum values, or
    type-coercion failures). A file that *succeeds* here indicates a hole in
    the schema's constraints and should be investigated.
    """
    with pytest.raises(Exception):
        yaml_loader.load(filepath, target_class=_target_class(filepath))
