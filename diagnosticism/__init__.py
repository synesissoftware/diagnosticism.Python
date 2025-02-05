
__author__      =   'Matt Wilson'
__copyright__   =   'Copyright 2019-2024, Synesis Information Systems, Copyright 2019, Synesis Software'
__credits__     =   [
        'Garth Lancaster',
        'Matt Wilson',
 ]
__email__       =   'matthew@synesis.com.au'
__license__     =   'BSD-3-Clause'
__maintainer__  =   'Matt Wilson'
__status__      =   'Beta'
__version__     =   '0.9.0'

from .contingent_reporting import abort, report
from .logging import (
    enable_logging,
    is_logging_enabled,
    is_severity_logged,
    log,
    set_log_filter,
)
from .program_name import *
from .severity import *
from .tracing import enable_tracing, is_tracing_enabled, trace
from .warning import warn

