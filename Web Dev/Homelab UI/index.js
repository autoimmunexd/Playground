document.body.onload = addCards;

json = [
    {
        "appname": "radarr",
        "picture": "radarr.png",
        "status": "paused",
        "port": 8989
    },
    {
        "appname": "sonarr",
        "picture": "sonarr.png",
        "status": "stopped",
        "port": 8989
    },
    {
        "appname": "sonarr",
        "picture": "sonarr.png",
        "status": "stopped",
        "port": 8989
    },
    {
        "appname": "sonarr",
        "picture": "sonarr.png",
        "status": "stopped",
        "port": 8989
    },
    {
        "appname": "sonarr",
        "picture": "sonarr.png",
        "status": "stopped",
        "port": 8989
    },
    {
        "appname": "sonarr",
        "picture": "sonarr.png",
        "status": "stopped",
        "port": 8989
    }
]

function addCards() {
    for (const app of json) {
        // Create a new div element with the class card
        const newDiv = document.createElement("div");
        newDiv.setAttribute("class", "card");

        // Create and set attributes for name element
        const nameElement = document.createElement("h1");
        nameElement.setAttribute("class", "card-name");
        nameElement.textContent = app.name;

        // Create and set attributes for picture element
        const pictureElement = document.createElement("img");
        pictureElement.setAttribute("class", "card-icon");
        pictureElement.setAttribute("src", app.picture);
        pictureElement.setAttribute("alt", `${app.name} Icon`);

        // Create and set attributes for status element
        const statusElement = document.createElement("div");
        statusElement.setAttribute("class", "card-status");

        const statusTextElement = document.createElement("span");
        statusTextElement.setAttribute("class", "card-text");
        statusTextElement.textContent = app.status;

        const statusIndicatorElement = document.createElement("span");
        statusIndicatorElement.setAttribute("class", "card-indicator");
        statusIndicatorElement.style.backgroundColor = app.status === "Running" ? "green" : "red";

        // Append child elements to status element
        statusElement.appendChild(statusTextElement);
        statusElement.appendChild(statusIndicatorElement);

        // Append child elements to new div element
        newDiv.appendChild(nameElement);
        newDiv.appendChild(pictureElement);
        newDiv.appendChild(statusElement);

        // Insert the new div element before the first existing card element in the document body
        const currentDiv = document.getElementsByClassName("card")[0];
        document.body.insertBefore(newDiv, currentDiv);
        console.log(app)
    }
}