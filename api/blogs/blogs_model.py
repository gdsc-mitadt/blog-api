import const
from datetime import datetime
from db import db

class UserLinks(db.EmbeddedDocument):
    profile_pic_link = db.StringField()
    github_link = db.StringField()
    linkedin_link = db.StringField()
    instagram_link = db.StringField()
    personal_site_link = db.StringField()

class UserDetails(db.EmbeddedDocument):
    meta = {'strict': False}
    email_id = db.StringField()
    first_name = db.StringField()
    last_name = db.StringField()
    organization = db.StringField()
    user_links = db.EmbeddedDocumentField(UserLinks)

class Content(db.EmbeddedDocument):
    meta = {'strict': False}
    title = db.StringField()
    body = db.StringField()
    footer = db.StringField()
    content_image = db.StringField()
    external_link = db.StringField()

class Blogs(db.Document):
    meta = {'collection': 'blogs', 'strict': False}
    created_on = db.DateTimeField()
    modified_on = db.DateTimeField()
    modified_by = db.StringField()
    content = db.EmbeddedDocumentField(Content)
    user_details = db.EmbeddedDocumentField(UserDetails)