from fastapi import status,Depends,APIRouter,HTTPException
import models
import schema
from database import get_db
from sqlalchemy.orm import Session
import oauth
router=APIRouter(
    prefix='/votes',
    tags=['Vote']
)
@router.post("/")
def vote_post(
    vote: schema.Vote,
    db: Session = Depends(get_db),
    current_user: int = Depends(oauth.get_current_user),
):
    post=db.query(models.POST).filter(models.POST.id==vote.post_id).first()
    if not post:
        raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Post with this id {vote.post_id} not found."
            )
    voter_post = db.query(models.Votes).filter(
        models.Votes.post_id == vote.post_id,
        models.Votes.user_id == current_user.id
    )
    found_vote = voter_post.first()

    if vote.dir == 1:  # Add vote
        if found_vote:
            raise HTTPException(
                status_code=status.HTTP_208_ALREADY_REPORTED,
                detail="You already voted for this post."
            )
        
        new_vote = models.Votes(post_id=vote.post_id, user_id=current_user.id)
        db.add(new_vote)
        db.commit()
        db.refresh(new_vote)
        return {"message": f"You successfully voted for post {vote.post_id}"}

    else:  # Remove vote
        if not found_vote:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Vote not found."
            )
        db.delete(found_vote)
        db.commit()
        return {"message": f"You successfully removed your vote for post {vote.post_id}"}
