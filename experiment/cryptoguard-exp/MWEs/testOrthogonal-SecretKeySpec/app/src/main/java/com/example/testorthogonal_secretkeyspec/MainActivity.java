package com.example.testorthogonal_secretkeyspec;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;

import java.security.SecureRandom;

import javax.crypto.SecretKey;
import javax.crypto.spec.SecretKeySpec;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        byte[]  keyMaterial = new byte[128];
        SecureRandom sr = new SecureRandom();
        sr.nextBytes(keyMaterial);

        GenericKey genericKey = new GenericKey("KeyAlgo", keyMaterial);
        byte[] encoded = OperatorUtils.getJceKey(genericKey).getEncoded();
        SecretKey keySpec = new SecretKeySpec(encoded, "GOST");
    }
}