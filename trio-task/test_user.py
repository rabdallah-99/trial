from flask_testing import TestCase
class TestBase(TestCase):
    def create_app(self):
        config_name = "Testing"

        # Pass in testing configurations for the app.
        # Here we use sqlite without a persistent database for our tests.
       
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///data.db", SECRET_KEY='cvm859df', DEBUG=True, WTF_CSRF_ENABLED=False)
        return app

    def setUp(self):
       

        db.session.commit()
        db.drop_all()
        db.create_all()
        sample1=Users(id=0, first_name="aaaaa", last_name="wwww", email="jdhsj@hsdg")
        sample2=Users(id=0, first_name="ali", last_name="one", email="jj@hsdg")
        db.session.add(sample1)
        db.session.add(sample2)
        db.session.commit()
        
    def tearDown(self):
        # Close the database session and remove all contents of the database
        db.session.remove()
        db.drop_all()
       
       
class TestModel(TestBase):
    def test_models(self):
    	user1=Users.query.filter_by(first_name="aaaaa").first()
    	user2=Users.query.filter_by(last_name="one").first()
    	assert user1.last_name == "wwww"
    	assert user2.first_name == "ali"
