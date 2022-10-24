#Command that makes bot respond with random sentence from the list
#author: danielCodingGuy

if message.content.startswith('$command'):
    responses = [
        'response 1',
        'response 2',
        'response 3',
        'response 4'
        ]
await message.reply(random.choice(responses), mention_author=True)