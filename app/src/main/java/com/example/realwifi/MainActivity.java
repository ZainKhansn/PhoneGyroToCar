package com.example.gyrodata;

import androidx.appcompat.app.AppCompatActivity;

import android.hardware.Sensor;
import android.hardware.SensorEvent;
import android.hardware.SensorEventListener;
import android.hardware.SensorManager;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import java.io.DataOutputStream;
import java.io.IOException;
import java.io.OutputStream;
import java.net.Socket;
import java.util.List;
import java.util.concurrent.Executor;
import java.util.concurrent.Executors;

public class MainActivity extends AppCompatActivity implements SensorEventListener {

    private static final String SERVER_IP = "0.0.0.0";  // Replace with the IP address of your Raspberry Pi
    private static final int SERVER_PORT = 5000;  // Choose a suitable port number

    private TextView tv;
    private Socket socket;
    private final Executor executor = Executors.newSingleThreadExecutor();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        tv = findViewById(R.id.textInputLayout);

        Button sendButton = findViewById(R.id.send_button);
        sendButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                initializeSocketConnection();
            }
        });

        SensorManager sm = (SensorManager) getSystemService(SENSOR_SERVICE);
        List<Sensor> typedSensors = sm.getSensorList(Sensor.TYPE_ROTATION_VECTOR);
        if (typedSensors != null && typedSensors.size() > 0) {
            sm.registerListener(this, typedSensors.get(0), SensorManager.SENSOR_DELAY_FASTEST);
        }
    }

    private void initializeSocketConnection() {
        executor.execute(new Runnable() {
            @Override
            public void run() {
                try {
                    socket = new Socket(SERVER_IP, SERVER_PORT);
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        });
    }

    @Override
    public void onSensorChanged(SensorEvent event) {
        float q[] = new float[16];
        float[] orientationTmps = new float[3];

        switch (event.sensor.getType()) {
            case Sensor.TYPE_ROTATION_VECTOR:
                SensorManager.getRotationMatrixFromVector(q, event.values);

                SensorManager.remapCoordinateSystem(q, SensorManager.AXIS_X, SensorManager.AXIS_Z, q);

                SensorManager.getOrientation(q, orientationTmps);

                String out =
                        " X: " + Float.toString((int) Math.toDegrees(orientationTmps[0])) +
                                " Y: " + Float.toString((int) Math.toDegrees(orientationTmps[1])) +
                                " Z: " + Float.toString((int) Math.toDegrees(orientationTmps[2]));
                tv.setText(out);

                if (socket != null && socket.isConnected()) {
                    sendGyroData(out);
                }

                break;
        }
    }

    private void sendGyroData(final String gyroData) {
        executor.execute(new Runnable() {
            @Override
            public void run() {
                try {
                    OutputStream outputStream = socket.getOutputStream();
                    DataOutputStream dataOutputStream = new DataOutputStream(outputStream);
                    dataOutputStream.writeUTF(gyroData);
                    dataOutputStream.flush();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        });
    }

    @Override
    public void onAccuracyChanged(Sensor sensor, int accuracy) {
        // Empty implementation
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        if (socket != null && socket.isConnected()) {
            try {
                socket.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }
}
