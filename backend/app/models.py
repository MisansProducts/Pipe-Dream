from pydantic import BaseModel
from typing import List, Optional, Any, Union
from datetime import datetime

class CityReading(BaseModel):
    city: str
    timestamp: Union[str, datetime, None]
    features: Optional[List[Any]] = None
    timezone: Optional[str] = None
