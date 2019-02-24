from flask import jsonify

class InteractionsDao:

    def likePost(self, pid):
        output = {
                "Output" : "liked post",
                "PID" : pid
                }
        return jsonify(output)

    def dislikePost(self, pid):
        output = {
                "Output" : "disliked post",
                "PID" : pid
                }
        return jsonify(output)

    def replyPost(self, pid, json):
        output = {
                "Output" : "replied to post",
                "PID" : pid,
                "Post" : json
                }
        return jsonify(output)
