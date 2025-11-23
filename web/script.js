const apiUrl = "/api/chat";
let currentCharacterId = "shakespeare"; // Default

// 1. Function to handle Selection
function selectCharacter(id, name, pfpUrl) {
    // Save state
    currentCharacterId = id;

    // Update Chat UI
    document.getElementById("chat-name").innerText = name;
    document.getElementById("chat-avatar").src = pfpUrl;

    // Switch Screens
    document.getElementById("selection-screen").style.display = "none";
    document.getElementById("phone-container").style.display = "flex";

    // Clear previous chat (optional)
    const chatBox = document.getElementById("chat-box");
    chatBox.innerHTML = `
        <div class="message-row bot-row">
            <div class="bubble bot-bubble">
                Hark! 'Tis I, ${name}. Speak thy mind. 👻
            </div>
        </div>`;
}

// 2. Function to go back
function goBack() {
    document.getElementById("phone-container").style.display = "none";
    document.getElementById("selection-screen").style.display = "flex";
}

// 3. Send Message Logic (Updated to send character ID)
async function sendMessage() {
    const inputField = document.getElementById("user-input");
    const message = inputField.value.trim();

    if (!message) return;

    addMessage(message, "user");
    inputField.value = ""; 

    const loadingId = addMessage("Typing...", "bot");

    try {
        const response = await fetch(apiUrl, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            // HERE IS THE MAGIC: We send the character ID too!
            body: JSON.stringify({ 
                message: message, 
                character: currentCharacterId 
            })
        });

        const data = await response.json();

        const loadingBubble = document.getElementById(loadingId);
        if (loadingBubble) {
            loadingBubble.innerText = data.response;
        }

    } catch (error) {
        console.error("Error:", error);
        const loadingBubble = document.getElementById(loadingId);
        if (loadingBubble) loadingBubble.innerText = "Error: Backend unreachable 👻";
    }
}

function addMessage(text, sender) {
    const chatBox = document.getElementById("chat-box");
    const row = document.createElement("div");
    row.classList.add("message-row");
    row.classList.add(sender === "user" ? "user-row" : "bot-row");

    const bubble = document.createElement("div");
    bubble.classList.add("bubble");
    bubble.classList.add(sender === "user" ? "user-bubble" : "bot-bubble");
    bubble.innerText = text;

    const id = "msg-" + Math.random().toString(36).substr(2, 9);
    bubble.id = id;

    row.appendChild(bubble);
    chatBox.appendChild(row);
    chatBox.scrollTop = chatBox.scrollHeight;

    return id;
}

function handleEnter(event) {
    if (event.key === "Enter") sendMessage();
}