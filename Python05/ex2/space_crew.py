from enum import Enum
from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import datetime


class Rank(Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=2, max_length=50)
    rank: Rank
    age: int = Field(..., ge=18, le=80)
    specialization: str = Field(..., min_length=3, max_length=30)
    years_experience: int = Field(..., ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(..., min_length=5, max_length=15)
    mission_name: str = Field(..., min_length=3, max_length=100)
    destination: str = Field(..., min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(..., ge=1, le=3650)
    crew: list[CrewMember] = Field(..., min_length=1, max_length=12)
    mission_status: str = Field(default="Planned")
    budget_million: float = Field(..., ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def mission_validation(self) -> "SpaceMission":
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")
        leader = False
        for member in self.crew:
            if member.rank == Rank.captain or member.rank == Rank.commander:
                leader = True
                break
        if not leader:
            raise ValueError("Must have at least"
                             " one Commander or Captain")
        experienced_crew = 0
        for member in self.crew:
            if member.years_experience >= 5:
                experienced_crew += 1
        if experienced_crew < len(self.crew) / 2 and self.duration_days > 365:
            raise ValueError("Long missions (> 365 days) need"
                             " 50% experienced crew (5+ years)")
        all_active = True
        for member in self.crew:
            if not member.is_active:
                all_active = False
                break
        if not all_active:
            raise ValueError("All crew members must be active")
        return self


def main() -> None:
    print("Space Mission Crew Validation")
    print("=========================================")
    member1 = CrewMember(
        member_id="1aa",
        name="Sarah Cannor",
        rank=Rank.commander,
        age=60,
        specialization="Mission Command",
        years_experience=20
    )
    member2 = CrewMember(
        member_id="2aa",
        name="John Smith",
        rank=Rank.lieutenant,
        age=50,
        specialization="Navigation",
        years_experience=5
    )
    member3 = CrewMember(
        member_id="3aa",
        name="Alice Johnson",
        rank=Rank.officer,
        age=40,
        specialization="Engineering",
        years_experience=4
    )
    try:
        valid_mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime(2024, 11, 11, 11, 11),
            duration_days=900,
            crew=[member1, member2, member3],
            budget_million=2500.0
        )
        print("Valid mission created:")
        print(f"Mission: {valid_mission.mission_name}")
        print(f"ID: {valid_mission.mission_id}")
        print(f"Destination: {valid_mission.destination}")
        print(f"Duration: {valid_mission.duration_days} days")
        print(f"Budget: ${valid_mission.budget_million}M")
        print(f"Crew size: {len(valid_mission.crew)}")
        print("Crew members:")
        for member in valid_mission.crew:
            print(f"- {member.name} ({member.rank}) - {member.specialization}")
    except ValidationError as e:
        print(e.errors()[0]["msg"].split(',')[1])
    print("\n=========================================")
    print("Expected validation error:")
    member4 = CrewMember(
        member_id="1aa",
        name="Sarah Cannor",
        rank=Rank.officer,
        age=60,
        specialization="Mission Command",
        years_experience=20
    )
    member5 = CrewMember(
        member_id="2aa",
        name="John Smith",
        rank=Rank.lieutenant,
        age=50,
        specialization="Navigation",
        years_experience=5
    )
    member6 = CrewMember(
        member_id="3aa",
        name="Alice Johnson",
        rank=Rank.officer,
        age=40,
        specialization="Engineering",
        years_experience=4
    )
    try:
        invalid_mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime(2024, 11, 11, 11, 11),
            duration_days=900,
            crew=[member4, member5, member6],
            budget_million=2500.0
        )
        print(invalid_mission)
    except ValidationError as e:
        print(e.errors()[0]["msg"].split(',')[1])


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
