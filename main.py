import eyed3
from PIL import Image
import time


def check_file(to_input):

    while True:

        try:
            path = input(to_input+": ")
            _ = open(path)

        except FileNotFoundError:
            print(f"File Not Found: {path}")

        else:
            return path


def initalize(path):
    audiofile = eyed3.load(path)
    return audiofile


def set_album_art(audiofile, conformation):
    
    if conformation:
        path = check_file("Enter the Album Art path")

        if "jpg" in path:
            audiofile.tag.images.set(3, open(path, "rb").read(), "images/jpeg")
        else:
            audiofile.tag.images.set(3, open(final_path, "rb").read(), "images/png")

        audiofile.tag.save()

    
def handle_edit_requests(audiofile, artist, album, album_artist, title, track_num, genre):

    if artist == "":
        artist = audiofile.tag.artist
    
    if album == "":
        album = audiofile.tag.album

    if album_artist == "":
        album_artist = audiofile.tag.album_artist

    if title == "":
        title = audiofile.tag.title
    
    if track_num == "":
        track_num = audiofile.tag.track_num

    if genre == "":
        genre = audiofile.tag.genre

    return (artist, album, album_artist, title, track_num, genre)


def edit_audiofile(audiofile, artist, album, album_artist, title, track_num, genre):
    audiofile.tag.artist = artist
    audiofile.tag.album = album
    audiofile.tag.album_artist = album_artist 
    audiofile.tag.title = title
    audiofile.tag.track_num = track_num
    audiofile.tag.genre = genre
    audiofile.tag.save()


if __name__ == "__main__":

    path = check_file("Enter the Audio path")
    print("\n")
    audiofile = initalize(path)

    print("Just press enter and leave the field empty if you dont want any alteration in that field.")

    artist = input("Enter Artist: ")
    album = input("Enter Album: ")
    album_artist = input("Enter Album Artist: ")
    title = input("Enter Title: ")
    track_num = input("Enter Track Number: ")
    genre = input("Enter Genre Id: ")

    print("\n")

    album_art = input("Do you want to change the album art image? (Yes or No): ").lower()
    if album_art[0] == "y":
        set_album_art(audiofile, True)

    handled_requests = handle_edit_requests(audiofile, artist, album, album_artist, title, track_num, genre)
    artist, album, album_artist, title, track_num, genre = handled_requests
    edit_audiofile(audiofile, artist, album, album_artist, title, track_num, genre)
    print("Completing...")
    time.sleep(3)
    print("Done")
