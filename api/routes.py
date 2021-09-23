from api.blogs.blogs_service import BasicBlogsApi, BlogsByIdApi

def initialize_routes(api):
    api.add_resource(BasicBlogsApi, '/api/blogs', endpoint='blogs')
    api.add_resource(BlogsByIdApi, '/api/blogs/<id>', endpoint='update_blogs')