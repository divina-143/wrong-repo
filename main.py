
from pyscript import display, document

# blue lock player database
placeholder = {
    "ISG": ("Yoichi Isagi", "Team Z", "Direct Shot"),
    "BAC": ("Meguru Bachira", "Team Z", "Monster Dribbling"),
    "CHI": ("Hyoma Chigiri", "Team Z", "Explosive Speed"),
    "KUN": ("Rensuke Kunigami", "Team Z", "Powerful Shooting"),
    "NAG": ("Seishiro Nagi", "Team V", "Ball Control"),
    "REO": ("Reo Mikage", "Team V", "Copy Ability"),
    "RIN": ("Rin Itoshi", "Team A", "Precision Shooting"),
    "BAR": ("Shoei Barou", "Team X", "Predator Instinct")
}


def element_checker(e):

    # get the player's code
    document.getElementById("result").innerHTML = " "
    element1 = document.getElementById(
        "element_Name"
    ).value.strip().upper()

    # search for the player
    result = placeholder.get(
        element1, ("Player not found", "-", "-")
    )

    # display player information
    document.getElementById("result").innerHTML = f"""
        <div class="player-card">
            <h3>BLUE LOCK PLAYER PROFILE</h3>
            <b>Player Code:</b> {element1}<br>
            <b>Player Name:</b> {result[0]}<br>
            <b>Team:</b> {result[1]}<br>
            <b>Weapon:</b> {result[2]}<br>
        </div>
    """
