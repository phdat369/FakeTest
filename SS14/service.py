from sqlalchemy.orm import Session
from model import WorldCup
from fastapi import HTTPException, status
def get_teams(db: Session):
    list_team = db.query(WorldCup).all()
    return list_team
def get_teams_by_id(db: Session, id_in: int):
    check_team_id = db.query(WorldCup).filter(WorldCup.id == id_in).first()
    if check_team_id:
        return {
            "message": "Information Team",
            "data": check_team_id
        }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="ID not Found"
    )
def 