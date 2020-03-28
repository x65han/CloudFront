const http = require("http");
const v1 = require('./v1.json');
const fs = require('fs');
const mime = require('mime');

const server = http.createServer(function (req, res) {
    // Route Parsing
    const tokens = req.url.split('/').filter(x => x.length);
    const route = tokens.join('/');

    // static/v1
    if (tokens.length == 2 && tokens[0] === 'static' && tokens[1] == 'v1') {
        sendJSON(res, v1);
    }

    // static/v1/xx
    if (tokens.length == 3 && tokens[0] === 'static' && tokens[1] == 'v1') {
        console.log(`[Route][${route}]`);
        const md5 = tokens[2];
        if (md5 in v1) {
            const fileName = v1[md5];
            console.log(`[Found] ${fileName} -> ${md5}`);
            sendFile(res, fileName, 1);
            return;
        }
    }

    respond(res, 404);
});

// utils
function respond(res, statusCode, body = '') {
    res.writeHead(statusCode, {
        'Content-Length': Buffer.byteLength(body),
        'Content-Type': 'text/plain',
    }).end(body);
}

function sendJSON(res, body) {
    res.writeHead(200, {
        'Content-Type': 'application/json'
    }).end(JSON.stringify(body));
}

function sendFile(res, fileName, version) {
    const fullPath = `./v${version}/${fileName}`;

    if (fs.existsSync(fullPath) === false) {
        console.log(`[senfFile][Not Found] ${fullPath}`);
        respond(res, 404);
    }

    res.writeHead(200, {
        // On Screen
        'Content-Type': mime.getType(fullPath),
        "Content-Disposition": fs.statSync(fullPath).size,
        'Cache-Control': 'max-age=31536000',
        // Direct Download
        // "Content-Type": "application/octet-stream",
        // "Content-Disposition": "attachment; filename=" + fileName,
    });

    var readStream = fs.createReadStream(fullPath);
    readStream.pipe(res);
}

// Port Setup
const PORT = process.env.PORT || 5000;

server.listen(PORT, () => {
    console.log(`Listening on port ${PORT}`);
});