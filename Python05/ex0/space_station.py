from datetime import datetime
from pydantic import BaseModel, ValidationError, Field
from typing import Optional


class SpaceStation(BaseModel):
    station_id: str = Field(..., max_length=10, min_length=3)
    name: str = Field(..., max_length=50, min_length=1)
    crew_size: int = Field(..., ge=1, le=20)
    power_level: float = Field(..., ge=0.0, le=100.0)
    oxygen_level: float = Field(..., ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = Field(True)
    notes: Optional[str] = Field(default=None, max_length=200)


def main() -> None:
    print("Space Station Data Validation")
    print("========================================")
    station = SpaceStation(
        station_id="ISS001",
        name="International Space Station",
        crew_size=6,
        power_level=85.5,
        oxygen_level=92.3,
        last_maintenance=datetime(2000, 11, 16, 11, 16),
        is_operational=True)
    print("Valid station created:")
    print(f"ID: {station.station_id}")
    print(f"Name: {station.name}")
    print(f"Crew: {station.crew_size} people")
    print(f"Power: {station.power_level}%")
    print(f"Oxygen: {station.oxygen_level}")
    if station.is_operational:
        print("Status: operational")
    else:
        print("Status: not operational")
    print("\n========================================")
    print("Expected validation error:")
    try:
        invalid_station = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=26,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime(2000, 11, 16, 11, 16),
            is_operational=True)
        print(invalid_station)
    except ValidationError as e:
        print(e.errors()[0]["msg"])


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
