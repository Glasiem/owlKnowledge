from owlready2 import *

onto = get_ontology("http://test.org/onto.owl")

with onto:
    class Artist(Thing):
       label = ["artist"]

    class Album(Thing):
        label = ["album"]

    class Song(Thing):
        label = ["song"]
               

    class singAsong(Artist >> Song):
        python_name = "songs"
        label = ["sing songs"]    

    class performedBy(Song >> Artist):
        python_name = "performedBy"    
        inverse_property = singAsong

        label = ["performed by"]

    class songsInAlbum(Album >> Song):
        python_name = "songsInAlbum"  
        label = ["songs in album"]

    class inAlbum(Song >> Album):
        python_name = "inAlbum"  
        inverse_property = songsInAlbum

        label = ["in album"]  

    class makeAnAlbum(Artist >> Album):
        python_name = "albums"
        label = ["made albums"]  

    class madeBy(Album >> Artist):
        python_name = "artists" 
        inverse_property = makeAnAlbum
   
        label = ["made by"]

    class Collab(Song):
        equivalent_to = [Song & performedBy.min(2, Artist) & inAlbum.some(Album)]
        label = ["collab song"]

    class CollabAlbum(Album):
        equivalent_to = [Album & madeBy.min(2, Artist) & songsInAlbum.some(Song)]
        label = ["collab album"]

    class Single(Album):
        equivalent_to = [Album & songsInAlbum.exactly(1, Song) & madeBy.some(Artist)]
        label = ["single"]

    class OneHitWonder(Artist):
        equivalent_to = [Artist & singAsong.exactly(1, Song) & makeAnAlbum.some(Album)]
        label = ["one hit wonder"]

    class ManyCoolTracks(Artist):
        equivalent_to = [Artist & singAsong.min(3, Song) & makeAnAlbum.some(Album)]
        label = ["has a lot of cool tracks"]

    song1 = Song(name="Kizuna_No_Kiseki")
    song2 = Song(name="Dark_Crow")
    song3 = Song(name="My_Hero[Slushii_Remix]")
    song4 = Song(name="Sl0t")
    song5 = Song(name="RTRT")
    song6 = Song(name="world.execute(me);")

    album1 = Album(songsInAlbum = [song1], name="Kizuna_No_Kiseki(album)")
    album2 = Album(songsInAlbum = [song2,song3], name="Dark_Crow(album)")
    album3 = Album(songsInAlbum = [song4,song5,song6], name="Miracle_Milk")

    artist1 = Artist(songs = [song1], albums = [album1], name="milet")
    artist2 = Artist(songs = [song1, song2, song3], albums = [album1,album2], name="MAN_WITH_A_MISSION")
    artist3 = Artist(songs = [song4,song5,song6], albums = [album3], name="Mili")

    AllDifferent([song1,song2,song3,song4,song5,song6])
    AllDifferent([album1,album2,album3])
    AllDifferent([artist1,artist2,artist3])
    
    close_world(Song)
    close_world(Artist)

onto.save("onto.owl")







