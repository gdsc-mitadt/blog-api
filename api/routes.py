from api.blogs.blogs_service import BasicBlogsApi, UpdateBlogsApi

def initialize_routes(api):
    api.add_resource(BasicBlogsApi, '/api/blogs', endpoint='blogs')
    api.add_resource(UpdateBlogsApi, '/api/blogs/<id>', endpoint='update_blogs')
