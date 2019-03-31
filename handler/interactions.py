from flask import jsonify
from psycopg2 import IntegrityError
from dao.interactions import InteractionsDao

REACTION_JSON_KEYS = ['rType', 'rDate']


def validate_json(json, keys):
    for key in keys:
        if key not in json:
            return jsonify(Error='Missing attribute in JSON'), 400


class InteractionHandler:
    @staticmethod
    def post_reaction(uid, pid, json):
        validate_json(json, REACTION_JSON_KEYS)
        dao = InteractionsDao()
        date = json.get('rDate')
        try:
            if json.get('rType') == 'like':
                dao.like_post(pid, uid, date)
            elif json.get('rType') == 'dislike':
                dao.dislike_post(pid, uid, date)
            else:
                return jsonify(Error='Invalid value'), 400
            return jsonify(Status='Success')
        except IntegrityError as e:
            print(e)
            return jsonify(Error=str(e))

    @staticmethod
    def update_reaction(uid, pid, json):
        validate_json(json, REACTION_JSON_KEYS)
        dao = InteractionsDao()
        date = json.get('rDate')
        try:
            if json.get('rType') == 'like':
                result = dao.update_to_like(pid, uid, date)
                if result[0] != 'UPDATE 0': return jsonify(Status='Success')
                else:                       return jsonify(Status='Failure')
            elif json.get('rType') == 'dislike':
                result = dao.update_to_dislike(pid, uid, date)
                if result[0] != 'UPDATE 0': return jsonify(Status='Success')
                else:                       return jsonify(Status='Failure')
            else:
                return jsonify(Error='Invalid value'), 400
        except IntegrityError as e:
            print(e)
            return jsonify(Error=str(e))

    @staticmethod
    def delete_reaction(uid, pid):
        dao = InteractionsDao()
        try:
            result = dao.delete_reaction(pid, uid)
            if result[0] != 'DELETE 0': return jsonify(Status='Success')
            else:                       return jsonify(Status='Failure')
        except IntegrityError as e:
            print(e)
            return jsonify(Error=str(e))

    @staticmethod
    def get_reaction(uid, pid):
        dao = InteractionsDao()
        try:
            result = dao.get_reaction(pid, uid)
            if result.size == 0: return jsonify(Reaction='none')
            else:                return jsonify(Reaction=result[0])
        except IntegrityError as e:
            print(e)
            return jsonify(Error=str(e))