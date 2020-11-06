# Cartloop Chat

## Setup

Make sure you have docker and docker-compose installed, then run:

    docker-compose up -d

You should be able to access the conversation endpoint at:

* http://localhost:8000/api/conversations/

And the chat endpoint at:

* http://localhost:8000/api/chats/

The setup takes care of creating dummy data (essentially the data provided in the task description with a few minor modifications).

## Using the POST endpoint

You should be able to post chats with the following payload:

    {
        "conversationId": 1,
        "chat": {
            "payload": "Hello",
            "userId": 1
        }
    }

The `conversationId` and `userId` must always be `1` because these are the only objects generated during setup.

## Difficulties

The following are the difficulties I had and how I dealt with them considering my time limitations.

### User vs client

I didn't understand the meaning of `user` and `client`, so I just treated `client` as an arbitrary integer and considered that the conversation happened between an operator and a user.

### Different user per chat

Although in the sample JSON each chat was linked to a different user, I couldn't make sense of that so I used the same ID everywhere. I know that it doesn't make much sense to link to the same user in every chat object, and that it would make more sense to link to the user in the Conversation object, but due to time limitations and since I couldn't make sense of the user/client distinction I continued like this.

### Invalid timestamp

The timestamp in the 3rd chat was invalid, so I simply used a correct value when populating the database with the sample conversation provided in the task description.

### Validation

* Payload character validation: I didn't have time.
* Payload should be shorter than 300 characters: Implemented in the model.
* UTC date stamp validation: I didn't understand this since this information is not in the example payload provided in the task description. I implemented the generation of the timestamp in the backend since this made more sense to me.
* Replacing keywords: in my understanding this is only applicable if the bonus question was implemented.
* Chat message state change: in my understanding this is only applicable if the bonus question was implemented.

### Tests

I know this wasn't explicit in the requirements but I was planning to implement them, unfortunately I didn't have time.

### Bonus

Didn't have time.
