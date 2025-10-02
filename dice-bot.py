import asyncio
import discord
import math 
import numpy as np
import re
import pytubefix as pytube
import spotipy

from discord.ext import tasks,commands
from spotipy.oauth2 import SpotifyClientCredentials

FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5','options': '-vn -filter:a "volume=0.05"'}#optimised settings for ffmpeg for streaming

loopsong = "False"
loc = "False"
yt = "False"
link = ""
context = ""
source = ""

CLIENT_ID = "[INSERT SPOTIFY DEV CLIENT ID]"
CLIENT_SECRET = "[INSERT SPOTIFY CLIENT SECRET]"
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=CLIENT_ID,
                                                               client_secret=CLIENT_SECRET))
        
class Greet(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.command(brief="A simple greeting.",help="Usage: &&hello\nA simple greeting.",aliases=["Hello"])
    async def hello(self, ctx):
        """A simple greeting."""
        member = ctx.author
        await ctx.send(f'Hello {member.display_name}, have a wonderful day!')
        
    @commands.command(brief="Get a random quote from the list!",help="Usage: &&quote\nGet a random quote from the list!",aliases=["Quote"])
    async def quote(self, ctx):
        """Get a random quote from the list!"""
        quote_array = ["WHAT DOES BRAINCELL EVOLVE INTO - Suds",
                        "But Grandma! You're not old! - Homeboy",
                        "Don't give me a thumbs up. Perish! - Kat",
                        "I'm sandwiched between fruit salad and someone's ass. - Joker",
                        "Good news: Bombs. - Skel",
                        "I'm still - in a dream. Girl Sniffer! - Homeboy",
                        "Oh good, do I get to punch his wife? - Kat",
                        "Fight later, existential crisis now? Sounds good! I end my turn. - Will  NO! - Skel",
                        "Some day soon we'll turn that sun into a snowcone. - Day",
                        "The Moon could be from accounting. - Matt",
                        "One French person is worth one foosball table. Scratch that. One French person is worth two foosball tables. - Homeboy",
                        "Mankey's Paw curls - Matt",
                        "You cannot command word Tax Evasion. - Kat",
                        "OK, Mr. Sister Sir. - Day",
                        "I like my woman like I like my pizza. Hot and depressing. - Day",
                        "That's not a vibe check, that's a murder... - Grav",
                        "So you put your item up for sale on Braig's List... - Grav",
                        "I can't believe all those times I was beating up children I didn't notice that - Grav",
                        "Isn't being psychotic fun? - Homeboy",
                        "You ruined your own trauma, by the way - Suds",
                        "I don't know how to fight weather with a sword. - Suds",
                        "Argue with the bones, I'm going on the boat. - Ct",
                        "My God Complex is 100% unrelated to my dick. - Ct",
                        "What are some other veggies...do you want an apple? - Zombie",
                        "We should make friendship bracelets with Anubis' spinal cord! :D - Homeboy",
                        "I was gonna say so you don't look weird, but I think we're well past that. - Joker  **Frog Stance** - Matt",
                        "I'm not going to lie to a child. - Chris  Not even to save another friend from vore? - Will",
                        "I'd like to think SOME people appreciate me. - Kat  Who and when?  I'd like to meet them. - Skel",
                        "Not Italian, Italians don't exist. - Grav",
                        "I'm putting chocolate into a bomb. Do you think I'm okay? - Day",
                        "I'm OSHA, and I *make* the violations - Kat",
                        "I'm so smart.  When I walk in the room, I bring the IQ down by 10! - Zombie",
                        "That question was sliding around my smooth brain, using it like an ice rink. - Zombie",
                        "No, no, the hoes are quite knowledgeable on the Elder Gods! - Grav",
                        "Bye Homeboy! - Kat  WHAT DO YOU MEAN BYE?!? - Homeboy"]
        ind = np.random.randint(len(quote_array))
        await ctx.send(quote_array[ind])
    
    @commands.command(brief="Get a random quote from the list, but this time it's D&D characters.",
                      help="Usage: &&dndquote\nGet a random quote from the list, but this time it's D&D characters.",
                      aliases=["Dndquote"])
    async def dndquote(self, ctx):
        """Get a random quote from the list, but this time it's D&D characters."""
        quote_array = ["Pickingthelockpickingthelock - Vi",
                       "...Misogyny. - Apollo",
                       "Are those ears real or are you just... happy to... Nevermind. - Goro"]
        ind = np.random.randint(len(quote_array))
        await ctx.send(quote_array[ind])
        
    @commands.command(brief="Compliments the friend you @ mention.",
                      help="Usage: &&compliment @Member\nCompliments the friend you @ mention.",
                      aliases=["Compliment"])
    async def compliment(self,ctx):
        """Compliments the friend you @ mention."""
        gen_array = ["You are a star beyond measure.",
                     "It's meeting people like you that makes me believe in miracles.",
                     "You express your heart truthfully and it shows in all of the best ways.",
                     "You've got a creativity that makes spending time around you a joy!",
                     "Honestly, you are a wonderful bean and no one can convince me otherwise."]
        matt_array = ["You have such a great imagination and way of realizing that imagination. ~~Also nice ass~~",
                      "You’re a great and inspiring DM.",
                      "You're one of the strongest people I know, and you continue to find ways to get stronger. I'm happy to know you as a person and that I get to witness you evolve as a person.",
                      "You’re the one who tends to take a first step. You tend to wonder who you are, but that's normal. You are a wonderful person and steadfast in many regards. You are also probably one of the best players in a roleplay sense.",
                      "You have an intense sense of compassion.  You empathize and express your empathy to those around you, making the world a more inviting place."]
        homeboy_array = ["The characters you make are some of the most well thought-out characters I've had the pleasure of learning about.",
                         "You’re a cinnamon roll.",
                         "You always find ways to make me smile and laugh. I know I can come to you when I need something to pick me up, and you're a great person to talk to in general. You're always such an amazing friend to me and I'm not afraid to say that.",
                         "You are a wonderful goober. You tend to have some of the best quips to the point that even you start laughing while trying to deliver them.",
                         "You've taken time out of your busy and stressful life to help people, being a light in their darkness. We're beyond blessed to know you, and you deserve the best (even if that best is us giving you a break ;) )"]
        suds_array = ["You have a heart of gold, and an intense love for so many things that you're always excited to share - it makes us excited too!",
                      "You have an over abundance of creativity. You also have quite the infectious laugh when a joke really gets to you.",
                      "You are a never ending factory of ideas and characters. The best part? Bangers. Every last one of them. Iconic like Goro, supportive in the best ways like Dalzin, short like Yurintide, you just stick the landing.",
                      "Your ability to weave a story never ceases to amaze me!",
                      "I don't know how you do it, but your range when it comes to playing characters is DAMN impressive."]
        will_array = ["Your insights about characterization and story telling are something truly special.",
                      "You’re probably one of the most well-informed people here. You know a lot about several topics and are able to yap about them for minutes on end. You also are headstrong in your ideals which is not always a bad thing.",
                      "You have ambition and passion that drives you to try and run multiple settings at once. It's commendable, and I hope you are taking time to take care of yourself considering.",
                      "You have an intense and burning creativity that comes out in all of your settings and projects. It's a joy to see you thrive!",
                      "When you tell a story, you evoke emotional responses and plant characters in the world."]
        skel_array = ["The amount of information you can absorb and also critically think about is incredible and envious.",
                      "I don't know how you do it, but you keep amazing me with your ideas. It takes a certain kind of genius to be able to do that, and I'm proud to be able to know you.",
                      "You are Creative, Insane, Silly, and Compassionate. You also have some of the wildest wordings of sentences that people still think about.",
                      "Never before have I met someone as patient as you. You also are very observant about things, but you give us time to say things when we are ready, assuming it isn't an issue with people.",
                      "You are a well of creativity and ideas, to the point where I'm pretty sure most people would have run out by now but you're still going strong!"]
        day_array = ["Your love for and knowledge about history and mythology is amazing, keep telling the world's stories.",
                     "You have a passion for story, and it comes out in the details you think of for your settings and characters!",
                     "You tend to wear your heart on your sleeve, quick to express your feelings on a matter. Also, you are willing to go far for the bit.",
                     "You have stepped forward and taken on large tasks with a motivation that is impressive.",
                     "You have a commendable drive to bring a story to life!"]
        grav_array = ["You have some of the most unique ideas I have had the pleasure of both seeing and playing.",
                      "You have some of the weirdest Campaign ideas but still keep it to the realm of DnD-esque. Also you have some of the silliest voices.",
                      "You are always committed to the bit, and you know how to let loose. Your characters are fun, and you definitely let your passion show.",
                      "Your ability to improv is some of the best I've ever seen!",
                      "I appreciate your dedication to making sure everyone is having fun by taking our bad ideas and making them good."]
        # Joker needs to have one more than everyone else because Ping-E
        joker_array = ["When you love a character, it shows so completely and brilliantly that I'm blinded by it.",
                       "You’re horny! But that's not the important part, what's more important is your ability to be a good competitor in a game. You can have some great Rival energy.",
                       "You tend to take advice well, and it's shown how much you have grown and improved as a person. From Rhys to Niel and beyond, you've only wanted and worked on improving your characters. Maybe one day we'll get you casting spells ;)",
                       "Ping-E",
                       "You may stick to a small group of classes, but you've gotten very good at knowing what they do and using the classes as a stepping stool for fully embodying the character.",
                       "It's always interesting to see what direction you choose to take your characters, because it's often unexpected!"]
        chris_array = ["Your roleplay is simple in the best of ways. There is no worry that a character you bring wouldn't be a fun one.",
                       "You may be on the lower end of number of interactions with the rest, but you still manage to make those moments fun. Your bluntness is definitely a charm that is hard to replicate.",
                       "You display a joy in the simple things, and that spreads to the rest of us!",
                       "Your knowledge on a wide range of topics is impressive.",
                       "You have the ability to play a wide range of character types, and it's always interesting to see what directions you choose!"]
        fiery_array = ["The spark you add to each of your ideas is every bit amazing as it is exciting. Which is to say a lot.",
                       "You're very chill, you're willing to try out new things to play with people here, and you just seem to have fun. What's not to like?",
                       "You are a problem in all the best ways, making sure some good chaos gets spread.",
                       "You have a very good grasp on characters and rules, and use that knowledge to create some of the most intriguing characters and situations.",
                       "You are skilled at telling a story, to the point where you can make people cry."]
        nate_array = ["You always try to make sure anyone who wants to be included in something is included.",
                      "I have only met two of your characters so far, and both are creative and wonderful.",
                      "You're very good at knowing what you can do and doing it well, in ways none of us could have prepared for!",
                      "You bring humor to the group, and your laugh brings a lot of joy.",
                      "It's always a pleasure playing alongside you because we always know it will be a fun time!"]
        ct_array = ["It cannot be understated how incredible you are at creating a story and world that engages everyone in it.",
                    "Your ability to intertwine multiple campaigns throughout a timeline with ease and little to no risk of things drastically changing, keeping everyone on their toes, is wonderful and I can only hope to be that prepared. Also, I love the character name spellings. It never gets old.",
                    "You are a problem.  Affectionate...I think.",
                    "You have so much creativity, coming up with ideas that I can't even dream of.",
                    "Your passion for the worlds you create is evident in the stories you tell."]
        zombie_array = ["You bring an infectious joy and pure gremlin energy to everything you do!",
                        "You are such a fun-loving person and your laugh is one of the most infectious I've heard. ~~Also you're Kat's husband, so like, that's automatically cool~~",
                        "We need to play more things together. You have a lot of fun, and you have a knack for breaking people's serious character mindsets (affectionate)",
                        "You are so kind, considering the feelings of those around you and making sure everyone is having a good time.",
                        "You have a passion for lore of the haunted and undead kinds, opening our eyes to a niche not often explored when you share your knowledge."]
        kat_array = ["You are one of the kindest and gentlest souls I have ever had the pleasure to call a friend.",
                     "You’re razor-sharp smart.",
                     "You are one of the most forward of the group. You try your best to accommodate for others... you're also the Sass Queen.",
                     "A Paragon of Positivity, always trying to solve problems in a healthy manner. You are able to speak your feelings quite well, and you literally threw all of this together so you could collect and read these. "]

        user_arg = ctx.message.mentions[0]
        username = user_arg.name
        
        indarray = []
        if username == "katthesassqueen":
            for i in range(0,100):
                ind = np.random.randint(len(kat_array))
                indarray.append(ind)
            ind = np.random.choice(indarray)
            output = kat_array[ind]
        elif username == "mehttaur":
            for i in range(0,100):
                ind = np.random.randint(len(matt_array))
                indarray.append(ind)
            ind = np.random.choice(indarray)
            output = matt_array[ind]
        elif username == "homeboy64":
            for i in range(0,100):
                ind = np.random.randint(len(homeboy_array))
                indarray.append(ind)
            ind = np.random.choice(indarray)
            output = homeboy_array[ind]
        elif username == "sudsinfinite":
            for i in range(0,100):
                ind = np.random.randint(len(suds_array))
                indarray.append(ind)
            ind = np.random.choice(indarray)
            output = suds_array[ind]
        elif username == "williamoliver11":
            for i in range(0,100):
                ind = np.random.randint(len(will_array))
                indarray.append(ind)
            ind = np.random.choice(indarray)
            output = will_array[ind]
        elif username == "thatrandomskeletor":
            for i in range(0,100):
                ind = np.random.randint(len(skel_array))
                indarray.append(ind)
            ind = np.random.choice(indarray)
            output = skel_array[ind]
        elif username == "daylinkpikmin":
            for i in range(0,100):
                ind = np.random.randint(len(day_array))
                indarray.append(ind)
            ind = np.random.choice(indarray)
            output = day_array[ind]
        elif username == "catgravitywell":
            for i in range(0,100):
                ind = np.random.randint(len(grav_array))
                indarray.append(ind)
            ind = np.random.choice(indarray)
            output = grav_array[ind]
        elif username == "just_joker_":
            for i in range(0,100):
                ind = np.random.randint(len(joker_array))
                indarray.append(ind)
            ind = np.random.choice(indarray)
            output = joker_array[ind]
        elif username == "sarge19":
            for i in range(0,100):
                ind = np.random.randint(len(chris_array))
                indarray.append(ind)
            ind = np.random.choice(indarray)
            output = chris_array[ind]
        elif username == "solarixephos":
            for i in range(0,100):
                ind = np.random.randint(len(fiery_array))
                indarray.append(ind)
            ind = np.random.choice(indarray)
            output = fiery_array[ind]
        elif username == "prcrstnt":
            for i in range(0,100):
                ind = np.random.randint(len(nate_array))
                indarray.append(ind)
            ind = np.random.choice(indarray)
            output = nate_array[ind]
        elif username == "daddyct":
            for i in range(0,100):
                ind = np.random.randint(len(ct_array))
                indarray.append(ind)
            ind = np.random.choice(indarray)
            output = ct_array[ind]
        elif username == "grandtheftzombie":
            for i in range(0,100):
                ind = np.random.randint(len(zombie_array))
                indarray.append(ind)
            ind = np.random.choice(indarray)
            output = zombie_array[ind]
        else:
            for i in range(0,100):
                ind = np.random.randint(len(gen_array))
                indarray.append(ind)
            ind = np.random.choice(indarray)
            output = gen_array[ind]
        await ctx.send(output)
        
    @commands.command(brief="Insults the target.",help="Usage: &&insult @Member\nInsults the target.",aliases=["Insult"])
    async def insult(self,ctx):
        part1 = ["artless","bawdy","beslubbering","bootless","churlish","cockered","clouted","craven","currish",
                 "dankish","dissembling","droning","errant","fawning","fobbing","froward","frothy","gleeking",
                 "goatish","gorbellied","impertinent","infectious","jarring","loggerheaded","lumpish","mammering",
                 "mangled","mewling","paunchy","pribbling","puking","puny","qualling","rank","reeky","roguish",
                 "ruttish","saucy","spleeny","spongy","surly","tottering","unmuzzled","vain","venomed","villainous",
                 "warped","wayward","weedy","yeasty"]
        part2 = ["base-court","bat-fowling","beef-witted","beetle-headed","boil-brained","clapper-clawed",
                 "clay-brained","common-kissing","crook-pated","dismal-dreaming","dizzy-eyed","doghearted",
                 "dread-bolted","earth-vexing","elf-skinned","fat-kidneyed","fen-sucked","flap-mouthed",
                 "fly-bitten","folly-fallen","fool-born","full-gorged","guts-griping","half-faced","hasty-witted",
                 "hedge-born","hell-hated","idle-headed","ill-breeding","ill-nurtured","knotty-pated","milk-livered",
                 "motley-minded","onion-eyed","plume-plucked","pottle-deep","pox-marked","reeling-ripe","rough-hewn",
                 "rude-growing","rump-fed","shard-borne","sheep-biting","spur-galled","swag-bellied","tardy-gaited",
                 "tickle-brained","toad-spotted","unchin-snouted","weather-bitten"]
        part3 = ["apple-john","baggage","barnacle","bladder","boar-pig","bugbear","bum-bailey","canker-blossom",
                 "clack-dish","clotpole","coxcomb","codpiece","death-token","dewberry","flap-dragon","flax-wench",
                 "flirt-gill","foot-licker","fustilarian","giglet","gudgeon","haggard","harpy","hedge-pig",
                 "horn-beast","hugger-mugger","joithead","lewdster","lout","maggot-pie","malt-worm","mammet",
                 "measle","minnow","miscreant","moldwarp","mumble-news","nut-hook","pigeon-egg","pignut",
                 "puttock","pumpion","ratsbane","scut","skainsmate","strumpet","varlot","vassal","whey-face",
                 "wagtail"]
        ind1 = np.random.randint(len(part1))
        ind2 = np.random.randint(len(part2))
        ind3 = np.random.randint(len(part3))
        
        insultstr = "You " + str(part1[ind1]) + " " + str(part2[ind2]) + " " + str(part3[ind3]) + "!"
        await ctx.send(insultstr)
    
class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief="Joins a voice channel", help="Usage: &&join\nJoins a voice channel",aliases=["Join"])
    async def join(self, ctx):
        """Joins a voice channel"""
        try:
            channel = ctx.author.voice.channel
            if ctx.voice_client is not None:
                return await ctx.voice_client.move_to(channel)
        except:
            return await ctx.send("Please connect to a voice channel first.")
            
        await ctx.message.delete()
        await channel.connect(self_deaf=True)
    
    @commands.command(brief="Plays a spotify track", help="Usage: &&spotify <TRACK URL>\nPlays a Spotify track, acts as a skip command.  May play incorrect tracks due to methods.",
                        aliases=["Spotify"])
    async def spotify(self, ctx, url: str = commands.parameter(description="A link to a Spotify track to be played.")):
        """Plays a Spotify track by putting the parameters into a YouTube search.  Also acts as a skip command."""
        track_id_match = re.search(r'track/([a-zA-Z0-9]+)', url)  # Regex search to parse the spotify link
        search_term = ""
        if track_id_match:
            track_id = track_id_match.group(1)
            track = sp.track(track_id)
            search_term = f"{track['name']} - {track['artists'][0]['name']}"
        if search_term != "":
            search = pytube.Search(search_term)
            results = search.results
            if len(results) > 0:
                vid_id = results[0].video_id
                yt_link = "https://www.youtube.com/watch?v=" + str(vid_id)
                await self.yt(ctx, yt_link)
            else:
                await ctx.send("Track not found on YouTube (yes I know it's a spotify link)")
        else:
            await ctx.send("Cannot locate Spotify track.")
 

    @commands.command(brief="Plays an online YouTube audio stream.  Also acts as a skip command.",
                      help="Usage: &&yt <URL>\nPlays an online YouTube audio stream.  Also acts as a skip command.",
                      aliases=["Yt", "YT"])
    async def yt(self, ctx, url: str = commands.parameter(description="A YouTube link for the video to be played.")):
        """Plays an online YouTube audio stream.  Also acts as a skip command."""
        global yt
        yt = "True"
        global loc
        loc = "False"
        global link
        if url != link:
            link = url
            delete = "True"
        else:
            delete = "False"
        global context
        context = ctx
        itag_list = [141,140,139,251,171,250,249]#These are the lists of itags that can be played by ffmpeg.
        for itag in itag_list:
            try:
                audio = pytube.YouTube(str(url)).streams.get_by_itag(itag).url#get stream url
                print("itag: " + str(itag))
                break
            except AttributeError:#cannot find stream by current itag, as itag not avaliable
                continue
        global source
        source = discord.FFmpegPCMAudio(audio, executable="C:\\Users\\advan\\AppData\\Local\\Programs\\Python\\Python313\\Lib\\site-packages\\discord\\ffmpeg\\bin\\ffmpeg.exe",**FFMPEG_OPTIONS)  # converts the youtube audio source into a source discord can use
        source = discord.PCMVolumeTransformer(source,volume=0.5)
        if ctx.voice_client.is_playing():
            await self.stop(ctx)#My own function to stop the bot from playing the music if music is already playing.
        ctx.voice_client.play(source)# play the source
        nowplaystr = "Now Playing! " + str(link)
        if delete == "True":
            await ctx.message.delete()
        await ctx.send(nowplaystr)
        if not self.playagain.is_running():
            await self.playagain.start()
     
    @tasks.loop(seconds=5.0)
    async def playagain(self):
        if yt=="True" and loopsong=="True":
            if not context.voice_client.is_playing():
                await self.yt(context,link)
        elif loc=="True" and loopsong=="True":
            if not context.voice_client.is_playing():
                await self.local(context,link)
        
    @commands.command(brief="Plays a local file.  Also acts as a skip command.",
                      help="Usage: &&local filepath\nPlays a local file.  Also acts as a skip command.",
                      aliases=["Local"])
    async def local(self,ctx,filepath: str = commands.parameter(description="The path to the file on your local computer (ex: C:/Music/filehere.mp3)")):
        """Plays a local file.  Also acts as a skip command."""
        global loc
        loc = "True"
        global yt
        yt = "False"
        global link
        link = filepath
        global context
        context = ctx
        FFMPEG_OPTIONS = {'options': '-vn -filter:a "volume=0.1"'}#optimised settings for ffmpeg for streaming
        global source
        source = discord.FFmpegPCMAudio(filepath,executable="C:\\Users\\advan\\AppData\\Local\\Programs\\Python\\Python313\\Lib\\site-packages\\discord\\ffmpeg\\bin\\ffmpeg.exe",**FFMPEG_OPTIONS)
        source = discord.PCMVolumeTransformer(source,volume=0.5)
        if ctx.voice_client.is_playing():
            await self.stop(ctx)#My own function to stop the bot from playing the music if music is already playing.
        ctx.voice_client.play(source)# play the source
        nowplaystr = "Now Playing! " + str(link)
        await ctx.message.delete()
        await ctx.send(nowplaystr)
        if not self.playagain.is_running():
            await self.playagain.start()
        
    @commands.command(brief="Repeats the current track, unless a new track is added.",
                      help="Usage: &&repeat arg\nRepeats the current track, unless a new track is added.",
                      aliases=["Repeat"])
    async def repeat(self,ctx,arg: str = commands.parameter(description="Whether the bot is repeating or not ('on' or 'off')")):
        """Repeats the current track, unless a new track is added."""
        global loopsong
        if arg == "on":
            loopsong = "True"
            await ctx.message.delete()
            await ctx.send("Repeat on!")
        else:
            loopsong = "False"
            await ctx.message.delete()
            await ctx.send("Repeat off!")
            
    @commands.command(brief="Displays the link or path for the current song.",
                      help="Usage: &&nowplaying\nDisplays the link or path for the current song.",
                      aliases=["Nowplaying"])
    async def nowplaying(self,ctx):
        nowplaystr = "Now Playing! " + str(link)
        if ctx.message:
            await ctx.message.delete()
        await ctx.send(nowplaystr)
         
    @commands.command(brief="Stops and disconnects the bot from voice",help="Usage: &&stop\nStops and disconnects the bot from voice",
                      aliases=["Stop","leave","Leave"])
    async def stop(self, ctx):
        """Stops and disconnects the bot from voice"""
        global loopsong
        loopsong = "False"
        global loc
        loc = "False"
        global yt
        yt = "False"
        global link
        link = ""
        global context
        context = ""
        global source
        source = ""
        await ctx.message.delete()
        await ctx.voice_client.disconnect()
        await ctx.send("Disconnected from voice! Have a great day!")
        
    @commands.command(brief="Changes the volume of the source.",help="Usage: &&volume <vol>\nChanges the volume of the source.",
                      aliases=["Volume"])
    async def volume(self,ctx,vol: float = commands.parameter(description="The volume of the bot, as a decimal that represents a percent. (Ex: 0.5 = 50%)")):
        global source
        source.volume = vol
        volstr = "Volume set to " + str(vol * 100) + "%"
        await ctx.message.delete()
        await ctx.send(volstr)

    @local.before_invoke
    @yt.before_invoke
    async def ensure_voice(self, ctx):
        if ctx.voice_client is None:
            if ctx.author.voice:
                await ctx.author.voice.channel.connect()
            else:
                await ctx.send("You are not connected to a voice channel.")
                raise commands.CommandError("Author not connected to a voice channel.")
        elif ctx.voice_client.is_playing():
            ctx.voice_client.stop()

class Roll(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    def rolldice(dtype):
        randnum = np.random.randint(dtype)
        diceroll = randnum + 1
        return diceroll
        
    def rolldice_er(dtype):
        dicearray = []
        for i in range(0,50):
            randint = np.random.randint(dtype)
            dicearray.append(randint + 1)
            randfloat = math.floor(dtype*(np.random.random())) + 1
            dicearray.append(randfloat)
    
        diceroll = np.random.choice(dicearray)
        return diceroll   
    
    @commands.command(help="Usage: &&roll <dice string>\n<dice string> can be any combination of #d# + #, with adv or dis on the end.\nEx: &&roll 2d4+5d10-3d6+7 adv\nDOES NOT SUPPORT MULTIPLICATION OR DIVISION AT THIS POINT",
                      brief="Rolls the dice as indicated.",
                      aliases=["Roll"])
    async def roll(self, ctx):
        """Rolls the dice as indicated."""
        member = ctx.author
        message = re.split(r'[\+\-\(\)\s\*/]+',ctx.message.content)
        all_rolls = []
        total = 0
        outstr = f'{member.mention}\n**Result:** '
        outstrend = ""
        ending = message[-1]
        
        modlist = []
        for i in message:
            try:
                mod = int(i)
                modlist.append(mod)
            except ValueError:
                continue
        
        firstind = len(message[1])+7   
        for x in range(0,len(modlist)):
            firstind += ctx.message.content[firstind:].find(str(modlist[x]))
            if (ctx.message.content[firstind - 1] == "-") or (ctx.message.content[firstind - 2] == "-"):
                total -= modlist[x]
                outstrend += " - " + str(modlist[x])
            elif (ctx.message.content[firstind - 1] == "+") or (ctx.message.content[firstind - 2] == "+"):
                total += modlist[x]
                outstrend += " + " + str(modlist[x])
            firstind += len(str(modlist[x]))
        
        if ending == "adv" or ending == "dis":
            total1 = 0
            total2 = 0
            allrolls1 = []
            allrolls2 = []
            outstr1 = ""
            outstr2 = ""
            for k in range(0,2):
                dicelist = filter(lambda x: ("d" in x),message)
                for i in dicelist:
                    if i != "adv" and i != "dis":
                        dstring = i.split("d")
                        num = dstring[0]
                        dtype = int(dstring[1])
                        sign_ind = ctx.message.content.find(i)
                        if (ctx.message.content[sign_ind - 1] == "-") or (ctx.message.content[sign_ind - 2] == "-"):
                            if k == 0:
                                outstr1 += " - " + i + " ("
                            else:
                                outstr2 += " - " + i + " ("
                            roll_list = []
                            for j in range(0,int(num)):
                                diceroll = Roll.rolldice(dtype)
                                roll_list.append(diceroll)
                                if k == 0:
                                    total1 -= diceroll
                                else:
                                    total2 -= diceroll
                                if diceroll == 1 or diceroll == dtype:
                                    if k == 0:
                                        outstr1 += "**" + str(diceroll) + "**"
                                    else:
                                        outstr2 += "**" + str(diceroll) + "**"
                                else:
                                    if k == 0:
                                        outstr1 += str(diceroll)
                                    else:
                                        outstr2 += str(diceroll)
                                if j < (int(num) - 1):
                                    if k == 0:
                                        outstr1 += ","
                                    else:
                                        outstr2 += ","
                            if k == 0:            
                                allrolls1.append(roll_list)
                                outstr1 += ") "
                            else:
                                allrolls2.append(roll_list)
                                outstr2 += ") "
                        
                        else:
                            if (ctx.message.content[sign_ind - 1] == "+") or (ctx.message.content[sign_ind - 2] == "+"):
                                if k == 0:
                                    outstr1 += " + "
                                else:
                                    outstr2 += " + "
                            if k == 0:
                                outstr1 += i + " ("
                            else:
                                outstr2 += i + " ("
                            roll_list = []
                            for j in range(0,int(num)):
                                diceroll = Roll.rolldice(dtype)
                                roll_list.append(diceroll)
                                if k == 0:
                                    total1 += diceroll
                                else:
                                    total2 += diceroll
                                if diceroll == 1 or diceroll == dtype:
                                    if k == 0:
                                        outstr1 += "**" + str(diceroll) + "**"
                                    else:
                                        outstr2 += "**" + str(diceroll) + "**"
                                else:
                                    if k == 0:
                                        outstr1 += str(diceroll)
                                    else:
                                        outstr2 += str(diceroll)
                                if j < (int(num) - 1):
                                    if k == 0:
                                        outstr1 += ","
                                    else:
                                        outstr2 += ","
                            if k == 0:            
                                allrolls1.append(roll_list)
                                outstr1 += ") "
                            else:
                                allrolls2.append(roll_list)
                                outstr2 += ") "
            # TODO: Add support for * and /
            if (total1 >= total2 and ending=="adv") or (total1<= total2 and ending=="dis"):
                total += total1
                outstr = outstr1
                reject = total2
                rejectstr = outstr2
            else:
                total += total2
                outstr = outstr2
                reject = total1
                rejectstr = outstr1
            totalstr = "~~" + rejectstr + "~~" + outstrend + " = " + str(total)
            outstr += totalstr
            await ctx.message.delete()
            await ctx.send(outstr) #Replace this with results!
        else:
            dicelist = filter(lambda x: ("d" in x),message)
            for i in dicelist:
                dstring = i.split("d")
                num = dstring[0]
                dtype = int(dstring[1])
                sign_ind = ctx.message.content.find(i)
                if (ctx.message.content[sign_ind - 1] == "-") or (ctx.message.content[sign_ind - 2] == "-"):
                    outstr += " - " + i + " ("
                    roll_list = []
                    for j in range(0,int(num)):
                        diceroll = Roll.rolldice(dtype)
                        roll_list.append(diceroll)
                        total -= diceroll
                        if diceroll == 1 or diceroll == dtype:
                            outstr += "**" + str(diceroll) + "**"
                        else:
                            outstr += str(diceroll)
                        if j < (int(num) - 1):
                            outstr += ","
                    all_rolls.append(roll_list)
                    outstr += ") "
                    
                else:
                    if (ctx.message.content[sign_ind - 1] == "+") or (ctx.message.content[sign_ind - 2] == "+"):
                        outstr += " + "
                    outstr += i + " ("
                    roll_list = []
                    for j in range(0,int(num)):
                        diceroll = Roll.rolldice(dtype)
                        roll_list.append(diceroll)
                        total += diceroll
                        if diceroll == 1 or diceroll == dtype:
                            outstr += "**" + str(diceroll) + "**"
                        else:
                            outstr += str(diceroll)
                        if j < (int(num) - 1):
                            outstr += ","
                    all_rolls.append(roll_list)
                    outstr += ") "
            # TODO: Add support for * and /
            totalstr = outstrend + " = " + str(total)
            outstr += totalstr
            await ctx.message.delete()
            await ctx.send(outstr) #Replace this with results!
            
            
    @commands.command(help="Usage: &&roller <dice string>\n<dice string> can be any combination of #d# + #, with adv or dis on the end.\nEx: &&roller 2d4+5d10-3d6+7 adv\nDOES NOT SUPPORT MULTIPLICATION OR DIVISION AT THIS POINT",
                      brief="Rolls the dice as indicated, with extra randomness (the result is randomly chosen from 100 rolls!)",
                      aliases=["Roller"])
    async def roller(self, ctx):
        """Rolls the dice, but extra random!"""
        member = ctx.author
        message = re.split(r'[\+\-\(\)\s\*/]+',ctx.message.content)
        all_rolls = []
        total = 0
        outstr = f'{member.mention}\n**Result:** '
        outstrend = ""
        ending = message[-1]
        
        modlist = []
        
        for i in message:
            try:
                mod = int(i)
                modlist.append(mod)
            except ValueError:
                continue
        
        firstind = len(message[1])+9   
        for x in range(0,len(modlist)):
            firstind += ctx.message.content[firstind:].find(str(modlist[x]))
            if (ctx.message.content[firstind - 1] == "-") or (ctx.message.content[firstind - 2] == "-"):
                total -= modlist[x]
                outstrend += " - " + str(modlist[x])
            elif (ctx.message.content[firstind - 1] == "+") or (ctx.message.content[firstind - 2] == "+"):
                total += modlist[x]
                outstrend += " + " + str(modlist[x])
            firstind += len(str(modlist[x]))
        
        if ending == "adv" or ending == "dis":
            total1 = 0
            total2 = 0
            allrolls1 = []
            allrolls2 = []
            outstr1 = ""
            outstr2 = ""
            for k in range(0,2):
                dicelist = filter(lambda x: ("d" in x),message)
                for i in dicelist:
                    if i != "adv" and i != "dis":
                        dstring = i.split("d")
                        num = dstring[0]
                        dtype = int(dstring[1])
                        sign_ind = ctx.message.content.find(i)
                        if (ctx.message.content[sign_ind - 1] == "-") or (ctx.message.content[sign_ind - 2] == "-"):
                            if k == 0:
                                outstr1 += " - " + i + " ("
                            else:
                                outstr2 += " - " + i + " ("
                            roll_list = []
                            for j in range(0,int(num)):
                                diceroll = Roll.rolldice_er(dtype)
                                roll_list.append(diceroll)
                                if k == 0:
                                    total1 -= diceroll
                                else:
                                    total2 -= diceroll
                                if diceroll == 1 or diceroll == dtype:
                                    if k == 0:
                                        outstr1 += "**" + str(diceroll) + "**"
                                    else:
                                        outstr2 += "**" + str(diceroll) + "**"
                                else:
                                    if k == 0:
                                        outstr1 += str(diceroll)
                                    else:
                                        outstr2 += str(diceroll)
                                if j < (int(num) - 1):
                                    if k == 0:
                                        outstr1 += ","
                                    else:
                                        outstr2 += ","
                            if k == 0:            
                                allrolls1.append(roll_list)
                                outstr1 += ") "
                            else:
                                allrolls2.append(roll_list)
                                outstr2 += ") "
                        
                        else:
                            if (ctx.message.content[sign_ind - 1] == "+") or (ctx.message.content[sign_ind - 2] == "+"):
                                if k == 0:
                                    outstr1 += " + "
                                else:
                                    outstr2 += " + "
                            if k == 0:
                                outstr1 += i + " ("
                            else:
                                outstr2 += i + " ("
                            roll_list = []
                            for j in range(0,int(num)):
                                diceroll = Roll.rolldice_er(dtype)
                                roll_list.append(diceroll)
                                if k == 0:
                                    total1 += diceroll
                                else:
                                    total2 += diceroll
                                if diceroll == 1 or diceroll == dtype:
                                    if k == 0:
                                        outstr1 += "**" + str(diceroll) + "**"
                                    else:
                                        outstr2 += "**" + str(diceroll) + "**"
                                else:
                                    if k == 0:
                                        outstr1 += str(diceroll)
                                    else:
                                        outstr2 += str(diceroll)
                                if j < (int(num) - 1):
                                    if k == 0:
                                        outstr1 += ","
                                    else:
                                        outstr2 += ","
                            if k == 0:            
                                allrolls1.append(roll_list)
                                outstr1 += ") "
                            else:
                                allrolls2.append(roll_list)
                                outstr2 += ") "
            # TODO: Add support for * and /
            if (total1 >= total2 and ending=="adv") or (total1<= total2 and ending=="dis"):
                total += total1
                outstr = outstr1
                reject = total2
                rejectstr = outstr2
            else:
                total += total2
                outstr = outstr2
                reject = total1
                rejectstr = outstr1
            totalstr = "~~" + rejectstr + "~~" + outstrend + " = " + str(total)
            outstr += totalstr
            await ctx.message.delete()
            await ctx.send(outstr) #Replace this with results!
        else:
            dicelist = filter(lambda x: ("d" in x),message)
            for i in dicelist:
                dstring = i.split("d")
                num = dstring[0]
                dtype = int(dstring[1])
                sign_ind = ctx.message.content.find(i)
                if (ctx.message.content[sign_ind - 1] == "-") or (ctx.message.content[sign_ind - 2] == "-"):
                    outstr += " - " + i + " ("
                    roll_list = []
                    for j in range(0,int(num)):
                        diceroll = Roll.rolldice_er(dtype)
                        roll_list.append(diceroll)
                        total -= diceroll
                        if diceroll == 1 or diceroll == dtype:
                            outstr += "**" + str(diceroll) + "**"
                        else:
                            outstr += str(diceroll)
                        if j < (int(num) - 1):
                            outstr += ","
                    all_rolls.append(roll_list)
                    outstr += ") "
                    
                else:
                    if (ctx.message.content[sign_ind - 1] == "+") or (ctx.message.content[sign_ind - 2] == "+"):
                        outstr += " + "
                    outstr += i + " ("
                    roll_list = []
                    for j in range(0,int(num)):
                        diceroll = Roll.rolldice_er(dtype)
                        roll_list.append(diceroll)
                        total += diceroll
                        if diceroll == 1 or diceroll == dtype:
                            outstr += "**" + str(diceroll) + "**"
                        else:
                            outstr += str(diceroll)
                        if j < (int(num) - 1):
                            outstr += ","
                    all_rolls.append(roll_list)
                    outstr += ") "
            # TODO: Add support for * and /
            totalstr = outstrend + " = " + str(total)
            outstr += totalstr
            await ctx.message.delete()
            await ctx.send(outstr) #Replace this with results!
            
            
    @commands.command(brief="Rolls stats based on the chosen method.",
                      help="Usage: &&rollstats <method>\nRolls stats based on the chosen method.",
                      aliases=["Rollstats"])
    async def rollstats(self,ctx,method: str = commands.parameter(description="The method of stats rolling (must be 4d6 or 1d20)")):
        rolltypestr = "Rolling stats using " + method + "!"
        if method == "4d6":
            dtype = 6
            rollsave = [] # For printing output
            total = []
            for i in range(0,6):
                minnum = 10
                minarray = 0
                dicearray = []
                for j in range(0,4):
                    roll = np.random.randint(dtype) + 1
                    dicearray.append(roll)
                    if roll < minnum:
                        minnum = roll
                        minarray = j
                discard = min(dicearray)
                discard_index = minarray
                rollstr = ""
                totalroll = 0
                for j in range(0,4):
                    if j == discard_index:
                        if dicearray[j] == 1 or dicearray[j] == dtype:
                            rollstr += "~~**" + str(dicearray[j]) + "**~~"
                        else:
                            rollstr += "~~" + str(dicearray[j]) + "~~"
                    else:
                        if dicearray[j] == 1 or dicearray[j] == dtype:
                            rollstr += "**" + str(dicearray[j]) + "**"
                        else:
                            rollstr += str(dicearray[j])
                        totalroll += dicearray[j]
                    if j < 3:
                        rollstr += ", "
                rollsave.append(rollstr)
                total.append(totalroll)
        elif method == "1d20":
            dtype = 20
            rollsave = []
            total = []
            for i in range(0,6):
                roll = np.random.randint(dtype) + 1
                if roll == 1 or roll == dtype:
                    rollsave.append("**" + str(roll) + "**")
                else:
                    rollsave.append(roll)
                total.append(roll)
                
        outstr = f'{ctx.author.mention}\n' + rolltypestr + '\n**Result:**\n'
        for i in range(0,len(rollsave)):
            outstr += str(rollsave[i]) + " = " + str(total[i])
            if i < len(rollsave)-1:
                outstr += "\n"
        await ctx.message.delete()
        await ctx.send(outstr)
        
        
    @commands.command(brief="Rolls stats based on the chosen method, with extra randomness.",
                      help="Usage: &&rollstats <method>\nRolls stats based on the chosen method, with extra randomness.",
                      aliases=["Rollstatser"])
    async def rollstatser(self,ctx,method: str = commands.parameter(description="The method of stats rolling (must be 4d6 or 1d20)")):
        rolltypestr = "Rolling stats using " + method + "!"
        if method == "4d6":
            dtype = 6
            rollsave = [] # For printing output
            total = []
            for i in range(0,6):
                minnum = 10
                minarray = 0
                dicearray = []
                for j in range(0,4):
                    roll = Roll.rolldice_er(dtype)
                    dicearray.append(roll)
                    if roll < minnum:
                        minnum = roll
                        minarray = j
                discard = min(dicearray)
                discard_index = minarray
                rollstr = ""
                totalroll = 0
                for j in range(0,4):
                    if j == discard_index:
                        if dicearray[j] == 1 or dicearray[j] == dtype:
                            rollstr += "~~**" + str(dicearray[j]) + "**~~"
                        else:
                            rollstr += "~~" + str(dicearray[j]) + "~~"
                    else:
                        if dicearray[j] == 1 or dicearray[j] == dtype:
                            rollstr += "**" + str(dicearray[j]) + "**"
                        else:
                            rollstr += str(dicearray[j])
                        totalroll += dicearray[j]
                    if j < 3:
                        rollstr += ", "
                rollsave.append(rollstr)
                total.append(totalroll)
        elif method == "1d20":
            dtype = 20
            rollsave = []
            total = []
            for i in range(0,6):
                roll = Roll.rolldice_er(dtype)
                if roll == 1 or roll == dtype:
                    rollsave.append("**" + str(roll) + "**")
                else:
                    rollsave.append(roll)
                total.append(roll)
                
        outstr = f'{ctx.author.mention}\n' + rolltypestr + '\n**Result:**\n'
        for i in range(0,len(rollsave)):
            outstr += str(rollsave[i]) + " = " + str(total[i])
            if i < len(rollsave)-1:
                outstr += "\n"
        await ctx.message.delete()
        await ctx.send(outstr)


intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True

bot = commands.Bot(
    command_prefix=commands.when_mentioned_or("&&"),
    description='A dice bot and more made by Kat',
    activity=discord.CustomActivity(name="&&help || Dice, Music, and More!"),
    intents=intents,
)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')
    await bot.add_cog(Music(bot))
    await bot.add_cog(Roll(bot))
    await bot.add_cog(Greet(bot))

bot.run("[INSERT YOUR BOT TOKEN HERE]")  # Yup you can run your own instance by generating your own.
# Or if you're Maya you've got my token already.
