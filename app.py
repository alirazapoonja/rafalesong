import streamlit as st # type: ignore

song_lyrics = {
    "Jimmy Jimmy Aja Aja": "Rafale Aaja Aaja Aaja, Rafale gir ja gir ja, Aaja Pakistan mere saath, hum jaigay aadi raat, Pukare pataka ki dun, Suna de wohi dhun, Aise crash tu howa kyun, Khamoshi tod de, china kya thunder sai haar ke, France chor de. ",
    "Doston Tum Sabko": "Doston tum sabko ye shaam mubarak ho, rafale ko rafale ka pataka mubarak ho, Aise rafale roz kahan milte hain, Aise  pataka sirf france mein khilte hain, Arey.. thunder tum jaisa kaun hain koi nahin",
    "Rote Hue Aate Hai Sab": "rafale hotay hue aate hai.n sab, ha.nsataa huaa thunder jo aaegaa, Vo france ka pataka kahalaaegaa",
    "Zindagi Pyar Ka Geet Hai": "rafale france ka piece hai, Ise har pataka main istemal karna padegaa",
    "Saat samundar paar": "Saat samundar paar main rafale lanay ter Peechhe peechhe a gai, thunder main china ki pehchan, Pakistan main rafale lanay agai",
    "Sandeshe Aate Hain": "rafale Aate Hain, Hum gi rahtah Hain, To pataka Aatha Hai, To Poochh Jaati Hai, rafale dobar kab Aaoge, rafale dobar kab Aaoge, batao Kab Aaoge, Ki Tum Bin Ye thunder Soona Soona Hai ",
    "Waka Waka": "france ka rafale bar bar gira gira, This time for India, If you get down, get up, oh-oh, When you get down, get up, eh-eh, france ka rafale bar bar gira gira, This time for India.  ",
    "C'Est La Vie": "wo bataoo sai wo bataoo sai india sai rafale nai chalti,",
    "John jaani janardan": "Operation hum nai kareya, naam nawaz sharif ka, india nai ki sab industries band, tara-ram-pam-pam-pam-pam  ",
    "Aap Jaisa Koi ": "Aap Jaisa Koi rafale Pakistan Mein Aaiay, Pakistan strong Bun Jai"
    
}
# App title
st.title("🎶 Rafale Song Lyrics")

st.write("Click on a song button to view its lyrics:")

# Loop through the dictionary and create a button for each song
for song_title, lyrics in song_lyrics.items():
    if st.button(song_title):
        st.success(lyrics)

