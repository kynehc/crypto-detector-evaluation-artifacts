package com.example.testkeypairgenerator;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.util.Log;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        KeyPairWrapper keyPairWrapper = new KeyPairWrapper();
        try {
            keyPairWrapper.init();
            byte[] n_array = keyPairWrapper.getModulus();
            Log.e("main", toHexString(n_array));
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    // to convert bytes to hex string for output
    public static String toHexString(byte[] bytes) {
        StringBuffer retString = new StringBuffer();
        for (byte b : bytes) {
            retString.append(Integer.toHexString((b & 255) + 256).substring(1));
        }
        return retString.toString();
    }
}