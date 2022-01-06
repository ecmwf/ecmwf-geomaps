
from .. import macro
from ..action import action
from ._data import Data


class Grib(Data):
    
    @action(
        macro.mgrib,
        file_name="grib_input_file_name",
        index="grib_field_position",
        grib_id="grib_id",
        grib_mode="grib_file_address_mode",
    )
    def _get(self, *args, **kwargs):
        pass