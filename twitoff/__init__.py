from flask import Flask


from twitoff.models import db, migrate
from twitoff.routes.home_routes import home_routes
from twitoff.routes.book_routes import book_routes



DATABASE_URL = "sqlite:///twitoff_99.db"
#DATABASE_URL = "sqlite:////users/username/Desktop/your-repo-name/twitoff_99.db"
#DATABASE_URL = "sqlite:///C:\\users\\username\\Desktop\\your-repo-name\\twitoff_99.db" 



def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URL"] = DATABASE_URL
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(home_routes)
    app.register_blueprint(book_routes)
    return app


if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)
