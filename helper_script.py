from blog import db, create_app

app = create_app()
app.app_context().push()

from blog.models import User, Role, UserRoles
tk = User.query.get(1)