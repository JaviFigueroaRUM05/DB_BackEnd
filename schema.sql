-- Actual Project schema
--
Create table Person(pid serial primary key, first_name varchar (20), last_name varchar (20),
                    email varchar (40), phone integer);

Create table Users(uid serial primary key, pid integer references Person(pid), uname varchar (20),
                    password varchar (20));

Create table Contacts(uid integer references Users(uid), cid integer references Users(uid), primary key (uid, cid));

Create table Cgroup(gid serial primary key, gName varchar (20), gPhoto varchar (100));

Create table Admins(uid integer references Users(uid), gid integer references Cgroup(gid), primary key (uid,gid));

Create table Participants(uid integer references Users(uid), gid integer references Cgroup(gid), primary key (uid,gid));

Create table Post(postID serial primary key, pDate timestamp, message text, media text,
                    uid integer references Users(uid), gid integer references Cgroup(gid));

Create table Reaction(rid serial primary key, rDate timestamp, rType char (1), postID integer references Post(postID));

Create table Reacts(uid integer references Users(uid), rid integer references Reaction(rid), primary key (uid, rid));

Create table Replies(postID integer references Post(postID), replyID integer references Post(postID),
                     primary key (postID, replyID));

Create table Hashtag(hid serial primary key, hName varchar(20));

Create table Tagged(postID integer references Post(postID), hid integer references Hashtag(hid),
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
