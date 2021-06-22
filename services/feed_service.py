from models.user import Feed


class FeedService:

    @staticmethod
    def add_user(users):
        name = users.get('name')
        title = users.get('title')
        content = users.get('content')

        Feed.create_feed(
            name=name,
            title=title,
            content=content
        )
    @staticmethod
    def get_all_feed():
        users = Feed.get_all_feed()
        results = []
        for user in users:
            _user = dict(
                id=user.id,
                name=user.name,
                title=user.title,
                content=user.content
            )
            results.append(user)
            return results
    @staticmethod
    def update_user(users):
        Feed.update_feed(
            _id=users.get('id'),
            name=users.get('name'),
            title=users.get('title'),
            content=users.get('content')
        )

    @staticmethod
    def  delete_feed(_id):
        Feed.del_feed(_id) 
