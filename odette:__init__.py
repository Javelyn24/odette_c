"""
ODETTE Project - Satellite Tracking Core Library

This package provides Python bindings for the C++ core library of the ODETTE project,
which implements satellite tracking, orbit determination, and propagation functionality.
"""

# Import the C++ extension module
try:
    from .satellite_core import *
except ImportError:
    import warnings
    warnings.warn(
        "Failed to import the satellite_core C++ extension. "
        "The package might not be properly installed or was built incorrectly."
    )

__version__ = '0.1.0'
