from flask import Blueprint, render_template, session, redirect, request, current_app, url_for, abort
from music_library.forms import MusicForm
from music_library.models import Song
import uuid
from dataclasses import asdict

pages = Blueprint(
    "pages", __name__, template_folder="templates", static_folder="static"
)



@pages.route("/")
def index():
    song_data = current_app.db.songList.find({})
    songs = [Song(**song) for song in song_data]
    return render_template(
        "index.html",
        title="Music Review List",
        songs=songs
    )

@pages.route("/add", methods=["GET", "POST"])
def add_song():
    form = MusicForm()


    if form.validate_on_submit():
        song = Song(
            _id = uuid.uuid4().hex,
            name = form.name.data,
            author = form.author.data,
            album = form.album.data,
            genre = form.genre.data
        )

        current_app.db.songList.insert_one(asdict(song))

        return redirect(url_for(".index"))

    return render_template("new_song.html", title="Music Review List - Add Song", form=form)


@pages.get("/song/<string:_id>")
def song(_id: str):
    song_data = current_app.db.songList.find_one({"_id": _id})
    if not song_data:
        abort(404)
    song = Song(**song_data)
    return render_template("song_details.html", song=song )


@pages.get("/toggle-theme")
def toggle():
    current_theme = session.get("theme")
    if current_theme == "dark":
        session["theme"] = "light"
    else:
        session["theme"] = "dark"


    return redirect(request.args.get("current_page"))