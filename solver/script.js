// credit to https://github.com/bryonpokemon/postuwu-woens-discord-token-generator

const se = new WebSocket("ws://127.0.0.1:3200");

se.onmessage = async (message) => {
    const payload = JSON.parse(message.data);
    window.focus();

    const reply = {
        type: "solved",
        token: ""
    };

    try {
        reply.token = await hsw(payload.solve);
    } catch (err) {
        reply.type = "failed";
        reply.token = err.message
    } finally {
        se.send(JSON.stringify(reply));
    }
};