#Basic help command that displays all of the features
#author: danielCodingGuy

if message.content.startswith('$help'):
  await message.reply('Command list: $command1, $command2, $command3', mention_author=True)
