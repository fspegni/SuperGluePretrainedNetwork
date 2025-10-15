# SuperGluePretrainedNetwork.py
"""
Shim module to expose the existing 'models' package
under the 'SuperGluePretrainedNetwork' namespace.

This allows:
    import SuperGluePretrainedNetwork
    from SuperGluePretrainedNetwork import models
    from SuperGluePretrainedNetwork.models.superglue import SuperGlue
"""

import importlib
import sys

# import the real package
_models = importlib.import_module("models")

# register it as a submodule of this package name
sys.modules[__name__ + ".models"] = _models

__all__ = ["models"]

