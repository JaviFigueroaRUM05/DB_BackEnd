from flask import jsonify
from dao.posts import PostsDAO

class PostsHandler:

    posts_cont = ["postid","pdate","message","mediatype", "media","uid","gid"]

    def build_post_dict(self, row):
        result = {}
        result['postid'] = row[0]
        result['pdate'] = row[1]
        result['message'] = row[2]
        result['mediatype'] = row[3]
        result['media'] = row[4]
        result['uid'] = row[5]
        result['gid'] = row[6]
        return result


    def getAllPosts(self):
        dao = PostsDAO()
        posts_list = dao.getAllPosts()
        result_list = []
        for row in posts_list:
            result = self.build_post_dict(row)
            result_list.append(result)
        return jsonify(Posts=result_list)

        # get posts in a group
    def getPostsByGroup(self, gid):
        dao = PostsDAO()
        post_list = dao.getPostsByGroup(gid)
        result_list = []
        for row in post_list:
            result = self.build_post_dict(row)
            result_list.append(result)
        return jsonify(Posts=result_list)


    def createNewPost(self, p_info):
        # dao = PostsDAO()
        # p_date= p_info['post_date']
        # media= p_info['media']
        # message= p_info['message']
        # gid = p_info['gid']
        # reply = p_info['reply_to_post']
        #
        # gid = dao.createNewGroup(p_date=p_date, media=media, message=message, gid=gid, reply=reply)
         p_info['pid']=5
         self.posts.append(p_info)
         return jsonify(p_info)

    def getPostsById(self, pid):
        # dao = PostsDAO()
        # row = dao.getPostById(pid)
        # if not row:
        #     return jsonify(Error = "Group Not Found"), 404
        # else:
        #     return row[1]
        for row in self.posts:
            if(row['pid'] == pid):
                result = row
                return jsonify(result)
            else:
                return 404


    #get posts made my a certain user
#TODO: check that its working
    def getPostsByUser(self, uid):
        # dao = PostsDAO()
        # post_list = dao.getPostsByUser(uid)
        # result_list = []
        # for row in post_list:
        #     post = dao.getPostById(row[0])
        #     result = self.build_post_dict(post)
        #     result_list.append(result)
        # return jsonify(Posts=result_list)
        posts = [{
            'pid' : 10,
            'p_date': '2019-01-25',
            'media' : 'default',
            'message' : 'Im tired'
        },
        {
            'pid' : 8,
            'p_date': '2019-01-25',
            'media' : 'default',
            'message' : 'Me too'
        }]
        return jsonify(posts)
