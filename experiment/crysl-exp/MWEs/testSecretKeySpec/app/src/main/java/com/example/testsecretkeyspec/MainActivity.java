package com.example.testsecretkeyspec;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;

import java.security.SecureRandom;

import javax.crypto.spec.SecretKeySpec;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        SecureRandom secureRandom = new SecureRandom();
        byte[] bytes = new byte[256];
        secureRandom.nextBytes(bytes);

        SecretKeySpec keySpec = new SecretKeySpec(bytes, "AES");
    }
}