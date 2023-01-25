#Command that bans member for time specified in the command or message
#Author: danielCodingGuy

class BanFlags(commands.FlagConverter):
    members: List[discord.Member] = commands.flag(name='member')
    reason: str
    days: int = 1

@commands.command()
async def ban(ctx, *, flags: BanFlags):
    for member in flags.members:
        await member.ban(reason=flags.reason, delete_message_days=flags.days)

    members = ', '.join(str(member) for member in flags.members)
    plural = f'{flags.days} days' if flags.days != 1 else f'{flags.days} day'
    await ctx.send(f'Banned {members} for {flags.reason!r} (deleted {plural} worth of messages)')

#Example: @<Bot name> ban member: @<member name> reason:<reason> days:<number of days>
#If number of days is different than the time specified in the code, this command should ban user mentioned in the message for time specified in the message
