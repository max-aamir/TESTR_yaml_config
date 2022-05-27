from detectron2.config import CfgNode


def get_cfg() -> CfgNode:
    """
    Get a copy of the default config.

    Returns:
        a detectron2 CfgNode instance.
    """
    from .defaults import _C
    print("___________________in adet/config/get_cfg()method___________________")
    return _C.clone()
