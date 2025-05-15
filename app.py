import streamlit as st # type: ignore

song_lyrics = {
    "Jimmy Jimmy Aja Aja": "Rafale Aaja Aaja Aaja, Rafale gir ja gir ja, Aaja Pakistan mere saath, hum jaigay aadi raat, Pukare pataka ki dun, Suna de wohi dhun, Aise crash tu howa kyun, Khamoshi tod de, china kya thunder sai haar ke, France chor de. ",
    "Doston Tum Sabko": "Doston tum sabko ye shaam mubarak ho, rafale ko rafale ka pataka mubarak ho, Aise rafale roz kahan milte hain, Aise  pataka sirf france mein khilte hain, Arey.. thunder tum jaisa kaun hain koi nahin",
    "Rote Hue Aate Hai Sab": "rafale hotay hue aate hai.n sab, ha.nsataa huaa thunder jo aaegaa, Vo france ka pataka kahalaaegaa",
    "Zindagi Pyar Ka Geet Hai": "rafale france ka piece hai, Ise har pataka main istemal karna padegaa",
    "Saat samundar paar": "Saat samundar paar main rafale tere Peechhe peechhe a gai, thunder main china ki pehchan, Pakistan main rafale gi ranay agai",
    "Sandeshe Aate Hain": "rafale Aate Hain, Hum gi rahtah Hain, To pataka Aatha Hai, To Poochh Jaati Hai, rafale dobar kab Aaoge, rafale dobar kab Aaoge, batao Kab Aaoge, Ki Tum Bin Ye thunder Soona Soona Hai ",
    "Song 7": "Lyrics of Song 7: ...",
    "Song 8": "Lyrics of Song 8: ..",
    "Song 9": "Lyrics of Song 9: ",
    "Song 10": "Lyrics of Song 10: !"
}
# App title
st.title("🎶 Rafale Song Lyrics")

st.write("Click on a song button to view its lyrics:")

# Loop through the dictionary and create a button for each song
for song_title, lyrics in song_lyrics.items():
    if st.button(song_title):
        st.success(lyrics)

