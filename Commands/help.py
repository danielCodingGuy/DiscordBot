#Basic help command that displays all of the features
#author: danielCodingGuy

if message.content.startswith('$help'):
  await message.reply('Command list: $hello', mention_author=True)
