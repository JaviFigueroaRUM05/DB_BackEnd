Create table Users(uid serial primary key, uname varchar (20) NOT NULL UNIQUE,
                    password varchar (20) NOT NULL, first_name varchar (20) NOT NULL,
                    last_name varchar (20)NOT NULL, email varchar (40) NOT NULL UNIQUE,
                    phone varchar(11) NOT NULL UNIQUE);

Create table Contacts(uid integer references Users(uid) NOT NULL,
                      cid integer references Users(uid) NOT NULL CHECK (cid <> uid),
                      primary key (uid, cid));

Create table Cgroup(gid serial primary key, gName varchar (20) NOT NULL, gPhoto varchar (100));

Create table Participants(uid integer references Users(uid) NOT NULL, gid integer references Cgroup(gid) NOT NULL,
                            primary key (uid,gid), isAdmin boolean NOT NULL);

Create table Post(postID serial primary key, pDate timestamp NOT NULL, message text,
                  mediaType char(1) NOT NULL,  media text, uid integer references Users(uid) NOT NULL,
                  gid integer references Cgroup(gid) NOT NULL);

Create table Reaction(rid serial primary key, rDate timestamp NOT NULL, rType char (1) NOT NULL,
                      postID integer references Post(postID) NOT NULL, uid integer references Users(uid) NOT NULL,
                      UNIQUE (postID, uid));

Create table Replies(opID integer references Post(postID) NOT NULL, replyID integer references Post(postID) NOT NULL,
                     primary key (opID, replyID));

Create table Hashtag(hid serial primary key, hName text NOT NULL UNIQUE);

Create table Tagged(postID integer references Post(postID) NOT NULL, hid integer references Hashtag(hid) NOT NULL,
                    primary key (postID, hid));
