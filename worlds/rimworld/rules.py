from typing import TYPE_CHECKING, Dict, Callable, Optional

from worlds.generic.Rules import set_rule, add_rule
from .locations import location_table, LocationDict
#from .options import AggressiveScanLogic, SwimRule
import math

if TYPE_CHECKING:
    from . import RimWorldWorld
    from BaseClasses import CollectionState, Location