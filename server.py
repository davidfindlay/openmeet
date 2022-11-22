from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session, sessionmaker, scoped_session, joinedload

from db.db import get_db
from models.base import Base
from models.unit import Unit
from models.meet import Meet
from models.meet_event import MeetEvent
from models.meet_event_type import MeetEventType, MeetEventTypeCache
from models.discipline import Discipline, DisciplineCache
from models.distance import Distance, DistanceCache
from models.team import Team
from models.athlete import Athlete

from schemas.meet import MeetResp, MeetCreate
from schemas.team import TeamResp, TeamCreate

from pprint import pprint
import datetime


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/meets/")
async def get_meets(db: Session = Depends(get_db)):
    meets = db.query(Meet).all()
    return {"status": "Success",
            "data": meets}


@app.get("/meets/{id}")
async def get_meet(id: int, db: Session = Depends(get_db)):
    meet = db.query(Meet).options(joinedload(Meet.events)).filter(Meet.meet_id == id).first()
    return {"status": "Success",
            "data": meet}


@app.post("/meet")
async def create_meet(meet: MeetCreate, db: Session = Depends(get_db)):

    # Create Meet item
    create_dt = datetime.datetime.now()
    db_meet = Meet(
        meetname=meet.meetname,
        startdate=meet.startdate,
        enddate=meet.enddate,
        deadline=meet.deadline,
        max_individual_events=meet.max_individual_events,
        max_relay_events=meet.max_relay_events,
        max_total_events=meet.max_total_events,
        age_up_date=meet.age_up_date,
        updated_at=create_dt,
        created_at=create_dt,
    )
    db.add(db_meet)
    db.commit()
    db.refresh(db_meet)

    # Check for events
    if meet.events and len(meet.events) > 0:
        for event in meet.events:
            meet_event_type_cache = MeetEventTypeCache()
            discipline_cache = DisciplineCache()
            distance_cache = DistanceCache()
            db_event = MeetEvent(
                meet_id=db_meet.meet_id,
                program_number=event.program_number,
                event_type=meet_event_type_cache[event.event_type],
                event_order=event.event_order,
                discipline=discipline_cache[event.discipline],
                distance=distance_cache[event.distance],
                legs=event.legs
            )

            db.add(db_event)
        db.commit()

    meet = db.query(Meet).options(joinedload(Meet.events)).filter(Meet.meet_id == db_meet.meet_id).first()
    return {
        "status": "Success",
        "data": meet
    }


@app.post("/meet/{meet_id}/teams")
async def create_teams(meet_id: int, teams: list[TeamCreate], db: Session = Depends(get_db)):

    # Create Team item
    create_dt = datetime.datetime.now()

    team_ids = []

    for team in teams:
        db_team = Team(
            team_id=team.team_id,
            meet_id=meet_id,
            team_name=team.team_name,
            abbreviation=team.abbreviation,
            updated_at=create_dt,
            created_at=create_dt
        )

        db.add(db_team)
        db.commit()
        db.refresh(db_team)
        team_ids.append(team.team_id)

        for athlete in team.members:
            db_athlete = Athlete(
                athlete_id=athlete.athlete_id,
                meet_id=meet_id,
                surname=athlete.surname,
                first_name=athlete.first_name,
                other_names=athlete.other_names,
                preferred_name=athlete.preferred_name,
                sex=athlete.sex,
                dob=datetime.datetime.strptime(athlete.dob, '%Y-%m-%d'),
                age=athlete.age,
                member_number=athlete.member_number,
                team_id=db_team.team_id,
                updated_at=create_dt,
                created_at=create_dt
            )

            db.add(db_athlete)

        db.commit()

    teams_return = db.query(Team).options(joinedload(Team.members)).filter(Team.team_id in team_ids).all()
    return {
        "status": "Success",
        "data": teams_return
    }


@app.get("/units/")
async def get_units(db: Session = Depends(get_db)):

    return db.query(Unit).all()

