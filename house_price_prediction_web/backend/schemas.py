from pydantic import BaseModel

class HouseInput(BaseModel):
    overall_qual: int
    gr_liv_area: float
    garage_cars: int
    total_bsmt_sf: float
    year_built: int
