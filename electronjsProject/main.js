const electron = require('electron');
const url = require('url');
const path  = require('path');

const {app , BrowserWindow, Menu, ipcMain} = electron;

let mainWindow;
let addWindow;
var fs = require('fs');
var content;




//lesten for app to be ready 
app.on('ready', function(){
    //create new window
    mainWindow = new BrowserWindow({});
    //load html into window
    mainWindow.loadURL(url.format({
        pathname: path.join(__dirname, 'mainWindow.html'),
        protocol: 'file:',
        slashes: true
    }));
    //close the entire program when close the main window
    mainWindow.on('closed', function(){
        app.quit();
    });

    //build menu from template  
    const mainMenu = Menu.buildFromTemplate(mainMenuTemplate);
    //insert menu
    Menu.setApplicationMenu(mainMenu);
});

//handle create add window
function createAddWindow(){
    //create new window
    addWindow = new BrowserWindow({
        width:300,
        height:300,
        title: 'add shopping list item'
    });

    //load html into window
    addWindow.loadURL(url.format({
        pathname: path.join(__dirname, 'addWindow.html'),
        protocol: 'file:',
        slashes: true
    }));
    
    //garpage handling when closeing window
    addWindow.on('closed', function(){
        addWindow = null;
    });
}

//catch item :add
ipcMain.on('item:add', function(e, item){
    var myJSON = JSON.stringify(item);
    myJSON = myJSON.replace("fday", "day");
    myJSON = myJSON.toLowerCase();
    fs.appendFile('reg.txt', myJSON+',\n', function (err) {
        if (err) throw err;
        console.log("added");
      });
      
});

//create menu template
const mainMenuTemplate = [
    {
        label:'file',
        submenu:[
            {
                label: 'Add Item',
                click(){
                    createAddWindow();
                }
            },
            {
                label: 'Clear Items'
            },
            {
                label: 'Quit',
                accelerator: process.platform == 'darwin'? 'command+Q':'ctrl+Q',
                click(){
                    app.quit();
                }
            }
        ]
    },
    
];

if(process.platform == 'darwin'){
    mainMenuTemplate.unshift({});
}

mainMenuTemplate.push({
        label: 'company',
        submenu:[
            {
                lable: 'archtecture',
                accelerator: process.platform == 'darwin'? 'command+a':'ctrl+a',
                click(item, focusedWindow){
                    focusedWindow.toggleDevTools();
                }
            },
            {
                role : 'reload'
            }
        ]
});
