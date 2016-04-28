/*
const net = require('net');

var client = new net.Socket();
client.connect('/Users/carljahn/Documents/IoT-Pi/helper/python/client-server/multiclient/uds_socket', function() {
	console.log('Connected');
});

client.on('data', function(data) {
	console.log(Date.now() + ' Received: ' + data);
	//client.destroy(); // kill client after server's response
});

client.on('close', function() {
	console.log('Connection closed');
});
*/

var amqp = require('amqplib/callback_api');

amqp.connect('amqp://localhost', function(err, conn) {
  conn.createChannel(function(err, ch) {
    var ex = 'logs';
    var msg = process.argv.slice(2).join(' ') || 'Hello World!';

    ch.assertExchange(ex, 'fanout', {durable: false});
    ch.publish(ex, '', new Buffer(msg));
    console.log(" [x] Sent %s", msg);
  });

  setTimeout(function() { conn.close(); process.exit(0) }, 500);
});
