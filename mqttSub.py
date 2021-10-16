import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):            #akan berjalan saat berhasil connect ke broker, yang dijalankan subscribe
    client.subscribe("Angka")

def on_message(client, userdata, message):              #akan berjalan saat ada pesan yang diterima
    hasil = message.payload.decode('utf-8')
    print("Nilai :", hasil)

client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message
client.connect("localhost", 1883, 60)

client.loop_forever()                                   #client nunggu pesan masuk
