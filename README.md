
# haha
Access a joke (or more) through python.

And what funnier joke than... 
Thor (for millennials), or Chuck Norris (for the X-gen).

But really, you can choose your own name to use in the joke.

Disclaimer: I say "joke", but don't make any promises on any of them actually being funny.

# Examples

On your first import, it will print a random joke
taken from [api.chucknorris.io], 
but replacing the name with "Thor", to fit with the times.

```pydocstring
>>> import haha  
Read! its what smart people do! but not Thor. He already is smart enough.
```

But you can choose your own name to mock.
Let's say, "Chuck Norris" (the actual original name used in the source database).

```pydocstring
>>> from haha import NamedJokes
>>> joke_gen = NamedJokes('Chuck Norris')  # make a joke with any name
>>> joke_gen()
'Chuck Norris is, and has always been where it's at.''
>>> joke_gen(search_term='airplane')  # you can specify a (single) word to filter the random joke
'Chuck Norris invented airplanes because he was tired of being the only person that could fly.'
```

You can specify a (single) word to filter the random joke.

```pydocstring
>>> joke_gen(search_term='airplane') 
```

```
MacGyver can build an airplane out of gum and paper clips. Chuck Norris can kill him and take it.

MacGyver can build an airplane out of gum and paper clips, but Chuck Norris can roundhouse-kick his head through a wall and take it.

911 happened when Chuck Norris threw a paper airplane

Chuck Norris never uses parachutes when he skydives out of airplanes because they only slow him down.

Before the Wright brothers made the first airplane, Chuck Norris had already invented the rocket and flown to Pluto, where he lived for 20 years.........naked

Chuck Norris invented airplanes because he was tired of being the only person that could fly.

September 11, 2001- The World Paper Airplane Throwing Championships were held in California...Chuck Norris won when his 4 best throws landed somewhere on the East Coast.

Chuck Norris can fly on an airplane to Maine from Hawaii in 30 seconds. he just has to tell the pilot to move over...

Chuck Norris doesn't use an airplane for travel, he simply turns of the gravity and farts

Chuck Norris dosent use airplanes to get to other countries, he just jumps from one continent to another.
```

