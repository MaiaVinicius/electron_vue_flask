const electron = require('electron');
const app = electron.app;
const BrowserWindow = electron.BrowserWindow;
const path = require('path');


/*************************************************************
 * py process
 *************************************************************/

const PY_DIST_FOLDER = 'myapp/dist';
const PY_FOLDER = 'myapp';
const PY_MODULE = 'api'; // without .py suffix

let pyProc = null;
let pyPort = null;

const guessPackaged = () => {
    const fullPath = path.join(__dirname, PY_DIST_FOLDER);
    return require('fs').existsSync(fullPath)
};

const getScriptPath = () => {
    if (!guessPackaged()) {
        return path.join(__dirname, PY_FOLDER, PY_MODULE + '.py')
    }
    if (process.platform === 'win32') {
        return path.join(__dirname, PY_DIST_FOLDER, PY_MODULE, PY_MODULE + '.exe')
    }

    let isDirectory = require('fs').existsSync(path.join(__dirname, PY_DIST_FOLDER, PY_MODULE, PY_MODULE));

    if (isDirectory) {
        return path.join(__dirname, PY_DIST_FOLDER, PY_MODULE, PY_MODULE)
    }
    return path.join(__dirname, PY_DIST_FOLDER, PY_MODULE)
};

const selectPort = () => {
    pyPort = 5000;
    return pyPort
};

const createPyProc = () => {
    let script = getScriptPath();
    let port = '' + selectPort();


    console.log(script);

    if (guessPackaged()) {
        pyProc = require('child_process').execFile(script)
    } else {
        pyProc = require('child_process').spawn('python', [script])
    }

    if (pyProc !== null) {
        // console.log(pyProc)
        console.log('child process success on port ' + port)
    }
};

const exitPyProc = () => {
    pyProc.kill();
    pyProc = null;
    pyPort = null
};

app.on('ready', createPyProc);
app.on('will-quit', exitPyProc);


/*************************************************************
 * window management
 *************************************************************/

let mainWindow = null;

const createWindow = () => {
    mainWindow = new BrowserWindow({width: 800, height: 600, icon: __dirname + '/static/icons/ico.png'});
    mainWindow.loadURL("http://localhost:5000");
    mainWindow.webContents.openDevTools();

    mainWindow.on('closed', () => {
        mainWindow = null
    })
};

setTimeout(function () {
    app.on('ready', createWindow)
}, 150);

app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') {
        app.quit()
    }
});

app.on('activate', () => {
    if (mainWindow === null) {
        createWindow()
    }
});
