package com.example.realwifi;

import android.os.Bundle;
import android.widget.Button;
import androidx.appcompat.app.AppCompatActivity;

import java.io.DataOutputStream;
import java.io.IOException;
import java.io.OutputStream;
import java.net.Socket;
import java.util.concurrent.Executor;
import java.util.concurrent.Executors;

public class MainActivity extends AppCompatActivity {

    private static final String SERVER_IP = "0.0.0.0";  // Replace to IP address of your Raspberry Pi
    private static final int SERVER_PORT = 5000;  // Choose a suitable port number

    private final Executor executor = Executors.newSingleThreadExecutor();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Button sendButton = findViewById(R.id.send_button);
        sendButton.setOnClickListener(view -> {
            String message = "Hello from Android!";
            SendMessageRunnable sendMessageRunnable = new SendMessageRunnable(message);
            executor.execute(sendMessageRunnable);
        });
    }

    private static class SendMessageRunnable implements Runnable {
        private final String message;

        public SendMessageRunnable(String message) {
            this.message = message;
        }

        @Override
        public void run() {
            try {
                Socket socket = new Socket(SERVER_IP, SERVER_PORT);
                OutputStream outputStream = socket.getOutputStream();
                DataOutputStream dataOutputStream = new DataOutputStream(outputStream);
                dataOutputStream.writeUTF(message);
                dataOutputStream.flush();
                dataOutputStream.close();
                socket.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }
}
