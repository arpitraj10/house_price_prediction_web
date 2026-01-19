from pydantic import BaseModel

class HouseInput(BaseModel):
    overall_qual: int
    gr_liv_area: int
    garage_cars: int
    total_bsmt_sf: int
    full_bath: int
    year_built: int
