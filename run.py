from app import create_app, db  # this is the app package in the app init.py file create_app is a function, db is out db instance
from app.auth.models import User

#if __name__ == '__main__': # remove this as it is not needed in prod
flask_app = create_app('prod')# create_app  a function we created in the app/init file


with flask_app.app_context(): # app_context is a method available inside flask insance (we call app). See below
    db.create_all()  # these creates all db-tables

        # if not User.query.filter_by(user_name='harry').first(): # if harry does not already exist create this default user
        #     User.create_user(user='harry', email='harry@potter.com', password='secret')
            # if harry does exit it will by bypass this and just run the app

    #flask_app.run(debug=True, port=5000) # use flask instance to run the application
    flask_app.run( )
    #

    # This whole with statements just tells flask to yuse the current app context to create the db tables
    #This is import when using packages because you are dealing with multiple applications in one project


    ####explanation#####

    #app_context() = Binds the application only. For as long as the application is bound to the current context the
    # flask.current_app points to that application. An application context is automatically
    # created when a request context is pushed if necessary.


    #flask.current_app =Points to the application handling the request. This is useful for extensions that want to support
    # multiple applications running side by side.
    # This is powered by the application context and not by the request context, so you can
    # change the value of this proxy by using the app_context() method.
    #

    #Notes On Proxies
    # Some of the objects provided by Flask are proxies to other objects. The reason behind this is that these proxies
    # are shared between threads and they have to dispatch to the actual object bound to a thread behind the scenes as necessary.
    #1. The proxy objects do not fake their inherited types, so if you want to perform actual instance checks,
    #you have to do that on the instance that is being proxied (see _get_current_object below).
    # 2. if the object reference is important (so for example for sending Signals)

    #If you need to get access to the underlying object that is proxied, you can use the _get_current_object() method:

                # app = current_app._get_current_object()
                # my_signal.send(app)

    ## What is a singal? In short, signals allow certain senders to notify subscribers that something happened.
    ##  example: Say you want to know what templates were rendered as part of a request: signals allow you to do exactly that.