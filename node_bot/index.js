const qrcode=require('qrcode-terminal')
const { Client, LocalAuth } = require('whatsapp-web.js')
const { executablePath } = require('puppeteer');
const chromePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe";


const whatsapp = new Client({
    authStrategy: new LocalAuth(),
    puppeteer: {
        executablePath: chromePath, 
        headless: false,
        args: ['--no-sandbox', '--disable-setuid-sandbox']
    }

})

whatsapp.on('qr', (qr) => {
    qrcode.generate(qr, { small: true });
})


whatsapp.on('ready', async () => {
    console.log('✅ WhatsApp Bot is ready!');
});



whatsapp.on('message_create', async(Message) => {
    const chat = await Message.getChat();
    if(Message.fromMe  && !Message.body.startsWith("🤖:") && chat.id._serialized==='918595562835@c.us'){
        const content = Message.body
        console.log(`💬 You said: ${content}`);
        console.log(chat.id._serialized);


        try {
            const response = await fetch('http://localhost:8000/store_message', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ message: content })
            });

            const data = await response.json();
            console.log("🤖 AI reply:", data.reply);
            if (data.reply) {
                await chat.sendMessage(data.reply);
            }
            if (Message.body.toLowerCase() === 'exit') {
                console.log('👋 Exiting...');
                await whatsapp.destroy();
                process.exit(0);
        }
            
        } catch (error) {
            console.error("❌ Failed to send to Flask:", error);
        }


            
    }
    
})

whatsapp.initialize()