from models.user import Feed


class FeedService:

    @staticmethod
    def add_feeds(feed):
        name = feed.get('name')
        title = feed.get('title')
        content = feed.get('content')

        Feed.create_feed(
            name=name,
            title=title,
            content=content
        )
    @staticmethod
    def get_all_feed():
        feed= Feed.get_all_feed()
        results = []
        for feeds in feed:
            _feeds = dict(
                id=feeds.id,
                name=feeds.name,
                title=feeds.title,
                content=feeds.content
            )
            results.append(_feeds)
            return results
    @staticmethod
    def update_feeds(feed):
        Feed.update_feed(
            _id=feed.get('id'),
            name=feed.get('name'),
            title=feed.get('title'),
            content=feed.get('content')
        )

    @staticmethod
    def  delete_feed(_id):
        Feed.del_feed(_id) 
