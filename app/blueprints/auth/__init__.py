from app import login_manager
from app.models.user import User


@login_manager.user_loader
def load_user(user_id):
    user = (
        User.query
        .filter(User.id == user_id)
        .first()
    )
    return user
