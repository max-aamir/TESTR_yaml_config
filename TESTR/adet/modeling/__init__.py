# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved
from .transformer_detector import TransformerDetector

_EXCLUDE = {"torch", "ShapeSpec"}
__all__ = [k for k in globals().keys() if k not in _EXCLUDE and not k.startswith("_")]
print("___________________in adet/modelling/__init__.py _________")