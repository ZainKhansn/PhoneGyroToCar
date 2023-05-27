# SendDataFromAndroidToRaspi
The "Realwifi" app is designed to facilitate sending a message from an Android phone to a Raspberry Pi over a Wi-Fi network.
The app provides a simple user interface with a button that triggers the message sending process.
When the user clicks the "Send" button, the app establishes a socket connection with the Raspberry Pi using the IP address and port specified in the code.
It then sends the message, "Hello from Android!", to the Raspberry Pi using the established socket connection.
To handle the network communication and background task, the app utilizes an AsyncTask or a Runnable executed on a separate thread. 
This ensures that the network operation does not block the main UI thread, providing a smooth user experience.
The Raspberry Pi, acting as the server, should be set up to listen for incoming socket connections on the specified IP address and port.
Upon receiving the message from the Android app, the Raspberry Pi can process the message according to its intended functionality.
To find MainActivity.java app-->src/main-->java/com/example/realwifi -->MainActivity.java
To find Raspberry Pi code raspi_main.py
