import json
from flask import Blueprint, request
from services.feed_service import FeedService

FEED = Blueprint(
    'feed',
    __name__,
    url_prefix='/api/v1'

)

@FEED.route('/users', methods=['POST'])
def create_feed():
    params = request.get_json()
    FeedService.add_user(params)
    return json.dumps({
        'Message': 'User {name} {title} {content} inserted.'
    })


@FEED.route('/users', methods=['GET'])
def get_all_feed():
    users = FeedService.get_all_users()
    return json.dumps({'users': users})


@FEED.route('/user', methods=['PUT'])
def update_feed():
    params = request.get_json()
    FeedService.update_feed(params)
    return json.dumps(({'message': 'feed updated successfully'}))


@FEED.route('/feed/<_id>', methods=['DELETE'])
def delete_feed(_id):
    FeedService.delete_feed(_id)
    return {"message": f"Feed successfully deleted."}
