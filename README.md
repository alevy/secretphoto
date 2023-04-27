# Secure Photo Lab

In this lab you will design and implement a private album feature. We have
given you a system that meets the correctness properties below, but one that is
very insecure and provides no confidentiality.

This coding lab is closely related to the theory pset.  In particular, we ask
you to implement a functionality very close to what you designed in the part
(c) of the first problem. However, note that the theory pset makes some
abstractions that do not apply here (see below).  Note that there is no
bandwith restriction here.  If you haven't looked at the theory part first, we
advise you to read it to get hints on how to proceed.

# Code Overview

In this lab, we provide methods in the `crypto` module to allow you to encrypt.
There are methods for both public-key and symmetric encryption, and each client
has an associated public key and authenticated encryption object that can be
used to encrypt and decrypt.

1. To create an album, all users that the album will be shared with must be added as friends.
2. To fetch an album, it will be required that the owner of the album is added as a friend.

We have implemented public profiles and provide a client to upload its own
_encryption_ public key into the public profile upon registration and have
provided a metadata field where you can add extra information.

## Tests

The grader for this lab replaces the crypto library with another alternative
that allows us to find all data that a client has access to. For this reason,
if you print encryption keys when running the grader, your encryption printouts
may look a bit different than you are expecting. However, they include data
that may be helpful in debugging. For more information, see the
`ag/ag3/crypto_overrides.py` file.

# Specification 

## Scenario

Suppose that Alice has taken some photos which she wishes to share _privately_
with some of her friends.  Right now, all the photos she uploads through our
application are public.

In order to allow Alice to control who has access to these pictures, we would
like to introduce the notion of _private albums_.
A private album has an _owner_ (`"Alice"`), a list of _photos_
(`[secret_party_invite.jpg, buried_treasure_coordinates.jpg]`), and a list of
_friends_ who can add photos to and view photos in the album (`["Alice", "Bob",
"Carlos", "Danielle"]`).
In this scenario, once Alice has created the album, she wishes for the
following to be true.

  1. All of the friends should be able to view all of the photos, and
  2. No one else should be able to view any of the photos.

## Assumptions

 - The server is functioning correctly and will not tamper with the integrity
     of messages.  However, the server might not authenticate users before
     performing operations on their behalf.

 - Operations between the clients and the server happen sequentially and
     atomically. A client will always have the latest version of the server
     state when the client tries to modify the state.

## Correctness

Given these assumptions, our albums feature should support the following
**correctness** properties.

1. Any client is able to create a private album and upload it to the server
   using `create_shared_album(album_name, photos, friends)`, where all friends
   in `friends` have been added using `add_friend`. The client who does this is
   the album's _owner_.
2. Any client which is part of an album's `friends` is able to view photos
   within the album by calling `get_album(album_name)`, provided that the album
   owner's signing key has been added locally using `add_friend`.
3. Any client which is part of an album's `friends` is able to add photos to
   the album by calling `add_photo_to_album(album_name, photo)`.
4. An album's owner can `add_friend_to_album(album_name, friend_username)`,
   provided that `friend_username` is the username of a user who has been added
   using `add_friend`. Once a friend is added to an album, it should be able to
   access all photos which were already added.

## Security

In addition, we should also support the following **confidentiality** property:
clients (identified by their public signing key) which are _not_ part of an
album should not be able to see any photo within the album. 

1. If a client is never a member of an album, they should not be able to see
   any photos in the album.
2. An album's owner can remove a member from an album with
   `remove_friend_from_album(album_name, friend_name)`.  After a member is
   removed, it should not be able to see any new photos that are added to the
   album.

## Liveness

Finally, we would like to have some property of liveness---that our system
still works even in the face of (certain types of) attackers. With this in
mind, we would like the following property:

1. The presence of illegitimate members in an album should not prevent
   legitimate members from using the album as usual. Any 'members' that were
   not added by someone besides should be ignored, but must not be allowed to
   view the album contents.

# Your Job

is to modify `client.py` to implement _secure_ private albums.

To do so, you can use the PKI, the public profile feature and the two new
cryptographic primitives we added to your library: authenticated symmetric-key
encryption and authenticated public-key encryption.  For a precise
specification of these primitives, refer to the theory portion of lab 3.

As with previous labs, _this is an open-ended assignment!_  Again, you may
modify any code in `client/` so long as you do not change the signatures of the
public methods of `Client` (i.e., the `__init__` method or methods not
beginning with an underscore `_`).
However, since your `Client` must still talk to our server, you will **not** be
able to modify any other files given to you.

