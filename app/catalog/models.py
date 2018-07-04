from app import db  # from our app.__init__.py file
from datetime import datetime  # for one of our fields

# just copying this in from the previous project- uflask

class Publication(db.Model):  #this inherents from db.Model
    __tablename__ = 'publication'  # this is the name of the table itself

    # note using SQLalchemy takes care alof the DB talk and config for us

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    def __init__(self, name): # removing ID because we want the priamry key to be auto-generated
        #self.id = id removing this so that the primary key is auto generated
        self.name = name

    def __repr__(self ):  # this returns a string version of the instance
        return  'Publisher is {} '.format(self.name)  # removing self that ID so the primary key could be auto-generated





class Book(db.Model):
    __tablename__ = 'book'  # this is the name of the table itself

    # note using SQLalchemy takes care a lot of the DB talk and config for us

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500), nullable=False, index=True) # this will spead up results time
    author = db.Column(db.String(350))
    avg_rating = db.Column(db.Float)
    format = db.Column(db.String(50))
    image = db.Column(db.String(100), unique=True)
    num_pages = db.Column(db.Integer)
    pub_date = db.Column(db.DateTime, default=datetime.utcnow())# this datetime is from Python

    #relationship

    pub_id = db.Column(db.Integer, db.ForeignKey('publication.id')) # this is the last column- need to define foreign key
    #  and pass the primary key from the publication table, the id column (which is its primary key)
    # this is a 1:many relationship- because each publisher can have more than one book.
    # so the one is the publisher the many is the # of books he can publish

    def __init__(self, title, author, avg_rating, book_format, image, num_pages, pub_id): # note relationship col is included

        # purpose constructs/registers the new instances every time one is created.
        self.title = title
        self.author = author
        self.avg_rating = avg_rating
        self.format = book_format
        self.image = image
        self.num_pages= num_pages
        self.pub_id = pub_id
        # note we did not include the pub date, because date fields in SQLAlchemy are popuated automatically because we set a sefault for this field
        # same with the primary key


    def __repr__(self):  # this returns a string version of the instance- prints in an acceptable manner
        return '{} by {} '.format(self.title, self.author)


