-- Actual Project schema
--
Create table Person(pid serial primary key, first_name varchar (20) NOT NULL, last_name varchar (20)NOT NULL,
                    email varchar (40) NOT NULL UNIQUE, phone varchar(11) NOT NULL UNIQUE);

Create table Users(uid serial primary key, pid integer references Person(pid) NOT NULL, uname varchar (20) NOT NULL UNIQUE,
                    password varchar (20) NOT NULL);

Create table Contacts(uid integer references Users(uid) NOT NULL, cid integer references Users(uid) NOT NULL CHECK (cid <> uid), primary key (uid, cid));

Create table Cgroup(gid serial primary key, gName varchar (20) NOT NULL, gPhoto varchar (100));

--How can we ensure that all admins are participants in their own chats?
Create table Admins(uid integer references Users(uid) NOT NULL, gid integer references Cgroup(gid) NOT NULL, primary key (uid,gid));

Create table Participants(uid integer references Users(uid) NOT NULL, gid integer references Cgroup(gid) NOT NULL, primary key (uid,gid));

Create table Post(postID serial primary key, pDate timestamp NOT NULL, message text, media text,
                    uid integer references Users(uid) NOT NULL, gid integer references Cgroup(gid) NOT NULL);

Create table Reaction(rid serial primary key, rDate timestamp NOT NULL, rType char (1) NOT NULL, postID integer references Post(postID) NOT NULL);

Create table Reacts(uid integer references Users(uid) NOT NULL, rid integer references Reaction(rid) NOT NULL, primary key (uid, rid));

Create table Replies(postID integer references Post(postID) NOT NULL, replyID integer references Post(postID) NOT NULL,
                     primary key (postID, replyID));

Create table Hashtag(hid serial primary key, hName varchar(20) NOT NULL UNIQUE);

Create table Tagged(postID integer references Post(postID) NOT NULL, hid integer references Hashtag(hid) NOT NULL,
                    primary key (postID, hid));



/*
-- This file contains the definitions of the tables to be used in the application.
--
create table chat_groups(gid serial primary key, gname varchar(20), gphoto varchar(200), gadmin integer references users(uid));

create table Contacts(tid serial, uid int references users(uid), cid int references users(uid));

create table Users(uid serial primary key, uname varchar(20), email varchar(20), password varchar(20), fname varchar(20), lname varchar(20), photo varchar(200));

create table Post(pid serial primary key, post_date date, media varchar(200), message text);

CREATE TABLE public.participants
(
  group_id integer,
  group_name character varying(20),
  participant_id integer,
  participant_name character varying(20),
  CONSTRAINT participants_group_id_fkey FOREIGN KEY (group_id)
      REFERENCES public.chat_groups (gid) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION,
  CONSTRAINT participants_participant_id_fkey FOREIGN KEY (participant_id)
      REFERENCES public.users (uid) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION
)

create table Reply(rid serial primary key, original_post integer references Post(pid), reply_post integer references Post(pid))

create table Group_Posts(gp_id serial primary key, gid integer references chat_groups(gid), pid integer references post(pid))
*/
