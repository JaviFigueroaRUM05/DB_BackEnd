from flask import jsonify
from dao.interactions import InteractionsDao
class InteractionHandler:

    def updateReaction(self, pid, json):
        dao = InteractionsDao()
        if json['rType'] == 'like':
            return dao.likePost(pid)
        elif json['rType'] == 'dislike':
            return dao.dislikePost(pid)
        else:
            return jsonify(Error="Unsuported reaction"), 405

    def postReply(self, pid, json):
        dao = InteractionsDao()
        return dao.replyPost(pid, json)
