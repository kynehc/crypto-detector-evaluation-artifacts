package com.example.testkeystoredefuse;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        KeyStoreBuilder builder = new KeyStoreBuilder();
        try {
            builder.loadAppKeyStore();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}