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
from models.entry import Entry
from models.relay_entry import RelayEntry
from models.relay_member import RelayMember
from models.heat_result import HeatResult
from models.official_result import OfficialResult

from schemas.meet import MeetResp, MeetCreate
from schemas.result import ResultUpdate
from schemas.team import TeamResp, TeamCreate
from schemas.athlete import AthleteResp, AthleteCreate
from schemas.entry import EntryResp, EntryCreate
from schemas.relay_entry import RelayEntryResp, RelayEntryCreate
from schemas.relay_member import RelayMemberResp, RelayMemberCreate

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

@app.get("/meet")
async def get_meet(meetname: str, db: Session = Depends(get_db)):
    meet = db.query(Meet).options(joinedload(Meet.events)).filter(Meet.meetname == meetname).first()
    if meet is not None:
        return {"status": "Success",
                "data": meet}
    else:
        # Return 404
        raise HTTPException(status_code=404, detail="Meet not found")


@app.get("/meet/{id}")
async def get_meet(id: int, db: Session = Depends(get_db)):
    meet = db.query(Meet).options(joinedload(Meet.events)).filter(Meet.meet_id == id).first()
    return {"status": "Success",
            "data": meet}

@app.post("/meet")
async def create_meet(meet: MeetCreate, db: Session = Depends(get_db)):

    if meet.stub is None or meet.stub == "":
        stub = meet.stub
    else:
        stub = ""

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
        stub=stub,
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
                program_number=str(event.program_number),
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


@app.get("/teams")
async def get_teams(db: Session = Depends(get_db)):
    teams = db.query(Team).options(joinedload(Team.members)).all()
    return {"status": "Success",
            "data": teams}


@app.post("/teams")
async def create_teams(teams: list[TeamCreate], db: Session = Depends(get_db)):

    # Create Team item
    create_dt = datetime.datetime.now()

    team_ids = []

    for team in teams:
        db_team = Team(
            team_id=team.team_id,
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
                surname=athlete.surname,
                first_name=athlete.first_name,
                other_names=athlete.other_names,
                preferred_name=athlete.preferred_name,
                sex=athlete.sex,
                dob=datetime.datetime.strptime(athlete.dob, '%Y-%m-%d').date(),
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

    print('my')

    return db.query(Unit).all()

# Add athlete
@app.post("/athletes")
async def create_athletes(athletes: list[AthleteCreate], db: Session = Depends(get_db)):
    create_dt = datetime.datetime.now()

    added_athletes = []

    for athlete in athletes:
        db_athlete = Athlete(
            surname=athlete.surname,
            first_name=athlete.first_name,
            other_names=athlete.other_names,
            preferred_name=athlete.preferred_name,
            sex=athlete.sex,
            dob=datetime.datetime.strptime(athlete.dob, '%Y-%m-%d').date(),
            age=athlete.age,
            member_number=athlete.member_number,
            team_id=athlete.team_id,
            updated_at=create_dt,
            created_at=create_dt
        )

        db.add(db_athlete)
        added_athletes.append(db_athlete)

    db.commit()
    for athlete in added_athletes:
        db.refresh(athlete)

    return {
        "status": "Success",
        "data": added_athletes
    }

@app.get("/meet/{meet_id}/entries")
def get_meet_entries(meet_id: int, db: Session = Depends(get_db)):
    entries = db.query(Entry).filter(Entry.meet_id == meet_id).all()
    return {"status": "Success",
            "data": entries}

@app.post("/meet/{meet_id}/entries")
def create_meet_entries(meet_id: int, entries: list[EntryCreate], db: Session = Depends(get_db)):
    create_dt = datetime.datetime.now()

    added_entries = []

    for entry in entries:
        db_entry = Entry(
            meet_id=meet_id,
            athlete_id=entry.athlete_id,
            program_number=entry.program_number,
            seed_time=entry.seed_time,
            scratched=entry.scratched,
            status_code=entry.status_code,
            updated_at=create_dt,
            created_at=create_dt
        )

        db.add(db_entry)
        added_entries.append(db_entry)

    db.commit()
    for entry in added_entries:
        db.refresh(entry)

    return {
        "status": "Success",
        "data": added_entries
    }

@app.post("/meet/{meet_id}/relays")
def create_meet_relays(meet_id: int, relays: list[RelayEntryCreate], db: Session = Depends(get_db)):
    create_dt = datetime.datetime.now()

    added_relays = []
    added_relay_ids = []

    for relay in relays:
        db_relay = RelayEntry(
            meet_id=meet_id,
            program_number=relay.program_number,
            team_id=relay.team_id,
            organisation_id=relay.organisation_id,
            seed_time=relay.seed_time,
            letter=relay.letter,
            team_name=relay.team_name,
            scratched=relay.scratched,
            status_code=relay.status_code,
            updated_at=create_dt,
            created_at=create_dt
        )

        db.add(db_relay)
        added_relays.append(db_relay)

    db.commit()
    for added_relay in added_relays:
        db.refresh(added_relay)
        added_relay_ids.append(added_relay.relay_entry_id)

        # Find this relay in the array
        for relay in relays:
            if relay.program_number == added_relay.program_number and relay.team_id == added_relay.team_id \
                and relay.organisation_id == added_relay.organisation_id and relay.letter == added_relay.letter:

                # Add the relay members
                for relay_member in relay.members:
                    db_relay_member = RelayMember(
                        relay_entry_id=added_relay.relay_entry_id,
                        leg=relay_member.leg,
                        athlete_id=relay_member.athlete_id,
                        updated_at=create_dt,
                        created_at=create_dt
                    )

                    db.add(db_relay_member)

                break

    db.commit()

    pprint(added_relay_ids)

    added_relays = db.query(RelayEntry).options(joinedload(RelayEntry.members)).filter(RelayEntry.relay_entry_id in added_relay_ids).all()

    return {
        "status": "Success",
        "data": added_relays
    }

@app.put("/meet/{meet_id}/results")
def update_results(meet_id: int, results: list[ResultUpdate], db: Session = Depends(get_db)):
    create_dt = datetime.datetime.now()
    update_dt = create_dt

    entry_ids = []
    for result in results:
        entry_ids.append(result.entry_id)

    # Get any existing Official Results
    existing_results = db.query(OfficialResult).filter(OfficialResult.entry_id.in_(entry_ids)).all()

    # Get entries for these
    entries = db.query(Entry).filter(Entry.entry_id.in_(entry_ids)).all()

    for result in results:
        if 'final_result' in result and result.final_result is not None:

            final_result = result.final_result

            # Check if a result with the same entry_id is in existing_results
            existing_result = next((x for x in existing_results if x.entry_id == result.entry_id), None)

            # Get the entry for this result
            entry = next((x for x in entries if x.entry_id == result.entry_id), None)
            if entry is None:
                # TODO: handle this better
                raise HTTPException(status_code=404, detail="Entry not found")

            if existing_result is not None:
                # Update the existing result
                if 'seconds' in final_result:
                    if existing_result.seconds != final_result.seconds:
                        existing_result.seconds = final_result.seconds
                        existing_result.updated_at = update_dt
                        db.add(existing_result)
            else:

                if 'seconds' in final_result:
                    seconds = final_result.seconds
                else:
                    seconds = None

                # Create a new result
                # TODO: handle distance results
                db_result = OfficialResult(
                    entry_id=result.entry_id,
                    meet_id=meet_id,
                    program_number=entry.program_number,
                    age_group_code=entry.age_group_code,
                    seconds=seconds,
                    updated_at=update_dt,
                    created_at=create_dt
                )

                db.add(db_result)


    updated_results = existing_results

    # Do this here so everything works or nothing does
    db.commit()


    return {
        "status": "Success",
        "data": updated_results
    }

